$ErrorActionPreference = "Stop"

$ProjectRoot = Resolve-Path "$PSScriptRoot\.."
Set-Location $ProjectRoot

if (!(Test-Path ".venv")) {
    python -m venv .venv
}

.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

pyinstaller --noconsole --onefile --name ChampurradoJumpscare src\champurrado_jumpscare.py

Write-Host "EXE generado en dist\ChampurradoJumpscare.exe"
