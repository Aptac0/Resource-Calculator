# RSS STORE APTAC - Actualizaciones

## 🚀 Sistemas de Actualización Disponibles

### 1️⃣ **Automático (Recomendado para usuarios finales)**

Al iniciar la aplicación, se verifica automáticamente si hay una nueva versión disponible en GitHub:

- ✅ Si hay nueva versión → aparecerá una notificación
- ✅ Puedes descargarla directamente desde la app
- ✅ Se instala automáticamente sin necesidad de hacer nada

**Ventajas:**
- Sin necesidad de instalar nada extra
- Sin necesidad de abrir navegadores o descargar archivos manualmente
- Las dependencias se instalan automáticamente

### 2️⃣ **Manual desde dentro de la App**

Puedes hacer clic en el botón **"Actualizar"** en la pantalla principal:

1. Se verifica la última versión disponible
2. Aparece un diálogo preguntando si deseas actualizar
3. Se descarga y se instala automáticamente

**Nota:** Este sistema es igual al automático pero iniciado manualmente.

### 3️⃣ **Manual desde línea de comandos (Para usuarios con Python)**

Si tienes Python 3.8+ instalado:

```bash
# Windows
actualizar.bat

# O directamente con Python
python update_helper.py 1.0.0 "C:\Program Files\RSS STORE APTAC\RSS STORE APTAC.exe"
```

**Requisitos:**
- Python 3.8 o superior
- Variable `PATH` configurada para Python
- Archivo `requirements.txt` en el mismo directorio

### 4️⃣ **Manual desde GitHub (Para desarrolladores)**

1. Descarga el repositorio: https://github.com/Aptac0/Resource-Calculator
2. Extrae el ZIP
3. Ejecuta `build.bat` para compilar el nuevo `.exe`
4. Copia el `.exe` nuevo a tu carpeta de instalación

---

## 📋 ¿Qué se actualiza?

### ✅ Se actualizan automáticamente:
- Archivos de reinos (`kingdoms/`)
- Iconos de botones (`Iconos/`)
- Archivo de traducciones (`translations.py`)
- Datos dinámicos

### ❌ Requieren descarga del nuevo `.exe`:
- Código principal (`app.py`)
- Scripts helper (`update_helper.py`)
- Compilación del programa

---

## 🔧 Instalación de Dependencias

Las dependencias se instalan automáticamente cuando:
1. Se descarga una actualización automáticamente
2. Se ejecuta el `actualizar.bat`
3. Se ejecuta `update_helper.py` manualmente

**Dependencias principales:**
- `Pillow` >= 9.0 (procesamiento de imágenes)
- `pytesseract` >= 0.3.10 (OCR)
- `PyInstaller` >= 6.1.0 (solo para compilación)

---

## 🐛 Solución de Problemas

### "Python no está instalado"
**Solución:** Descarga e instala Python desde https://www.python.org
- Marca la opción "Add Python to PATH" durante la instalación
- Reinicia tu computadora

### "Error descargando actualización"
**Posibles causas:**
- Sin conexión a Internet
- GitHub está caído
- Firewall bloqueando conexiones

**Solución:** Intenta de nuevo en unos minutos

### "No se encuentra update_helper.py"
**Solución:** Asegúrate de descargar el repositorio completo desde GitHub, no solo el `.exe`

---

## 📞 Contacto y Soporte

Si tienes problemas con las actualizaciones:
1. Verifica que tienes conexión a Internet
2. Intenta nuevamente en unos minutos
3. Si persiste el error, crea un issue en GitHub: https://github.com/Aptac0/Resource-Calculator/issues

---

## 📊 Versiones

- **v1.0.0** - Versión inicial con sistema de actualizaciones
  - Sistema automático de verificación de versiones
  - Descarga e instalación automática
  - Auto-instalación de dependencias
  - Interfaz multiidioma

Para ver cambios entre versiones, visita: https://github.com/Aptac0/Resource-Calculator/releases
