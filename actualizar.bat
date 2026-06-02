@echo off
REM Script para actualizar RSS STORE APTAC desde la última versión de GitHub
REM Requiere: Python 3.8+ en la variable PATH

echo ====================================
echo  Actualizador - RSS STORE APTAC
echo ====================================
echo.

REM Detectar la ruta de instalación
if exist "app.py" (
    set APP_DIR=%cd%
) else (
    set APP_DIR=%~dp0
)

echo Directorio de aplicación: %APP_DIR%

REM Verificar que update_helper.py existe
if not exist "%APP_DIR%\update_helper.py" (
    echo Error: No se encontró update_helper.py
    echo Por favor descarga el repositorio completo de GitHub
    pause
    exit /b 1
)

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python no está instalado o no está en la variable PATH
    echo Por favor instala Python desde https://www.python.org
    echo Asegúrate de marcar "Add Python to PATH" durante la instalación
    pause
    exit /b 1
)

echo.
echo Descargando versión actual de app.py...
cd /d "%APP_DIR%"

REM Ejecutar update_helper
python update_helper.py 1.0.0 "RSS STORE APTAC.exe"

if errorlevel 0 (
    echo.
    echo ✓ Actualización completada
    echo La próxima vez que ejecutes el programa tendrá los últimos cambios
    timeout /t 5 /nobreak
) else (
    echo.
    echo Error: Fallo en la actualización
    pause
)
