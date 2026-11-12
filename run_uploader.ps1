<#
================================================================================================
 YouTube 업로드 PC 실행기 (Windows PowerShell)
 VERSION: v1.2 — 2026-11-12 — 더블 클릭 실행 파일 '유튜브_업로드.bat' 이 이 스크립트를 받아 -Web 으로 실행 (사용자 지시 "그냥 더블 클릭하면 실행되는
          프로그램으로 만들어서 내가 다운 받을 수 있게 해줘") · Python 이 없으면 -Web·-Auth 때 winget 으로 설치할지 물음(Y 일 때만) ·
          PATH 에 없는 Python(%LOCALAPPDATA%\Programs\Python\Python3*) 도 찾음.
 (v1.1 — 2026-11-12 — **-Web: 업로드 화면** (사용자 지시 "…내가 업로드 버튼 누르면 일주일 후 자동 예약으로 올라가게 해줘 토큰 만료되면 알아서
          인증 코드 돌려서 설정 넣어주도록 하고 필요한 환경변수 값들 넣을 수 있는 웹 사이트 코드 만들어줘 주제별로 가능하도록 해줘"):
          tools/upload_web.py 를 받아 이 PC 에서만 열리는 화면(http://127.0.0.1:8770) — 주제 탭 · 키 칸(<주제>/.env) · 자료 점검 · [업로드] = 7일 뒤 17:00 예약 ·
          토큰 만료면 브라우저 인증을 저절로. 영상은 GitHub 'uploads' 브랜치 조각을 받아 이어 붙임 (Drive 원본이 없어도).)
 (v1.0 — 2026-10-15 — 사용자 지시 "압축본 올린거 삭제하고 구글 드라이브 내 드라이브에 youtube 폴더에 주제 (예: economic)맞는 폴더에
          원본 영상 올리고 pc에서 영상 및 환경설정을 받아서 업로드 하는 코드 만들어서 올리는 걸로 하자 자동 예약 기능도 있어야해"
          코드(tools/pc_upload.py 등)를 GitHub 에서 받고 → GitHub 의 업로드 설정 + Google Drive 내 드라이브/youtube/<주제>/<영상ID>.mp4 원본으로
          유튜브에 비공개 업로드 + 예약 공개(기본: 실행 시각 + 1시간) → youtube.json 을 GitHub 에 기록. 연구·교육용 — 투자·세무·보험 상담 아님.
================================================================================================
 처음 한 번 (자세히: guides/upload_guide.md 11번):
   1) 분석기와 같은 폴더(예: 문서\ytb)에서 이 스크립트를 받는다
      curl.exe -L -o run_uploader.ps1 https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_uploader.ps1
   2) powershell -ExecutionPolicy Bypass -File run_uploader.ps1 -Auth
      → .env 에 YOUTUBE_CLIENT_ID · YOUTUBE_CLIENT_SECRET 를 먼저 넣으라고 하면 메모장으로 넣고 다시
      → 브라우저에서 유튜브 채널 계정으로 로그인·허용 (체크 칸 모두) → 새 YOUTUBE_REFRESH_TOKEN(유튜브 + Drive 권한)이 .env 에 저장됨
      → 같은 3개 값을 Claude Code 클라우드 환경에도 넣으면 Claude 가 렌더 뒤 원본을 Drive 에 바로 올린다
   3) .env 의 GITHUB_TOKEN (분석기와 같은 토큰, Contents 쓰기) — 올린 기록(youtube.json)을 GitHub 에 남김

 자주 쓰는 실행:
   유튜브_업로드.bat 더블 클릭                                                     # ★★★ (v1.2) 아래 -Web 과 같음 — 받기: GitHub main 의 유튜브_업로드.bat
   powershell -ExecutionPolicy Bypass -File run_uploader.ps1 -Web                  # ★★ (v1.1) 업로드 화면 — 주제별 키 · 자료 점검 · [업로드] 7일 뒤 예약
   powershell -ExecutionPolicy Bypass -File run_uploader.ps1                       # ★ 준비된 영상 전부 → 지금부터 1시간 뒤 공개
   powershell -ExecutionPolicy Bypass -File run_uploader.ps1 -DryRun               # 올리지 않고 확인만 (설정·Drive 영상·예약 시각)
   powershell -ExecutionPolicy Bypass -File run_uploader.ps1 -Gap 24h              # 여러 개면 하루에 하나씩 공개 (첫 영상 1시간 뒤)
   powershell -ExecutionPolicy Bypass -File run_uploader.ps1 -At "2026-10-16 18:00"   # 첫 영상 공개 시각을 직접 (한국 시간)
   powershell -ExecutionPolicy Bypass -File run_uploader.ps1 -Ids isa-mangi-2026-10    # 그 영상만
   powershell -ExecutionPolicy Bypass -File run_uploader.ps1 -RegisterTask         # 자동: 1시간마다 새로 준비된 영상을 올림 (각각 1시간 뒤 공개)
   powershell -ExecutionPolicy Bypass -File run_uploader.ps1 -UnregisterTask       # 자동 끄기
 동작: ① 코드(tools/pc_upload.py · drive_videos.py · youtube_upload.py · srt_tool.py · subtitle_widths.json · youtube_auth.py)는 매번 최신으로
       ② .env 에 업로드 키 줄이 없으면 더함 (있는 값은 건드리지 않음, 값은 화면에 쓰지 않음)
       ③ .venv (분석기와 같이 씀) + Pillow (ffmpeg 없는 PC 에서 썸네일 변환) → python tools/pc_upload.py
       ④ 로그: logs\uploader_<날짜>.log
#>
param(
    [string]$Topic = "economic",
    [string]$Delay = "1h",
    [string]$At = "",
    [string]$Gap = "0m",
    [string]$Ids = "",
    [int]$Max = 4,
    [switch]$DryRun,
    [switch]$KeepVideo,
    [switch]$Auth,
    [switch]$RegisterTask,
    [switch]$UnregisterTask,
    [int]$EveryHours = 1,
    [string]$Repo = "yeomin1024/yeomin1024-ytb",
    [string]$Branch = "main",
    [switch]$NoVenv,
    [switch]$Web,
    [int]$Port = 8770,
    [Parameter(ValueFromRemainingArguments = $true)][string[]]$ExtraArgs
)
$ErrorActionPreference = "Continue"
$ProgressPreference = "SilentlyContinue"
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}
try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch {}
if ($PSScriptRoot) { Set-Location -Path $PSScriptRoot }

