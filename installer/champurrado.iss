[Setup]
AppId={{15C3BB8A-AF0D-4AF4-B5F4-7E421C45C255}
AppName=Champurrado Jumpscare
AppVersion=1.0.0
AppPublisher=Personal
DefaultDirName={autopf}\ChampurradoJumpscare
DefaultGroupName=Champurrado Jumpscare
OutputDir=.
OutputBaseFilename=ChampurradoJumpscare-Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "Crear acceso directo en el escritorio"; GroupDescription: "Accesos directos:"; Flags: unchecked

[Dirs]
Name: "{app}\assets\Champurrado"

[Files]
Source: "..\dist\ChampurradoJumpscare.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\assets\Champurrado\*"; DestDir: "{app}\assets\Champurrado"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Champurrado Jumpscare"; Filename: "{app}\ChampurradoJumpscare.exe"
Name: "{autodesktop}\Champurrado Jumpscare"; Filename: "{app}\ChampurradoJumpscare.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\ChampurradoJumpscare.exe"; Description: "Iniciar Champurrado Jumpscare"; Flags: nowait postinstall skipifsilent
