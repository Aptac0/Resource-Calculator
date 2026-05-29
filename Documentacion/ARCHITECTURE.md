# 🏗️ Arquitectura del Sistema de Actualizaciones

## 📊 Estructura del Proyecto en GitHub

```
Resource-Calculator/
├── app.py                    ← Aplicación principal
├── build.bat                 ← Script para compilar
├── installer.iss             ← Inno Setup installer
├── kingdoms/                 ← DESCARGABLE EN ACTUALIZACIONES
│   ├── 3498.txt
│   ├── 3822.txt
│   ├── 3935.txt
│   ├── 4001.txt
│   ├── 4080.txt
│   └── 4081.txt
├── Iconos/                   ← DESCARGABLE EN ACTUALIZACIONES
│   ├── Agregar.png
│   ├── Aptac.png
│   ├── Eliminar.png
│   ├── Mochila.png
│   ├── Nueva-Ventana.png
│   ├── Recursos-Cuenta.png
│   ├── Recursos-Totales.png
│   └── ...
├── Tesseract-OCR/           ← NO SE ACTUALIZA (demasiado grande)
├── README.md
└── GITHUB_SETUP.md
```

## 🔄 Flujo de Actualización

### 📱 En la Computadora del Usuario

```
┌─────────────────────────────────────┐
│   Usuario Presiona "Actualizar"     │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│  App Descarga ZIP desde GitHub      │
│  (Resource-Calculator-main.zip)     │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│  Extrae archivos:                   │
│  • kingdoms/*.txt                   │
│  • Iconos/*.png                     │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│  Reemplaza archivos en:             │
│  C:\Program Files\RSS STORE APTAC\  │
├─ kingdoms\                          │
├─ Iconos\                            │
└─────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│  Recarga la lista de reinos         │
│  ¡Actualizaciones completas!        │
└─────────────────────────────────────┘
```

## 💾 Instalación Inicial del Usuario

1. Descarga el instalador: `RSS_STORE_APTAC_Installer.exe`
2. Lo descomprime en: `C:\Program Files\RSS STORE APTAC\`
3. Archivos iniciales:
   - `RSS STORE APTAC.exe` (la aplicación)
   - `kingdoms/` (con los reinos incluidos)
   - `Iconos/` (con los iconos incluidos)
   - `Tesseract-OCR/` (herramienta OCR)

## 🔄 Actualizaciones Futuras

Cuando el usuario presiona "Actualizar GitHub":

✅ **Descarga automáticamente:**
- Nuevos reinos en `kingdoms/`
- Iconos actualizados en `Iconos/`

❌ **NO descarga:**
- Tesseract-OCR (demasiado grande ~450MB)
- Python/dependencias (instaladas con el .exe)

## 🚀 Flujo de Trabajo para el Desarrollador

### Agregar un nuevo reino

1. Crea/edita archivo:
```bash
kingdoms/5000.txt
```

2. En PowerShell:
```powershell
git add kingdoms/5000.txt
git commit -m "Add kingdom 5000"
git push origin main
```

3. Los usuarios presionan "Actualizar" ✓

### Actualizar un reino existente

1. Edita: `kingdoms/3498.txt`
2. Commit y Push:
```powershell
git add kingdoms/3498.txt
git commit -m "Update kingdom 3498 resources"
git push origin main
```

3. Usuario presiona "Actualizar" ✓

## 📊 Tamaño Estimado de Descargas

| Elemento | Tamaño | Incluido en Actualización |
|----------|--------|--------------------------|
| Archivo ZIP del repo | ~500 KB | ✅ Sí |
| kingdoms/*.txt | ~50 KB | ✅ Sí |
| Iconos/*.png | ~200 KB | ✅ Sí |
| Tesseract-OCR | ~450 MB | ❌ No |
| Python Runtime | ~100 MB | ❌ No |
| **TOTAL DESCARGA** | **~750 KB** | - |

*La descarga de actualizaciones es muy rápida (~5-10 segundos)*

## 🔐 Repositorio Debe Ser Público

```
GitHub > Resource-Calculator > Settings > General
> Visibility: Public
```

Si es privado, los usuarios no podrán descargar actualizaciones.

## ✅ Checklist Final

- [ ] Repositorio creado en GitHub
- [ ] Archivos subidos (git push)
- [ ] Repositorio es **PUBLIC**
- [ ] `app.py` tiene los valores correctos:
  - `GITHUB_OWNER = "Aptac00"`
  - `GITHUB_REPO = "Resource-Calculator"`
- [ ] Carpeta `kingdoms/` tiene archivos `.txt`
- [ ] Carpeta `Iconos/` tiene archivos `.png`
- [ ] Compilé nuevo `.exe` con `build.bat`
- [ ] Creé nuevo instalador con Inno Setup
- [ ] Probé botón "Actualizar GitHub" en la app

---

**Ahora los usuarios pueden mantener sus datos sincronizados** 🎯