$Base = "https://raw.githubusercontent.com/$Repo/$Branch"
$CodeFiles = @("tools/pc_upload.py", "tools/drive_videos.py", "tools/youtube_upload.py", "tools/srt_tool.py", "tools/subtitle_widths.json",
               "tools/youtube_auth.py", "tools/upload_web.py", "tools/upload_pack.py")
$TaskName = "YouTubeUpload_$Topic"
function Write-Step([string]$msg) { Write-Host "[UPLOADER] [$(Get-Date -Format s)] $msg" }

# ② .env — 업로드 키 줄 (없을 때만 더함). 값은 화면에 쓰지 않는다
$EnvBlock = @"

# ── 유튜브 업로드 (run_uploader.ps1) — 절대 공유하지 마세요. 자세히: guides/upload_guide.md 11번
# Google Cloud 콘솔 → 사용자 인증 정보 → OAuth 클라이언트(데스크톱 앱)의 ID·보안 비밀번호
YOUTUBE_CLIENT_ID=
YOUTUBE_CLIENT_SECRET=
# 비워 두고 'run_uploader.ps1 -Auth' 를 실행하면 브라우저 허용 뒤 저절로 채워짐 (유튜브 + Google Drive 권한)
YOUTUBE_REFRESH_TOKEN=
# (선택) Google Drive 데스크톱 앱의 '내 드라이브' 경로 — 비우면 G:\내 드라이브 등을 찾아보고, 없으면 Drive API 로 받음
DRIVE_DIR=
"@
if (-not (Test-Path ".env")) {
    Set-Content -Path ".env" -Value "# 비밀 키 파일 — 절대 GitHub 에 올리거나 공유하지 마세요`r`n# [올린 기록·비공개 저장소] GitHub 토큰 (Contents: Read and write)`r`nGITHUB_TOKEN=" -Encoding UTF8
}
$envText = Get-Content ".env" -Raw -Encoding UTF8
if ($envText -notmatch "(?m)^\s*YOUTUBE_REFRESH_TOKEN\s*=") {
    Add-Content -Path ".env" -Value $EnvBlock -Encoding UTF8
    Write-Step "📝 .env 에 유튜브 업로드 키 줄을 더했습니다 → 메모장으로 YOUTUBE_CLIENT_ID·YOUTUBE_CLIENT_SECRET 를 넣고 '-Auth' 로 실행"
}
function Get-Secret([string]$Name) {
    $v = [Environment]::GetEnvironmentVariable($Name)
    if ($v -and $v.Trim()) { return $v.Trim() }
    foreach ($line in (Get-Content ".env" -Encoding UTF8)) {
        if ($line -match "^\s*$Name\s*=\s*['`"]?([^'`"\s]+)") { return $Matches[1] }
    }
    return ""
}

# 작업 스케줄러 (자동 업로드)
if ($UnregisterTask) {
    schtasks /Delete /TN $TaskName /F | Out-Null
    if ($LASTEXITCODE -eq 0) { Write-Step "자동 업로드를 껐습니다: $TaskName" } else { Write-Step "등록된 자동 업로드가 없습니다: $TaskName" }
    exit 0
}
if ($RegisterTask) {
    $self = Join-Path (Get-Location) "run_uploader.ps1"
    $tr = "powershell -NoProfile -ExecutionPolicy Bypass -File `"$self`" -Topic $Topic -Delay $Delay -Gap $Gap -Max $Max -Branch $Branch"
    schtasks /Create /TN $TaskName /TR $tr /SC HOURLY /MO $EveryHours /F | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Step "자동 업로드 등록: $EveryHours 시간마다 새로 준비된 영상(업로드 시트 + Drive 원본)을 올리고 각각 $Delay 뒤 공개 ($TaskName)"
        Write-Step "PC 가 켜져 있고 로그인돼 있어야 돕니다. 로그: logs\uploader_<날짜>.log · 끄기: -UnregisterTask"
        exit 0
    }
    Write-Step "❌ 자동 업로드 등록 실패 → PowerShell 을 다시 열어 시도하거나 작업 스케줄러 앱에서 직접 만드세요"
    exit 1
}

# ① 코드 (항상 최신)
$Token = Get-Secret "GITHUB_TOKEN"
function Get-Remote([string]$RelPath, [string]$OutFile) {
    $tmp = "$OutFile.download"
    $dir = Split-Path -Parent $OutFile
    if ($dir -and -not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
    try {
        if ($Token) {    # 비공개 저장소도 — 토큰은 머리글로만
            $headers = @{ Authorization = "Bearer $Token"; "X-GitHub-Api-Version" = "2022-11-28"; Accept = "application/vnd.github.raw" }
            Invoke-WebRequest -Uri "https://api.github.com/repos/$Repo/contents/$RelPath`?ref=$Branch" -Headers $headers -OutFile $tmp -UseBasicParsing -ErrorAction Stop
        } else {
            Invoke-WebRequest -Uri "$Base/$RelPath" -OutFile $tmp -UseBasicParsing -ErrorAction Stop
        }
        if ((Get-Item $tmp).Length -le 0) { throw "빈 파일" }
        Move-Item -Force $tmp $OutFile
        Write-Step "받음: $RelPath"
        return $true
    } catch {
        if (Test-Path $tmp) { Remove-Item -Force $tmp }
        Write-Step "받기 실패: $RelPath ($($_.Exception.Message))"
        return $false
    }
}
foreach ($f in $CodeFiles) {
    if (-not (Get-Remote $f $f)) {
        if (Test-Path $f) { Write-Step "⚠️ 최신 $f 를 못 받아서 있던 파일로 실행합니다" }
        else { Write-Step "❌ $f 를 받지 못했습니다 → 인터넷 연결, 비공개 저장소면 .env 의 GITHUB_TOKEN 확인"; exit 1 }
    }
}

