# 🔧 Guía de Compilación con PyInstaller

## Para compilar tu aplicación a un .exe con soporte multiidioma

---

## Requisitos Previos

```bash
# Python 3.7+
python --version

# Instalar PyInstaller
pip install pyinstaller

# Instalar pytesseract y PIL (si no están)
pip install pytesseract pillow
```

---

## Paso 1: Preparar la Carpeta

```
C:\Users\Aptac\Desktop\Bot Resources\
├── app.py
├── translations.py          ← IMPORTANTE: Incluir este archivo
├── Iconos/
├── kingdoms/
├── Tesseract-OCR/
└── build.bat                ← Script de compilación
```

---

## Paso 2: Crear Script de Compilación

Crea o actualiza `build.bat`:

```batch
@echo off
REM Script para compilar RSS STORE APTAC con PyInstaller

echo ============================================
echo Compilando RSS STORE APTAC...
echo ============================================

REM Limpiar builds anteriores
rmdir /s /q build dist

REM Compilar con PyInstaller
pyinstaller --onefile ^
    --windowed ^
    --icon=Iconos\Aptac.png ^
    --add-data "Iconos:Iconos" ^
    --add-data "kingdoms:kingdoms" ^
    --add-data "translations.py:." ^
    --name "RSS STORE APTAC" ^
    app.py

echo.
echo ============================================
echo Compilación completada!
echo El .exe está en: dist\RSS STORE APTAC.exe
echo ============================================
pause
```

---

## Paso 3: Compilación Automática

### Opción A: Usar el script build.bat
```bash
cd "C:\Users\Aptac\Desktop\Bot Resources"
build.bat
```

### Opción B: Compilación manual con PyInstaller
```bash
cd "C:\Users\Aptac\Desktop\Bot Resources"

pyinstaller --onefile ^
    --windowed ^
    --icon=Iconos\Aptac.png ^
    --add-data "Iconos:Iconos" ^
    --add-data "kingdoms:kingdoms" ^
    --add-data "translations.py:." ^
    --name "RSS STORE APTAC" ^
    app.py
```

---

## Paso 4: Verificación

Después de compilar:

1. **Busca el .exe**
   ```
   C:\Users\Aptac\Desktop\Bot Resources\dist\RSS STORE APTAC.exe
   ```

2. **Prueba el .exe**
   - Haz doble clic en `RSS STORE APTAC.exe`
   - Debería funcionar como la versión Python
   - Verifica que el selector de idiomas aparezca

3. **Prueba cada idioma**
   - Cambia a cada uno de los 6 idiomas
   - Verifica que todo se traduce correctamente

---

## Paso 5: Distribución

### Para Compartir con Usuarios

```
RSS STORE APTAC - Installer/
├── RSS STORE APTAC.exe          ← Aplicación compilada
├── README.txt                   ← Instrucciones
├── CAMBIOS.txt                  ← Notas de versión
└── installer.iss                ← (Opcional) Script Inno Setup
```

### Crear Instalador con Inno Setup (Opcional)

1. Abre `installer.iss`
2. Apunta a: `dist\RSS STORE APTAC.exe`
3. Compila con Inno Setup
4. Distribuye el `.exe` del instalador

---

## 📦 Archivos que SE INCLUYEN Automáticamente

Con la compilación de PyInstaller:

✅ `app.py` → compilado en el .exe  
✅ `translations.py` → incluido con `--add-data`  
✅ `Iconos/` → incluido con `--add-data`  
✅ Todas las dependencias de Python  

---

## ⚠️ Archivos que DEBES INCLUIR Manualmente

Si quieres distribuir con archivos extra:

```
RSS STORE APTAC.exe (compilado)
└─ ACOMPAÑADO DE:
   ├── kingdoms/           (Opcional: si quieres pre-cargar)
   ├── Tesseract-OCR/      (Si quieres OCR incorporado)
   └── README.md           (Documentación)
```

### O mejor: Distribuir todo como carpeta

```
RSS STORE APTAC - v1.0/
├── RSS STORE APTAC.exe
├── kingdoms/
├── Iconos/
├── Tesseract-OCR/
├── LANGUAGE_SUPPORT.md
├── VISUAL_GUIDE.md
└── README.md
```

---

## 🧪 Testing Post-Compilación

Después de compilar, prueba:

```
1. Abrir la aplicación
2. Ver que abre sin errores
3. Ver selector de idiomas
4. Cambiar a cada idioma
5. Verificar que texto se traduce
6. Procesar una imagen
7. Guardar resultado
8. Verificar .txt está OK
9. Cerrar y volver a abrir
10. Cambiar idioma de nuevo
```

