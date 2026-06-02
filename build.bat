@echo off
REM Compila el ejecutable RSS STORE APTAC.exe y empaqueta kingdoms/ e Iconos/.
pyinstaller --onefile --windowed --name "RSS STORE APTAC" ^
  --add-data "kingdoms;kingdoms" ^
  --add-data "Iconos;Iconos" ^
  --add-data "translations.py;." ^
  --add-data "update_helper.py;." ^
  --add-data "requirements.txt;." ^
  --icon "Iconos\Aptac.png" app.py
echo.
echo Build completo. Revisa la carpeta dist\ para encontrar RSS STORE APTAC.exe
pause
