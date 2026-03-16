$ErrorActionPreference = "Stop"

$ProjectRoot = Resolve-Path "$PSScriptRoot\.."
Set-Location $ProjectRoot

$InnoCompiler = "C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
if (!(Test-Path $InnoCompiler)) {
    throw "No se encontró Inno Setup en '$InnoCompiler'. Instala Inno Setup 6 y vuelve a intentar."
}

if (!(Test-Path "dist\ChampurradoJumpscare.exe")) {
    throw "No existe dist\ChampurradoJumpscare.exe. Ejecuta primero scripts\build.ps1"
}

& $InnoCompiler "installer\champurrado.iss"
Write-Host "Instalador generado en installer\ChampurradoJumpscare-Setup.exe"
