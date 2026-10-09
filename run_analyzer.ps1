<#
================================================================================================
 YouTube 주제 분석기 실행기 (Windows PowerShell)
 VERSION: v1.0 — 2026-10-09 — 분석 코드·설정 파일을 GitHub에서 wget(Invoke-WebRequest)으로 받아 실행
================================================================================================
 처음 한 번 (새 폴더에서):
   1) Python 3.10 이상 설치 — python.org 설치 화면에서 "Add python.exe to PATH" 체크
   2) PowerShell을 열고 작업할 폴더로 이동한 뒤 아래 두 줄 실행
      wget https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.ps1 -OutFile run_analyzer.ps1
      powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1
   3) 처음 실행하면 .env 파일이 생깁니다 → 메모장으로 열어 YOUTUBE_API_KEY(필수)·GITHUB_TOKEN(권장) 입력 → 2)의 둘째 줄 다시 실행

 자주 쓰는 실행:
   powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1                                # 주식 (stock/analyzer_config.toml)
   powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1 -Folder realestate -Topic 부동산   # 다른 주제
   powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1 -UpdateConfig                  # 설정 파일도 GitHub 최신으로 (기존 파일은 .bak)
   powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1 -Branch claude/dreamy-brown-r105x4   # main에 합치기 전 브랜치에서 받기
   powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1 --no-push --cases 3            # 그 밖의 인자는 분석기 옵션으로 전달

 동작: ① youtube_topic_analyzer.py 를 매번 최신으로 받음 (실패하면 있던 파일 사용)
       ② <Folder>/analyzer_config.toml 은 없을 때만 받음 (내가 고친 설정을 덮어쓰지 않음)
       ③ .venv 가상환경을 만들고(처음 한 번) 그 안의 Python으로 실행 — 필요한 패키지는 분석기가 자동 설치
 ※ 'wget'은 Windows PowerShell 5.1에서 Invoke-WebRequest의 별칭입니다. 이 스크립트는 PowerShell 7에서도 되도록 Invoke-WebRequest를 직접 씁니다.
#>
param(
    [string]$Folder = "stock",
    [string]$Topic = "",
    [string]$Repo = "yeomin1024/yeomin1024-ytb",
    [string]$Branch = "main",
    [switch]$UpdateConfig,
    [switch]$NoVenv,
    [Parameter(ValueFromRemainingArguments = $true)][string[]]$AnalyzerArgs
)
$ErrorActionPreference = "Continue"           # 외부 명령(python)의 경고 출력 때문에 멈추지 않게 — 오류는 직접 확인
$ProgressPreference = "SilentlyContinue"      # Invoke-WebRequest 진행 표시 끄기 (PowerShell 5.1에서 다운로드가 매우 느려지는 문제)
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}
try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch {}   # 오래된 Windows의 TLS 설정
if ($PSScriptRoot) { Set-Location -Path $PSScriptRoot }

$Base = if ($env:RAW_BASE) { $env:RAW_BASE } else { "https://raw.githubusercontent.com/$Repo/$Branch" }
$Script = "youtube_topic_analyzer.py"
$Cfg = "$Folder/analyzer_config.toml"

function Write-Step([string]$msg) { Write-Host "[RUNNER] $msg" }

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

# ① 분석 코드 (항상 최신)
if (-not (Get-Remote $Script $Script)) {
    if (Test-Path $Script) { Write-Step "⚠️ 최신 코드를 못 받아서 있던 $Script 로 실행합니다" }
    else {
        Write-Step "❌ $Script 를 받지 못했습니다 → 인터넷 연결과 -Repo/-Branch 값을 확인하세요 (현재: $Repo / $Branch)"
        exit 1
    }
}

# ② 설정 파일 (없을 때만, -UpdateConfig 면 백업 후 최신으로)
if ($UpdateConfig -and (Test-Path $Cfg)) {
    Copy-Item -Force $Cfg "$Cfg.bak"
    Write-Step "기존 설정 파일 백업: $Cfg.bak"
}
if ($UpdateConfig -or -not (Test-Path $Cfg)) {
    if (-not (Get-Remote $Cfg $Cfg)) {
        if (Test-Path $Cfg) { Write-Step "설정 파일은 있던 것을 그대로 씁니다: $Cfg" }
        else { Write-Step "GitHub에 $Cfg 가 없습니다 → 분석기가 새 설정 파일 틀을 만들고 주제어 자동완성 모드로 실행합니다" }
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
$runArgs = @($Script)
if (Test-Path $Cfg) { $runArgs += @("--config", $Cfg) } else { $runArgs += @("--folder", $Folder) }
if ($Topic) { $runArgs += @("--topic", $Topic) }
if ($AnalyzerArgs) { $runArgs += $AnalyzerArgs }
Write-Step "실행: python $($runArgs -join ' ')"
& $pyExe @pyPre @runArgs
$code = $LASTEXITCODE
if ($code -ne 0 -and (Test-Path ".env") -and -not (Select-String -Path ".env" -Pattern "^YOUTUBE_API_KEY=.+" -Quiet)) {
    Write-Step "👉 .env 파일을 메모장으로 열어 YOUTUBE_API_KEY 를 넣고 저장한 뒤 이 스크립트를 다시 실행하세요"
}
exit $code
