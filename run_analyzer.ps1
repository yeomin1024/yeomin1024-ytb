<#
================================================================================================
 YouTube 분석 PC 실행기 (Windows PowerShell)
 VERSION: v2.0 — 2026-10-13 — 기본 주제 economic(경제·재테크). 분석기 + 작은 채널 성공 사례(자막·썸네일·댓글)를
          tools/pc_analysis.py 로 함께 돌리고, 할당량이 끝나 못 한 부분은 할당량 초기화(한국 오후 4~5시) 뒤 자동으로 이어서.
          검색어 목록 <Folder>/keywords.toml 도 받음. -Once · -RegisterTask(작업 스케줄러) · -AnalyzerOnly(예전 방식) 추가
 (v1.0 — 2026-10-09 — 분석 코드·설정 파일을 GitHub에서 받아 분석기만 실행)
================================================================================================
 처음 한 번 (자세히: guides/pc_analysis.md):
   1) Python 3.10 이상 설치 — python.org 설치 화면에서 "Add python.exe to PATH" 체크
   2) PowerShell을 열고 작업할 폴더(예: 문서\ytb)로 이동한 뒤 아래 두 줄 실행
      wget https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.ps1 -OutFile run_analyzer.ps1
      powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1
   3) 처음 실행하면 .env 파일이 생깁니다 → 메모장으로 열어 YOUTUBE_API_KEY(필수)·GITHUB_TOKEN(권장) 입력·저장 → 2)의 둘째 줄 다시 실행

 자주 쓰는 실행:
   powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1                 # 경제·재테크 — 끝날 때까지 (남으면 다음 날 자동으로 이어서, 창을 열어 두기)
   powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1 -Once           # 한 회차만 (남은 부분은 다음에 실행할 때)
   powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1 -RegisterTask   # 매일 17:15 에 -Once 로 자동 실행 (창을 닫아도 됨, PC는 켜져 있어야)
   powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1 -UnregisterTask # 자동 실행 끄기
   powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1 -UpdateConfig   # 설정·검색어 파일도 GitHub 최신으로 (기존 파일은 .bak)
   powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1 -AnalyzerOnly   # 예전처럼 분석기만 한 번
   powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1 --dry-run       # 그 밖의 인자는 tools/pc_analysis.py 로 (-AnalyzerOnly 면 분석기로)

 동작: ① 코드(youtube_topic_analyzer.py · tools/pc_analysis.py · tools/outlier_research.py · tools/outlier_stats.py)는 매번 최신으로 받음
       ② <Folder>/analyzer_config.toml · <Folder>/keywords.toml 은 없을 때만 받음 (내가 고친 설정·검색어를 덮어쓰지 않음)
       ③ .venv 가상환경을 만들고(처음 한 번) 그 안의 Python으로 실행 — 필요한 패키지는 자동 설치
 ※ 'wget'은 Windows PowerShell 5.1에서 Invoke-WebRequest의 별칭입니다. 이 스크립트는 PowerShell 7에서도 되도록 Invoke-WebRequest를 직접 씁니다.
#>
param(
    [string]$Folder = "economic",
    [string]$Repo = "yeomin1024/yeomin1024-ytb",
    [string]$Branch = "main",
    [switch]$UpdateConfig,
    [switch]$NoVenv,
    [switch]$Once,
    [switch]$AnalyzerOnly,
    [switch]$RegisterTask,
    [switch]$UnregisterTask,
    [string]$TaskTime = "17:15",
    [Parameter(ValueFromRemainingArguments = $true)][string[]]$ExtraArgs
)
$ErrorActionPreference = "Continue"           # 외부 명령(python)의 경고 출력 때문에 멈추지 않게 — 오류는 직접 확인
$ProgressPreference = "SilentlyContinue"      # Invoke-WebRequest 진행 표시 끄기 (PowerShell 5.1에서 다운로드가 매우 느려지는 문제)
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}
try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch {}   # 오래된 Windows의 TLS 설정
if ($PSScriptRoot) { Set-Location -Path $PSScriptRoot }

$Base = if ($env:RAW_BASE) { $env:RAW_BASE } else { "https://raw.githubusercontent.com/$Repo/$Branch" }
$CodeFiles = @("youtube_topic_analyzer.py", "tools/pc_analysis.py", "tools/outlier_research.py", "tools/outlier_stats.py")
$ConfigFiles = @("$Folder/analyzer_config.toml", "$Folder/keywords.toml")
$TaskName = "YouTubeAnalysis_$Folder"

function Write-Step([string]$msg) { Write-Host "[RUNNER] [$(Get-Date -Format s)] $msg" }