---

## 🐛 Solución de Problemas

### Problema: "No encuentra translations.py"
**Solución**: Usa `--add-data "translations.py:."`

### Problema: "No encuentra Iconos"
**Solución**: Usa `--add-data "Iconos:Iconos"`

### Problema: "Falta pytesseract"
**Solución**: 
```bash
pip install pytesseract
pyinstaller ... (con --hidden-import=pytesseract si es necesario)
```

### Problema: El .exe es muy grande (>500MB)
**Solución**: Es normal con Tesseract-OCR. Excluye con:
```bash
--exclude-module Tesseract-OCR
```

### Problema: Se abre pero cierra inmediatamente
**Solución**: Ejecuta desde terminal para ver error:
```bash
"dist\RSS STORE APTAC.exe"
```

---

## 📊 Tamaño Esperado

| Componente | Tamaño |
|-----------|--------|
| app.py + translations.py | ~100 KB |
| Python runtime | ~50 MB |
| Dependencies (PIL, pytesseract) | ~30 MB |
| Iconos incluidos | ~500 KB |
| **TOTAL SIN Tesseract** | ~80 MB |
| Tesseract-OCR (opcional) | ~450 MB |
| **TOTAL CON Tesseract** | ~530 MB |

---

## 🚀 Flujo Completo de Compilación

```
1. Verificar que todo funciona en Python:
   python app.py
   ✓ Cambiar idiomas
   ✓ Procesar imágenes

2. Compilar:
   build.bat
   (o comando manual de PyInstaller)

3. Esperar a que termine (~5-10 min)

4. Probar .exe:
   dist\RSS STORE APTAC.exe
   ✓ Mismo test que en Python

5. Distribuir:
   Copiar dist\RSS STORE APTAC.exe
   (+ archivos complementarios si es necesario)
```

---

## 📝 Especificaciones del .exe Compilado

```
Archivo: RSS STORE APTAC.exe
Tipo: Ejecutable Windows
Arquitectura: x86 (32-bit) o x64 (64-bit)
Requisitos: Windows 7+
Dependencias: Ninguna (todo incluido)
Idiomas: 6 (ES, EN, PT, ID, VI, FR)
Tamaño: ~80-530 MB (depende de opciones)
```

---

## ✅ Checklist Pre-Compilación

- [ ] `translations.py` existe en la carpeta
- [ ] `app.py` funciona correctamente en Python
- [ ] `python test_translations.py` pasa todas las pruebas
- [ ] He probado cambiar idiomas
- [ ] He probado procesar imágenes
- [ ] He guardado un archivo .txt
- [ ] PyInstaller está instalado: `pip install pyinstaller`
- [ ] Tengo script build.bat actualizado

---

## ✅ Checklist Post-Compilación

- [ ] El .exe se encuentra en `dist/`
- [ ] El .exe abre sin errores
- [ ] El selector de idiomas aparece
- [ ] Puedo cambiar a cada idioma
- [ ] El texto se traduce correctamente
- [ ] Puedo procesar imágenes
- [ ] Los .txt se guardan correctamente
- [ ] El .exe se puede cerrar sin errores

---

## 🎯 Comandos Rápidos

### Compilación simple
```bash
pyinstaller --onefile --windowed app.py
```

### Compilación completa (recomendada)
```bash
pyinstaller --onefile --windowed --icon=Iconos\Aptac.png ^
    --add-data "Iconos:Iconos" ^
    --add-data "kingdoms:kingdoms" ^
    --add-data "translations.py:." ^
    --name "RSS STORE APTAC" app.py
```

### Limpiar antes de compilar
```bash
rmdir /s /q build dist
```

### Verificar que existe el .exe
```bash
dir dist\*.exe
```

---

## 📚 Documentación Relacionada

- `LANGUAGE_SUPPORT.md` - Sistema de traducciones
- `LANGUAGE_CHANGES.md` - Cambios en app.py
- `CHECKLIST.md` - Verificación completa
- `test_translations.py` - Validación del sistema

---

## 🎁 Extra: Crear Instalador con Inno Setup

Si quieres crear un instalador profesional:

1. Descarga Inno Setup: https://jrsoftware.org/isdl.php
2. Abre tu `installer.iss`
3. Cambia la ruta del .exe:
   ```
   Source: "dist\RSS STORE APTAC.exe"; DestDir: "{app}"
   ```
4. Compila en Inno Setup
5. Distribuye el .exe del instalador

---

**Última actualización**: 2025  
**Versión**: 1.0.0  
**Estado**: ✅ Listo para compilar
