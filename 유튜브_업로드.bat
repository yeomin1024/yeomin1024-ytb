@echo off
rem ==========================================================================================
rem  YouTube upload screen - double-click launcher (Windows)
rem  VERSION: v1.0 - 2026-11-12 - user request: double-click program for the upload screen
rem  1) work folder = this file's folder if run_uploader.ps1 / run_analyzer.ps1 / .env is here,
rem     otherwise Documents\ytb (the analyzer folder)
rem  2) copies itself there + makes a desktop shortcut (first time only)
rem  3) downloads the latest run_uploader.ps1 from GitHub, then runs "run_uploader.ps1 -Web"
rem     (http://127.0.0.1:8770 - this PC only). Close this window to stop the screen.
rem  Open this file in Notepad to read every step. Details: guides/upload_guide.md section 13.
rem  Research/educational tool - not investment advice.
rem ==========================================================================================
setlocal
set "YTB_SELF=%~f0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "$s=[IO.File]::ReadAllText($env:YTB_SELF,[Text.Encoding]::UTF8); $m='#'+'#PS#'+'#'; Invoke-Expression $s.Substring($s.IndexOf($m))"
if errorlevel 1 pause
endlocal
exit /b
##PS##
# ── 여기부터 PowerShell — 위 cmd 줄이 이 아래만 읽어 실행합니다 (cmd 는 exit /b 에서 멈춤) ──
$ErrorActionPreference = 'Continue'
$ProgressPreference = 'SilentlyContinue'
try { [Console]::OutputEncoding = [Text.Encoding]::UTF8 } catch {}
try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch {}
try { $Host.UI.RawUI.WindowTitle = '유튜브 업로드 화면 — 이 창을 닫으면 꺼짐' } catch {}
$Repo = 'yeomin1024/yeomin1024-ytb'
$Name = '유튜브 업로드'
function Say([string]$m) { Write-Host "[LAUNCHER] [$(Get-Date -Format s)] $m" }

# 1) 작업 폴더 — 이 파일 옆에 업로더·분석기 파일이나 .env 가 있으면 여기, 아니면 문서\ytb (guides/pc_analysis.md 의 분석기 폴더)
$self = $env:YTB_SELF
$here = Split-Path -Parent $self
$work = $null
foreach ($f in @('run_uploader.ps1', 'run_analyzer.ps1', '.env')) {
    if (Test-Path -LiteralPath (Join-Path $here $f)) { $work = $here; break }
}
if (-not $work) { $work = Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'ytb' }
if (-not (Test-Path -LiteralPath $work)) {
    New-Item -ItemType Directory -Force -Path $work | Out-Null
    Say "작업 폴더를 만들었습니다: $work"
}
Set-Location -LiteralPath $work
Say "작업 폴더: $work (키 파일 .env · 받은 영상 · 로그가 여기에 생김)"

# 2) 이 파일을 작업 폴더에 두고 바탕화면 바로가기 (처음 한 번 — 다운로드 폴더의 파일을 지워도 바로가기는 그대로)
$keep = Join-Path $work (Split-Path -Leaf $self)
if ($here.TrimEnd('\') -ne $work.TrimEnd('\')) {
    try { Copy-Item -LiteralPath $self -Destination $keep -Force -ErrorAction Stop; Say "이 실행 파일을 작업 폴더에 복사했습니다: $keep" }
    catch { $keep = $self; Say "⚠️ 작업 폴더에 복사하지 못했습니다 (이 자리에서 실행): $($_.Exception.Message)" }
}
try {
    $lnk = Join-Path ([Environment]::GetFolderPath('Desktop')) "$Name.lnk"
    if (-not (Test-Path -LiteralPath $lnk)) {
        $sc = (New-Object -ComObject WScript.Shell).CreateShortcut($lnk)
        $sc.TargetPath = $keep
        $sc.WorkingDirectory = $work
        $sc.Description = '유튜브 업로드 화면 (이 PC 에서만 — http://127.0.0.1:8770)'
        $sc.Save()
        Say "바탕화면에 '$Name' 바로가기를 만들었습니다 — 다음부터는 그것을 더블 클릭"
    }
} catch { Say "⚠️ 바탕화면 바로가기를 만들지 못했습니다 (이 파일을 더블 클릭해도 됩니다): $($_.Exception.Message)" }

# 3) 업로더 실행기를 GitHub 최신으로 (실행기가 화면 코드 tools/*.py 도 다시 최신으로 받음)
$ps1 = Join-Path $work 'run_uploader.ps1'
$tmp = "$ps1.download"
try {
    Invoke-WebRequest -Uri "https://raw.githubusercontent.com/$Repo/main/run_uploader.ps1" -OutFile $tmp -UseBasicParsing -ErrorAction Stop
    if ((Get-Item -LiteralPath $tmp).Length -le 0) { throw '빈 파일' }
    Move-Item -LiteralPath $tmp -Destination $ps1 -Force
    Say '받음: run_uploader.ps1 (GitHub 최신)'
} catch {
    Remove-Item -LiteralPath $tmp -Force -ErrorAction SilentlyContinue
    if (Test-Path -LiteralPath $ps1) { Say "⚠️ 최신 실행기를 받지 못해 있던 run_uploader.ps1 로 엽니다: $($_.Exception.Message)" }
    else { Say "❌ run_uploader.ps1 을 받지 못했습니다 → 인터넷 연결을 확인하고 다시 더블 클릭하세요: $($_.Exception.Message)"; exit 1 }
}

# 4) 업로드 화면 — 브라우저가 저절로 열림 (8770 이 쓰이고 있으면 다음 빈 번호) · 이 창을 닫으면 화면도 꺼짐
Say '업로드 화면을 엽니다 — 브라우저가 열리지 않으면 아래에 나온 http://127.0.0.1:… 주소를 여세요. 끝낼 때는 이 창을 닫으면 됩니다.'
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File $ps1 -Web
exit $LASTEXITCODE
