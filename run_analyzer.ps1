<#
================================================================================================
 YouTube 분석 PC 실행기 (Windows PowerShell)
 VERSION: v3.6 — 2026-10-28 — -Transcribe: 대본만 받기 (사용자 지시: "그럼 대본 받아야하는 목록 정해서 pc 실행하면 저장소에 올리는 코드 알려줘") —
          tools/pc_transcribe.py run <주제>: GitHub 의 <주제>/result/outliers/transcript_todo.csv 순서대로 자막 → 없으면 음성인식(앞 5분 → 끝까지),
          대본 두 파일(transcript.json·.txt)만 GitHub API 로 main 에. 웹 화면·분석기는 켜지 않음 (클라우드 주제의 사례 폴더를 덮지 않게)
 (v3.5 — 2026-10-15 — 웹 화면 v2.0 (한 화면·주제 탭 — 사용자 지시: "하나의 사이트에서 그냥 탭 만들어서 다른 주제 볼 수 있게 하자"):
          -Folder 없이 켜면 저장소의 topics.txt 주제 전부(지금 economic·stock)를 받아 한 화면의 탭으로. -Folder economic,stock 도 창 하나에 탭 둘
          (예전처럼 주제마다 창이 뜨지 않음 — 예전 창은 닫고 다시). 자동 실행(-Auto·-Once·-RegisterTask)은 그대로 -Folder (기본 economic))
 (v3.4 — 2026-10-15 — -ResetCache: 이 주제의 탐색 캐시·탐색 목록을 치운 뒤 평소처럼 실행 (지우지 않고 .yt_work/old/ 로 옮김 —
          승인한 자료·분석 결과는 그대로. 사용자 지시: "왜 예전 재테크 캐시가 남아 있어 이거 어떻게해"). tools/pc_analysis.py v1.13)
 (v3.3 — 2026-10-15 — 코드 목록에 tools/shorts_analysis.py (쇼츠 분석 — 사용자 지시: "… 쇼츠 분석 기능도 추가해 … 전력을 다해서
          해봐"). 웹 화면 v1.6 의 4번 칸 [롱폼 | 쇼츠]. 실행 명령은 같음)
 (v3.2 — 2026-10-15 — 안내만 (사용자 지시: "분석기 여러개 열어서 각자 다른 주제로 탐색해도 되지? … economic 같은 주제 경로를
          선택할 수 있게해서 각각 주제별로 탐색할 수 있게"): 웹 화면 v1.5 — -Folder economic,health 면 주제마다 창(포트)을 하나씩 띄움,
          같은 주제 창이 이미 있으면 그 창을 엶. 할당량은 같은 키의 모든 창이 함께 셈(화면 위 '남은 할당량'), 초기화 뒤 남은 것은 저절로 이어서)
 (v3.1 — 2026-10-14 — 코드 목록에 tools/success_analysis.py(성공 사례 분석 analysis.md), 설정 목록에 <주제>/analysis_rules.toml
          (사용자 지시: "… 올바른 분석 결과까지만 내도록 수정해"). 웹 화면 v1.3 도 켤 때 코드를 받으므로 예전 실행기로도 새 도구가 옴)
 (v3.0 — 2026-10-14 — 실행하면 웹 화면이 뜸 (사용자 지시: "이거 분석기 웹 ui 형식으로 만들어 실행하면 바로 웹 ui가 나와서 env,
          검색어 수정할 수 있게하고 탐색 버튼 누르면 … 승인 버튼을 눌러야 관련 자료를 받아서 분석"): 기본 = tools/web_ui.py (브라우저에
          http://127.0.0.1:8765/). 예전 자동 실행(할당량이 끝나면 다음 날 이어서)은 -Auto, -Once·작업 스케줄러도 자동 실행.
          코드 목록에 tools/web_ui.py·tools/weekly_analysis.py 추가)
 (v2.5 — 2026-10-13 — 검색어 목록 <주제>/keywords.txt (한 줄에 하나, 그룹 없음)도 받음 (사용자 지시: "걍 검색어 내가 수정해도
          돌아가게 하면 안돼?"). GitHub 에서 고친 설정·검색어는 tools/pc_analysis.py v1.7 이 회차마다 받아 씀 (VERSION 안 올려도 됨))
 (v2.4 — 2026-10-13 — pip 이 없는 가상환경 고침 (사용자 PC 오류: ".venv\Scripts\python.exe: No module named pip"):
          ① .venv 에 pip 이 없으면 ensurepip 로 설치 (안 되면 분석 코드가 공식 get-pip.py 로 한 번 더)
          ② .venv 만들기가 실패하면 반쯤 만든 .venv 를 지움 (남겨 두면 다음 실행이 pip 없는 .venv 를 씀) → pip 없이 만들어
             분석 코드가 pip 을 설치하게 함)
 (v2.3 — 2026-10-13 — 검색어를 태그로 바꾼 새 판을 PC 가 자동으로 받게 (사용자 지시: "그냥 검색어를 재테크 관련 태그로 찾아서
          다 그걸로 탐색해봐"): 설정·검색어 파일(<주제>/analyzer_config.toml·keywords.toml·tag_rules.toml)은 PC 에 있어도
          GitHub 쪽 파일 머리의 VERSION 이 더 높으면 예전 것을 .bak 으로 두고 새 판으로 바꿈 (같거나 낮으면, VERSION 이 없으면 그대로).
          코드 목록에 tools/tag_keywords.py (태그에서 검색어 고르기) 추가)
 (v2.2.1 — 2026-10-13 — 안내 문구만: 실행 명령을 -File run_analyzer.ps1 (.\ 없이 — Git Bash 가 \ 를 지워 '-File 인수가 없습니다' 오류),
          받기는 curl.exe (코드 동작은 v2.2 그대로))
 (v2.2 — 2026-10-13 — 여러 주제를 동시에: -Folder economic,health (사용자 지시: "동시에 병렬로 다른 주제 분석도 가능하도록").
          주제마다 <주제>/analyzer_config.toml·keywords.toml 을 받고(없을 때만), tools/pc_analysis.py 가 주제마다 따로 돌림.
          주제별 키는 <주제>/.env (없으면 맨 위 .env))
 (v2.1 — 2026-10-13 — 비공개 저장소에서도 받기: .env(또는 환경 변수)의 GITHUB_TOKEN 이 있으면 GitHub API 로 코드·설정을 받음
          (사용자 지시: "비공개로 돌릴테니까 전부 다 업로드되게"). .env 가 없으면 먼저 틀을 만듦. 토큰 값은 화면에 쓰지 않음)
 (v2.0 — 2026-10-13 — 기본 주제 economic(경제·재테크). 분석기 + 작은 채널 성공 사례(자막·썸네일·댓글)를
          tools/pc_analysis.py 로 함께 돌리고, 할당량이 끝나 못 한 부분은 할당량 초기화(한국 오후 4~5시) 뒤 자동으로 이어서.
          검색어 목록 <Folder>/keywords.toml 도 받음. -Once · -RegisterTask(작업 스케줄러) · -AnalyzerOnly(예전 방식) 추가)
 (v1.0 — 2026-10-09 — 분석 코드·설정 파일을 GitHub에서 받아 분석기만 실행)
================================================================================================
 처음 한 번 (자세히: guides/pc_analysis.md):
   1) Python 3.10 이상 설치 — python.org 설치 화면에서 "Add python.exe to PATH" 체크
   2) PowerShell을 열고 작업할 폴더(예: 문서\ytb)로 이동한 뒤 이 스크립트를 받아 실행
      (저장소가 공개일 때) curl.exe -L -o run_analyzer.ps1 https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.ps1
      (저장소가 비공개일 때 — 토큰을 물어봄, 화면에 남지 않음) guides/pc_analysis.md "처음 한 번" 4번의 두 줄
      powershell -ExecutionPolicy Bypass -File run_analyzer.ps1
   3) 처음 실행하면 .env 파일이 생깁니다 → 메모장으로 열어 YOUTUBE_API_KEY(필수)·GITHUB_TOKEN(권장) 입력·저장 → 2)의 둘째 줄 다시 실행

 자주 쓰는 실행:
   powershell -ExecutionPolicy Bypass -File run_analyzer.ps1                 # ★ 웹 화면 — 주제(재테크·주식 …)는 위쪽 탭 (topics.txt 전부)
   powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Folder stock   # 웹 화면을 주식 탭부터 (PC 에 있는 다른 주제도 탭으로 보임)
   powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Auto           # 예전 자동 실행 — 끝날 때까지 (남으면 다음 날 이어서, 창을 열어 두기)
   powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Auto -Folder economic,health   # 자동 실행 여러 주제 동시에
   powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Once           # 자동 실행 한 회차만 (남은 부분은 다음에 실행할 때)
   powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -RegisterTask   # 매일 17:15 에 -Once 로 자동 실행 (창을 닫아도 됨, PC는 켜져 있어야)
   powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -UnregisterTask # 자동 실행 끄기
   powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -UpdateConfig   # 설정·검색어 파일도 GitHub 최신으로 (기존 파일은 .bak)
   powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -ResetCache -Folder stock   # 이 주제 탐색 캐시·탐색 목록 치우고 실행 (.yt_work/old/ 로 옮김)
   powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -AnalyzerOnly   # 예전처럼 분석기만 한 번
   powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Transcribe -Folder stock            # ★ 대본만 받아 올리기 (목록 순서대로, 멈췄다 다시 하면 이어서)
   powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Transcribe -Folder stock --limit 5  # 시험 삼아 5개만 (그 밖: --korean-only · --no-whisper · --model medium)
   powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 --port 8800     # 그 밖의 인자는 웹 화면(tools/web_ui.py)으로 (-Auto 면 pc_analysis.py, -AnalyzerOnly 면 분석기로)

 동작: ① 코드(youtube_topic_analyzer.py · tools/pc_analysis.py · tools/outlier_research.py · tools/outlier_stats.py · tools/tag_keywords.py)는 매번 최신으로 받음
       ② <Folder>/analyzer_config.toml · keywords.toml · keywords.txt(검색어) · tag_rules.toml 은 없을 때(또는 VERSION 이 더 높을 때) 받고,
          실행 중에는 tools/pc_analysis.py 가 회차마다 GitHub 에서 고친 것을 받음
          (예전 것은 .bak — 같은 판이면 내가 고친 설정·검색어를 덮어쓰지 않음)
       ③ .venv 가상환경을 만들고(처음 한 번) 그 안의 Python으로 실행 — 필요한 패키지는 자동 설치
 ※ 'wget'은 Windows PowerShell 5.1에서 Invoke-WebRequest의 별칭입니다. 이 스크립트는 PowerShell 7에서도 되도록 Invoke-WebRequest를 직접 씁니다.
#>
param(
    [string[]]$Folder = @("economic"),
    [string]$Repo = "yeomin1024/yeomin1024-ytb",
    [string]$Branch = "main",
    [switch]$UpdateConfig,
    [switch]$ResetCache,
    [switch]$NoVenv,
    [switch]$Once,
    [switch]$Auto,
    [switch]$AnalyzerOnly,
    [switch]$Transcribe,
    [switch]$RegisterTask,
    [switch]$UnregisterTask,
    [string]$TaskTime = "17:15",
    [Parameter(ValueFromRemainingArguments = $true)][string[]]$ExtraArgs
)
$FolderGiven = $PSBoundParameters.ContainsKey("Folder")    # v3.5: 안 주면 웹 화면은 topics.txt 주제 전부 (탭)
$ErrorActionPreference = "Continue"           # 외부 명령(python)의 경고 출력 때문에 멈추지 않게 — 오류는 직접 확인
$ProgressPreference = "SilentlyContinue"      # Invoke-WebRequest 진행 표시 끄기 (PowerShell 5.1에서 다운로드가 매우 느려지는 문제)
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}
try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch {}   # 오래된 Windows의 TLS 설정
if ($PSScriptRoot) { Set-Location -Path $PSScriptRoot }

$Base = if ($env:RAW_BASE) { $env:RAW_BASE } else { "https://raw.githubusercontent.com/$Repo/$Branch" }
$Folder = @($Folder | ForEach-Object { $_ -split "," } | ForEach-Object { $_.Trim() } | Where-Object { $_ })   # -File 로 부르면 "a,b" 한 글자열
if (-not $Folder) { $Folder = @("economic") }
$CodeFiles = @("youtube_topic_analyzer.py", "tools/pc_analysis.py", "tools/outlier_research.py", "tools/outlier_stats.py", "tools/tag_keywords.py",
               "tools/web_ui.py", "tools/weekly_analysis.py", "tools/success_analysis.py", "tools/shorts_analysis.py", "tools/pc_transcribe.py")
$ConfigFiles = @($Folder | ForEach-Object { "$_/analyzer_config.toml"; "$_/keywords.toml"; "$_/keywords.txt"; "$_/tag_rules.toml"; "$_/analysis_rules.toml" })
$TaskName = "YouTubeAnalysis_" + ($Folder -join "_")

function Write-Step([string]$msg) { Write-Host "[RUNNER] [$(Get-Date -Format s)] $msg" }

# .env 틀 (없을 때만) — 비공개 저장소는 GITHUB_TOKEN 이 있어야 코드를 받으므로 먼저 만든다. 값은 화면에 쓰지 않는다
$EnvTemplate = @"
# YouTube 분석 비밀 키 파일 — 절대 GitHub 에 올리거나 공유하지 마세요
# '=' 뒤에 값을 붙여넣고 저장 (따옴표 필요 없음). 자세히: guides/pc_analysis.md

# [필수] YouTube Data API v3 키 (Google Cloud 콘솔 → API 및 서비스 → 사용자 인증 정보 → API 키)
YOUTUBE_API_KEY=

# [비공개 저장소면 필수] GitHub 토큰 (Fine-grained, 저장소 yeomin1024-ytb, Contents: Read and write) — 코드 받기·결과 올리기
GITHUB_TOKEN=
"@
function Get-Secret([string]$Name) {
    $v = [Environment]::GetEnvironmentVariable($Name)
    if ($v -and $v.Trim()) { return $v.Trim() }
    if (Test-Path ".env") {
        foreach ($line in (Get-Content ".env" -Encoding UTF8)) {
            if ($line -match "^\s*$Name\s*=\s*['`"]?([^'`"\s]+)") { return $Matches[1] }
        }
    }
    return ""
}

# 작업 스케줄러 등록/해제 (코드 받기 전에 처리 — 등록만 하고 끝)
if ($UnregisterTask) {
    schtasks /Delete /TN $TaskName /F | Out-Null
    if ($LASTEXITCODE -eq 0) { Write-Step "자동 실행을 껐습니다: $TaskName" } else { Write-Step "등록된 자동 실행이 없습니다: $TaskName" }
    exit 0
}
if ($RegisterTask) {
    $self = Join-Path (Get-Location) "run_analyzer.ps1"
    $tr = "powershell -NoProfile -ExecutionPolicy Bypass -File `"$self`" -Folder $($Folder -join ',') -Branch $Branch -Auto -Once"   # 자동 실행 (화면 없이)
    schtasks /Create /TN $TaskName /TR $tr /SC DAILY /ST $TaskTime /F | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Step "매일 $TaskTime 에 자동 실행 등록: $TaskName (할당량 초기화 = 한국 오후 4시, 미국 표준시 기간 11~3월엔 5시 → $TaskTime 이면 둘 다 지남)"
        Write-Step "PC가 켜져 있고 로그인돼 있어야 돕니다. 확인: 작업 스케줄러 앱 → '작업 스케줄러 라이브러리' → $TaskName · 끄기: -UnregisterTask"
        exit 0
    }
    Write-Step "❌ 자동 실행 등록 실패 → PowerShell을 다시 열어 시도하거나, 작업 스케줄러 앱에서 직접 만드세요 (guides/pc_analysis.md)"
    exit 1
}

if (-not (Test-Path ".env")) {
    Set-Content -Path ".env" -Value $EnvTemplate -Encoding UTF8
    Write-Step "📝 .env 파일을 만들었습니다 → 메모장으로 열어 YOUTUBE_API_KEY·GITHUB_TOKEN 을 넣고 저장하세요"
}
$Token = Get-Secret "GITHUB_TOKEN"
$UseApi = [bool]($Token -and -not $env:RAW_BASE)
Write-Step "코드 받는 방법: $(if ($UseApi) { 'GitHub API + 토큰 (비공개 저장소도 됨)' } else { '공개 주소 (토큰 없음 — 저장소가 비공개면 실패)' })"

function Get-Remote([string]$RelPath, [string]$OutFile) {
    $url = "$Base/$RelPath"
    $tmp = "$OutFile.download"
    $dir = Split-Path -Parent $OutFile
    if ($dir -and -not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
    try {
        if ($UseApi) {    # 비공개 저장소: GitHub API (Contents, base64 — 1MB 이하 파일) — 토큰은 머리글로만, 화면에 쓰지 않음
            $url = "https://api.github.com/repos/$Repo/contents/$RelPath" + "?ref=$Branch"
            $headers = @{ Authorization = "Bearer $Token"; "X-GitHub-Api-Version" = "2022-11-28" }
            $r = Invoke-RestMethod -Uri $url -Headers $headers -UseBasicParsing -ErrorAction Stop
            if (-not $r.content) { throw "내용 없음 (1MB 넘는 파일이거나 폴더)" }
            [IO.File]::WriteAllBytes((Join-Path (Get-Location).Path $tmp), [Convert]::FromBase64String(($r.content -replace "\s", "")))
        } else {
            Invoke-WebRequest -Uri $url -OutFile $tmp -UseBasicParsing -ErrorAction Stop    # = wget
        }
        if ((Get-Item $tmp).Length -le 0) { throw "빈 파일" }
        Move-Item -Force $tmp $OutFile
        Write-Step "받음: $RelPath"
        return $true
    } catch {
        if (Test-Path $tmp) { Remove-Item -Force $tmp }
        Write-Step "받기 실패: $url ($($_.Exception.Message))"
        if (-not $UseApi) { Write-Step "👉 저장소가 비공개면 .env 에 GITHUB_TOKEN 을 넣고 다시 실행하세요" }
        else { Write-Step "👉 토큰이 이 저장소를 읽을 수 있는지 확인: Repository access 에 yeomin1024-ytb · Contents 권한 (guides/pc_analysis.md)" }
        return $false
    }
}

function Get-FileVersion([string]$Path) {
    # 파일 머리(처음 15줄)의 'VERSION: v2.0' → [version] (없으면 $null) — 설정 파일 새 판 알아보기 (v2.3)
    if (-not (Test-Path $Path)) { return $null }
    foreach ($line in (Get-Content -Path $Path -TotalCount 15 -Encoding UTF8)) {
        if ($line -match 'VERSION:\s*v(\d+(?:\.\d+){0,3})') {
            $v = $Matches[1]
            if ($v -notmatch '\.') { $v = "$v.0" }
            return [version]$v
        }
    }
    return $null
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

# ①-1 주제 목록 (v3.5) — -Folder 없이 웹 화면을 켜면 저장소 topics.txt 의 주제 전부를 받아 탭으로 (자동 실행은 -Folder 그대로)
if ($Transcribe -and -not $FolderGiven) {    # v3.6: 대본 받기는 주제를 꼭 정함 (웹 화면 탭 목록을 쓰지 않음)
    Write-Step "❌ -Transcribe 는 주제를 정해 주세요 → 예: -Transcribe -Folder stock"
    exit 1
}
if (-not $FolderGiven -and -not ($Auto -or $Once -or $AnalyzerOnly -or $Transcribe)) {
    if (Get-Remote "topics.txt" "topics.txt") {
        $list = @(Get-Content -Path "topics.txt" -Encoding UTF8 | ForEach-Object { $_.Trim() } |
                  Where-Object { $_ -and -not $_.StartsWith("#") -and $_ -match '^[a-z][a-z0-9_-]{1,30}$' })
        if ($list) { $Folder = $list }
    }
    $ConfigFiles = @($Folder | ForEach-Object { "$_/analyzer_config.toml"; "$_/keywords.toml"; "$_/keywords.txt"; "$_/tag_rules.toml"; "$_/analysis_rules.toml" })
    Write-Step "주제 탭: $($Folder -join ', ') (저장소 topics.txt — 한 주제부터 열려면 -Folder stock)"
}

# ② 설정·검색어 파일 (없을 때만, -UpdateConfig 면 백업 후 최신으로, GitHub 쪽 VERSION 이 더 높으면 백업 후 새 판으로 — v2.3)
foreach ($c in $ConfigFiles) {
    if (-not $UpdateConfig -and (Test-Path $c)) {
        $remote = "$c.remote"
        if (Get-Remote $c $remote) {
            $lv = Get-FileVersion $c
            $rv = Get-FileVersion $remote
            if ($lv -and $rv -and ($rv -gt $lv)) {
                Copy-Item -Force $c "$c.bak"
                Move-Item -Force $remote $c
                Write-Step "🔄 새 판으로 바꿈: $c (v$lv → v$rv). 예전 파일은 $c.bak — 내가 고친 내용이 있었다면 거기서 옮기세요"
            } else {
                Remove-Item -Force $remote
                Write-Step "있던 파일 그대로: $c (PC v$lv · GitHub v$rv)"
            }
        } else {
            Write-Step "있던 파일을 그대로 씁니다: $c"
        }
        continue
    }
    if ($UpdateConfig -and (Test-Path $c)) {
        Copy-Item -Force $c "$c.bak"
        Write-Step "기존 파일 백업: $c.bak"
    }
    if ($UpdateConfig -or -not (Test-Path $c)) {
        if (-not (Get-Remote $c $c)) {
            if (Test-Path $c) { Write-Step "있던 파일을 그대로 씁니다: $c" }
            else { Write-Step "⚠️ GitHub에 $c 가 없습니다 → -Folder 이름을 확인하세요 (현재: $($Folder -join ', ')). 새 주제는 Claude 에게 '<주제> 검색어 만들어줘'" }
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
    $venvPy = ".venv\Scripts\python.exe"
    if (-not (Test-Path $venvPy)) {
        Write-Step "가상환경(.venv) 만드는 중 (처음 한 번)"
        & $pyExe @pyPre -m venv .venv
        if ($LASTEXITCODE -ne 0) {     # 반쯤 만든 .venv 를 남기지 않음 (v2.4) → pip 없이 다시 만들고 pip 은 아래에서
            Write-Step "⚠️ 가상환경 만들기 실패 → 지우고 pip 없이 다시 만듦 (pip 은 다음 단계에서 설치)"
            Remove-Item -Recurse -Force ".venv" -ErrorAction SilentlyContinue
            & $pyExe @pyPre -m venv --without-pip .venv
            if ($LASTEXITCODE -ne 0) {
                Remove-Item -Recurse -Force ".venv" -ErrorAction SilentlyContinue
                Write-Step "❌ 가상환경을 만들지 못했습니다 → -NoVenv 로 다시 실행하거나, python.org 에서 Python 을 다시 설치하세요"
                exit 1
            }
        }
    }
    # pip 확인 (v2.4): 만들다 끊긴 .venv 는 python.exe 만 있고 pip 이 없음 ('No module named pip') → ensurepip
    & $venvPy -m pip --version 2>$null | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Step "⚠️ 가상환경(.venv)에 pip 이 없습니다 → ensurepip 로 설치"
        & $venvPy -m ensurepip --upgrade --default-pip
        & $venvPy -m pip --version 2>$null | Out-Null
        if ($LASTEXITCODE -eq 0) { Write-Step "pip 준비됨" }
        else { Write-Step "⚠️ ensurepip 실패 → 분석 코드가 공식 get-pip.py 로 한 번 더 시도합니다 (그래도 안 되면 .venv 폴더를 지우고 다시 실행)" }
    }
    $pyExe = $venvPy
    $pyPre = @()
}

# ③-1 캐시 치우기 (v3.4) — 이 주제의 탐색 캐시·탐색 목록만, 지우지 않고 .yt_work/old/ 로 옮긴 뒤 평소처럼 실행
if ($ResetCache) {
    $resetArgs = @("tools/pc_analysis.py") + $Folder + @("--reset-cache")
    Write-Step "캐시 치우기: python $($resetArgs -join ' ')"
    & $pyExe @pyPre @resetArgs
    if ($LASTEXITCODE -ne 0) { Write-Step "⚠️ 캐시 치우기 실패 (위 줄 확인) — 그대로 실행합니다" }
}

# ④ 실행
if ($Transcribe) {      # v3.6: 대본만 받기 — 웹 화면·분석기를 켜지 않고, 대본 두 파일만 GitHub 에 (tools/pc_transcribe.py)
    $runArgs = @("tools/pc_transcribe.py", "run") + $Folder
    if ($ExtraArgs) { $runArgs += $ExtraArgs }
    Write-Step "대본 받기: python $($runArgs -join ' ') — 멈추려면 Ctrl+C (받은 것은 먼저 올리고 끝남, 다시 실행하면 이어서)"
    & $pyExe @pyPre @runArgs
    $code = $LASTEXITCODE
} elseif ($AnalyzerOnly) {    # 예전 방식: 분석기만, 주제마다 차례로
    $code = 0
    foreach ($f in $Folder) {
        $runArgs = @("youtube_topic_analyzer.py", "--config", "$f/analyzer_config.toml")
        if ($ExtraArgs) { $runArgs += $ExtraArgs }
        Write-Step "실행: python $($runArgs -join ' ')"
        & $pyExe @pyPre @runArgs
        if ($LASTEXITCODE -ne 0) { $code = $LASTEXITCODE }
    }
} elseif ($Auto -or $Once) {    # 예전 자동 실행 (할당량이 끝나면 다음 날 이어서)
    $runArgs = @("tools/pc_analysis.py") + $Folder     # 주제가 여러 개면 동시에 (pc_analysis.py 가 주제마다 따로 띄움)
    if ($Once) { $runArgs += "--once" }
    if ($ExtraArgs) { $runArgs += $ExtraArgs }
    Write-Step "실행: python $($runArgs -join ' ')"
    & $pyExe @pyPre @runArgs
    $code = $LASTEXITCODE
} else {                         # 기본: 웹 화면 (v3.0) — 브라우저가 저절로 열림, 이 창을 닫으면 화면도 꺼짐
    $runArgs = @("tools/web_ui.py") + $Folder
    if ($ExtraArgs) { $runArgs += $ExtraArgs }
    Write-Step "웹 화면 실행: python $($runArgs -join ' ') — 브라우저가 저절로 열림 (주제는 화면 위쪽 탭, 주소는 아래 ▶ 줄, 끝내려면 이 창에서 Ctrl+C)"
    & $pyExe @pyPre @runArgs
    $code = $LASTEXITCODE
}
if ($code -eq 3) { Write-Step "할당량 때문에 남은 부분이 있습니다 → 다음 실행(또는 작업 스케줄러)이 이어서 받습니다" }
if ($code -ne 0 -and $code -ne 3 -and (Test-Path ".env") -and -not (Select-String -Path ".env" -Pattern "^YOUTUBE_API_KEY=.+" -Quiet)) {
    Write-Step "👉 .env 파일을 메모장으로 열어 YOUTUBE_API_KEY 를 넣고 저장한 뒤 이 스크립트를 다시 실행하세요"
}
exit $code