# 작업 스케줄러 등록/해제 (코드 받기 전에 처리 — 등록만 하고 끝)
if ($UnregisterTask) {
    schtasks /Delete /TN $TaskName /F | Out-Null
    if ($LASTEXITCODE -eq 0) { Write-Step "자동 실행을 껐습니다: $TaskName" } else { Write-Step "등록된 자동 실행이 없습니다: $TaskName" }
    exit 0
}
if ($RegisterTask) {
    $self = Join-Path (Get-Location) "run_analyzer.ps1"
    $tr = "powershell -NoProfile -ExecutionPolicy Bypass -File `"$self`" -Folder $Folder -Branch $Branch -Once"
    schtasks /Create /TN $TaskName /TR $tr /SC DAILY /ST $TaskTime /F | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Step "매일 $TaskTime 에 자동 실행 등록: $TaskName (할당량 초기화 = 한국 오후 4시, 미국 표준시 기간 11~3월엔 5시 → $TaskTime 이면 둘 다 지남)"
        Write-Step "PC가 켜져 있고 로그인돼 있어야 돕니다. 확인: 작업 스케줄러 앱 → '작업 스케줄러 라이브러리' → $TaskName · 끄기: -UnregisterTask"
        exit 0
    }
    Write-Step "❌ 자동 실행 등록 실패 → PowerShell을 다시 열어 시도하거나, 작업 스케줄러 앱에서 직접 만드세요 (guides/pc_analysis.md)"
    exit 1
}

function Get-Remote([string]$RelPath, [string]$OutFile) {
    $url = "$Base/$RelPath"
    $tmp = "$OutFile.download"
    $dir = Split-Path -Parent $OutFile
    if ($dir -and -not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
    try {
        Invoke-WebRequest -Uri $url -OutFile $tmp -UseBasicParsing -ErrorAction Stop    # = wget
        if ((Get-Item $tmp).Length -le 0) { throw "빈 파일" }
        Move-Item -Force $tmp $OutFile
        Write-Step "받음: $RelPath"
        return $true
    } catch {
        if (Test-Path $tmp) { Remove-Item -Force $tmp }
        Write-Step "받기 실패: $url ($($_.Exception.Message))"
        return $false
    }
}

function Find-Python {
    foreach ($cand in @(@("py", "-3"), @("python"), @("python3"))) {
        if (-not (Get-Command $cand[0] -ErrorAction SilentlyContinue)) { continue }
        $pre = @()
        if ($cand.Count -gt 1) { $pre = $cand[1..($cand.Count - 1)] }
        & $cand[0] @pre -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" 2>$null | Out-Null
        if ($LASTEXITCODE -eq 0) { return , @($cand) }
    }
    return $null
}

# ① 코드 (항상 최신, 못 받으면 있던 파일)
foreach ($f in $CodeFiles) {
    if (-not (Get-Remote $f $f)) {
        if (Test-Path $f) { Write-Step "⚠️ 최신 $f 를 못 받아서 있던 파일로 실행합니다" }
        else {
            Write-Step "❌ $f 를 받지 못했습니다 → 인터넷 연결과 -Repo/-Branch 값을 확인하세요 (현재: $Repo / $Branch)"
            exit 1
        }
    }
}

# ② 설정·검색어 파일 (없을 때만, -UpdateConfig 면 백업 후 최신으로)
foreach ($c in $ConfigFiles) {
    if ($UpdateConfig -and (Test-Path $c)) {
        Copy-Item -Force $c "$c.bak"
        Write-Step "기존 파일 백업: $c.bak"
    }
    if ($UpdateConfig -or -not (Test-Path $c)) {
        if (-not (Get-Remote $c $c)) {
            if (Test-Path $c) { Write-Step "있던 파일을 그대로 씁니다: $c" }
            else { Write-Step "⚠️ GitHub에 $c 가 없습니다 → -Folder 이름을 확인하세요 (현재: $Folder)" }
        }
    }
}

# ③ Python + 가상환경
$py = Find-Python
if (-not $py) {
    Write-Step "❌ Python 3.10 이상을 찾지 못했습니다 → https://www.python.org/downloads/ 에서 설치 ('Add python.exe to PATH' 체크) 후 다시 실행"
    exit 1
}
$pyExe = $py[0]
$pyPre = @()
if ($py.Count -gt 1) { $pyPre = $py[1..($py.Count - 1)] }
if (-not $NoVenv) {
    if (-not (Test-Path ".venv\Scripts\python.exe")) {
        Write-Step "가상환경(.venv) 만드는 중 (처음 한 번)"
        & $pyExe @pyPre -m venv .venv
        if ($LASTEXITCODE -ne 0) { Write-Step "❌ 가상환경을 만들지 못했습니다 → -NoVenv 로 다시 실행해 보세요"; exit 1 }
    }
    $pyExe = ".venv\Scripts\python.exe"
    $pyPre = @()
}

# ④ 실행
$cfg = "$Folder/analyzer_config.toml"
if ($AnalyzerOnly) {
    $runArgs = @("youtube_topic_analyzer.py", "--config", $cfg)
} else {
    $runArgs = @("tools/pc_analysis.py", $Folder)
    if ($Once) { $runArgs += "--once" }
}
if ($ExtraArgs) { $runArgs += $ExtraArgs }
Write-Step "실행: python $($runArgs -join ' ')"
& $pyExe @pyPre @runArgs
$code = $LASTEXITCODE
if ($code -eq 3) { Write-Step "할당량 때문에 남은 부분이 있습니다 → 다음 실행(또는 작업 스케줄러)이 이어서 받습니다" }
if ($code -ne 0 -and $code -ne 3 -and (Test-Path ".env") -and -not (Select-String -Path ".env" -Pattern "^YOUTUBE_API_KEY=.+" -Quiet)) {
    Write-Step "👉 .env 파일을 메모장으로 열어 YOUTUBE_API_KEY 를 넣고 저장한 뒤 이 스크립트를 다시 실행하세요"
}
exit $code