# ③ Python + 가상환경 + Pillow
function Find-Python {
    foreach ($cand in @(@("py", "-3"), @("python"), @("python3"))) {
        if (-not (Get-Command $cand[0] -ErrorAction SilentlyContinue)) { continue }
        $pre = @()
        if ($cand.Count -gt 1) { $pre = $cand[1..($cand.Count - 1)] }
        & $cand[0] @pre -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" 2>$null | Out-Null
        if ($LASTEXITCODE -eq 0) { return , @($cand) }
    }
    # (v1.2) PATH 에 없는 설치본 — 이 사용자용 · 모든 사용자용 (새 버전 먼저)
    $dirs = @("$env:LOCALAPPDATA\Programs\Python", "$env:ProgramFiles")
    foreach ($exe in ($dirs | ForEach-Object { Get-ChildItem -Path $_ -Filter "Python3*" -Directory -ErrorAction SilentlyContinue } |
                      Sort-Object Name -Descending | ForEach-Object { Join-Path $_.FullName "python.exe" })) {
        if (-not (Test-Path $exe)) { continue }
        & $exe -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" 2>$null | Out-Null
        if ($LASTEXITCODE -eq 0) { return , @($exe) }
    }
    return $null
}
$py = Find-Python
# (v1.2) 없으면 화면(-Web)·인증(-Auth) 때만 설치할지 묻는다 — 예약 작업(-RegisterTask 로 돈 실행)에서는 묻지 않음
if (-not $py -and ($Web -or $Auth) -and (Get-Command winget -ErrorAction SilentlyContinue)) {
    Write-Step "Python 3.10 이상이 없습니다. 지금 설치할까요? (winget · Python 3.12 · 이 사용자만 · 몇 분) — Y 를 누르고 Enter"
    $ans = Read-Host "설치 [Y/N]"
    if ($ans -match '^\s*(y|yes|ㅛ|예|네)\s*$') {
        winget install -e --id Python.Python.3.12 --scope user --accept-package-agreements --accept-source-agreements
        $env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [Environment]::GetEnvironmentVariable("Path", "User")
        $py = Find-Python
        if ($py) { Write-Step "Python 설치 완료: $($py -join ' ')" }
    } else { Write-Step "설치하지 않았습니다" }
}
if (-not $py) { Write-Step "❌ Python 3.10 이상이 없습니다 → https://www.python.org/downloads/ ('Add python.exe to PATH' 체크)"; exit 1 }
$pyExe = $py[0]
$pyPre = @()
if ($py.Count -gt 1) { $pyPre = $py[1..($py.Count - 1)] }
if (-not $NoVenv) {
    $venvPy = ".venv\Scripts\python.exe"
    if (-not (Test-Path $venvPy)) {
        Write-Step "가상환경(.venv) 만드는 중 (처음 한 번)"
        & $pyExe @pyPre -m venv .venv
        if ($LASTEXITCODE -ne 0) { Remove-Item -Recurse -Force ".venv" -ErrorAction SilentlyContinue; Write-Step "⚠️ 가상환경 실패 → 시스템 Python 으로 실행" }
    }
    if (Test-Path $venvPy) { $pyExe = $venvPy; $pyPre = @() }
}
& $pyExe @pyPre -c "import PIL" 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Step "Pillow 설치 (썸네일 변환 — 처음 한 번)"
    & $pyExe @pyPre -m pip install -q pillow
}

