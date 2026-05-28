; Installer script for RSS STORE APTAC
; Requires Inno Setup (https://jrsoftware.org/isinfo.php)
; Place a Tesseract archive named "Tesseract-OCR.rar" and a RAR extractor named "rar.exe" next to this script before compiling.

[Setup]
AppName=RSS STORE APTAC
AppVersion=1.0
DefaultDirName={pf}\RSS STORE APTAC
DefaultGroupName=RSS STORE APTAC
OutputBaseFilename=RSS_STORE_APTAC_Installer
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64

[Files]
Source: "dist\RSS STORE APTAC.exe"; DestDir: "{app}"; Flags: ignoreversion

Source: "kingdoms\*"; DestDir: "{app}\kingdoms"; Flags: recursesubdirs createallsubdirs
Source: "Iconos\*"; DestDir: "{app}\Iconos"; Flags: recursesubdirs createallsubdirs

Source: "Tesseract-OCR.rar"; DestDir: "{tmp}"; Flags: ignoreversion deleteafterinstall

[Icons]
Name: "{group}\RSS STORE APTAC"; Filename: "{app}\RSS STORE APTAC.exe"
Name: "{commondesktop}\RSS STORE APTAC"; Filename: "{app}\RSS STORE APTAC.exe"; Tasks: desktopicon

[Tasks]
Name: desktopicon; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked

[Run]
; After installation, offer to run the app
Filename: "{app}\RSS STORE APTAC.exe"; Description: "Launch RSS STORE APTAC"; Flags: nowait postinstall skipifsilent

[Code]

const
  WM_SETTINGCHANGE = $001A;
  SMTO_ABORTIFHUNG = 2;

var
  RarPath: String;


// Windows API para refrescar variables de entorno
function SendMessageTimeout(
  hWnd: Integer;
  Msg: Integer;
  wParam: Integer;
  lParam: Integer;
  fuFlags: Integer;
  uTimeout: Integer;
  var lpdwResult: Integer
): Integer;
external 'SendMessageTimeoutW@user32.dll stdcall';


// Agregar carpeta al PATH del sistema
function AppendToSystemPath(PathToAdd: String): Boolean;
var
  OldPath: String;
  NewPath: String;
  ResultBuf: Integer;
begin
  Result := False;

  // Leer PATH actual
  if not RegQueryStringValue(
    HKLM,
    'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
    'Path',
    OldPath
  ) then
    OldPath := '';

  // Evitar duplicados
  if Pos(LowerCase(PathToAdd), LowerCase(OldPath)) = 0 then
  begin

    if OldPath = '' then
      NewPath := PathToAdd
    else
      NewPath := OldPath + ';' + PathToAdd;

    // Guardar PATH actualizado
    RegWriteStringValue(
      HKLM,
      'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
      'Path',
      NewPath
    );

    // Refrescar variables de entorno
    SendMessageTimeout(
      $FFFF,
      WM_SETTINGCHANGE,
      0,
      0,
      SMTO_ABORTIFHUNG,
      5000,
      ResultBuf
    );

    Result := True;
  end
  else
    Result := True;
end;


// Instalación post setup
procedure CurStepChanged(CurStep: TSetupStep);
var
  ExtractRes: Integer;
  TPath: String;
begin

  if CurStep = ssPostInstall then
  begin

    // Buscar WinRAR instalado
    if FileExists(ExpandConstant('{pf}\WinRAR\Rar.exe')) then
      RarPath := ExpandConstant('{pf}\WinRAR\Rar.exe')
    else if FileExists(ExpandConstant('{pf32}\WinRAR\Rar.exe')) then
      RarPath := ExpandConstant('{pf32}\WinRAR\Rar.exe')
    else
      RarPath := '';



    // Verificar WinRAR
    if RarPath = '' then
    begin
      MsgBox(
        'WinRAR no está instalado.'#13#10#13#10 +
        'No se pudo extraer Tesseract-OCR.',
        mbError,
        MB_OK
      );

      Exit;
    end;



    // Verificar archivo RAR
    if not FileExists(ExpandConstant('{tmp}\Tesseract-OCR.rar')) then
    begin
      MsgBox(
        'No se encontró Tesseract-OCR.rar',
        mbError,
        MB_OK
      );

      Exit;
    end;



    // Extraer Tesseract
    Exec(
      RarPath,
      'x "' +
      ExpandConstant('{tmp}\Tesseract-OCR.rar') +
      '" "' +
      ExpandConstant('{pf}\') +
      '" -y',
      '',
      SW_HIDE,
      ewWaitUntilTerminated,
      ExtractRes
    );



    // Resultado extracción
    if ExtractRes <> 0 then
    begin
      MsgBox(
        'Error extrayendo Tesseract-OCR.'#13#10 +
        'Código: ' + IntToStr(ExtractRes),
        mbError,
        MB_OK
      );

      Exit;
    end
    else
    begin
      MsgBox(
        'Tesseract-OCR instalado correctamente.',
        mbInformation,
        MB_OK
      );
    end;



    // Detectar carpeta correcta
    if DirExists(ExpandConstant('{pf}\Tesseract-OCR\bin')) then
      TPath := ExpandConstant('{pf}\Tesseract-OCR\bin')
    else if DirExists(ExpandConstant('{pf}\Tesseract-OCR')) then
      TPath := ExpandConstant('{pf}\Tesseract-OCR')
    else
      TPath := '';



    // Agregar al PATH
    if TPath <> '' then
    begin

      if AppendToSystemPath(TPath) then
      begin
        MsgBox(
          'Tesseract agregado al PATH:'#13#10#13#10 +
          TPath,
          mbInformation,
          MB_OK
        );
      end
      else
      begin
        MsgBox(
          'No se pudo agregar Tesseract al PATH.',
          mbError,
          MB_OK
        );
      end;

    end
    else
    begin
      MsgBox(
        'No se encontró la carpeta Tesseract-OCR.',
        mbError,
        MB_OK
      );
    end;

  end;

end;