# -Auth: 리프레시 토큰 (유튜브 + Drive 권한) 발급 → .env 에 저장
if ($Auth) {
    $cid = Get-Secret "YOUTUBE_CLIENT_ID"
    $csec = Get-Secret "YOUTUBE_CLIENT_SECRET"
    if (-not $cid -or -not $csec) { Write-Step "❌ .env 에 YOUTUBE_CLIENT_ID · YOUTUBE_CLIENT_SECRET 를 먼저 넣고 다시 -Auth (guides/pipeline.md '처음 한 번 할 일' B)"; exit 1 }
    & $pyExe @pyPre tools/youtube_auth.py --client-id $cid --client-secret $csec --save-env .env
    exit $LASTEXITCODE
}

# -Web (v1.1): 업로드 화면 — 창을 닫으면 꺼짐
if ($Web) {
    $env:PYTHONIOENCODING = "utf-8"; $env:PYTHONUTF8 = "1"
    Write-Step "업로드 화면을 엽니다 → 브라우저 http://127.0.0.1:$Port/ (이 창을 닫으면 화면도 꺼짐)"
    & $pyExe @pyPre tools/upload_web.py --port $Port --repo $Repo
    exit $LASTEXITCODE
}

# ④ 업로드
$runArgs = @("tools/pc_upload.py", "--topic", $Topic, "--delay", $Delay, "--gap", $Gap, "--max", "$Max", "--repo", $Repo, "--branch", $Branch)
if ($At) { $runArgs += @("--at", $At) }
if ($Ids) { $runArgs += @("--ids", $Ids) }
if ($DryRun) { $runArgs += "--dry-run" }
if ($KeepVideo) { $runArgs += "--keep-video" }
if ($ExtraArgs) { $runArgs += $ExtraArgs }
if (-not (Test-Path "logs")) { New-Item -ItemType Directory -Path "logs" | Out-Null }
$log = "logs\uploader_$(Get-Date -Format yyyy-MM-dd).log"
$env:PYTHONIOENCODING = "utf-8"; $env:PYTHONUTF8 = "1"     # 로그 파일로 넘길 때 한글이 깨지지 않게 (콘솔도 UTF-8)
Write-Step "실행: python $($runArgs -join ' ')  (로그 $log)"
& $pyExe @pyPre @runArgs 2>&1 | Tee-Object -FilePath $log -Append
$code = $LASTEXITCODE
if ($code -ne 0) { Write-Step "끝 (종료 코드 $code) — 위 표에서 failed·no_video·not_run 줄과 [VIDEO] ok=False 로그를 확인하세요" }
exit $code
