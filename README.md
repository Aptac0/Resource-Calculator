# RSS STORE APTAC - Resource Calculator

**Disponible en múltiples idiomas / Available in multiple languages:**

- 🇪🇸 [Español](docs/README_es.md)
- 🇬🇧 [English](docs/README_en.md)
- 🇵🇹 [Português](docs/README_pt.md)
- 🇻🇳 [Tiếng Việt](docs/README_vi.md)
- 🇮🇩 [Bahasa Indonesia](docs/README_id.md)
- 🇫🇷 [Français](docs/README_fr.md)

---

## 🚀 Quick Start / Inicio Rápido

**Windows users / Usuarios de Windows:**
1. Download `RSS_STORE_APTAC_Installer.exe` from [Releases](../../releases)
2. Run the installer / Ejecuta el instalador
3. Done! App will auto-update / ¡Hecho! La app se actualizará automáticamente

**Características / Features:**
- ✨ OCR-based resource extraction / Extracción de recursos con OCR
- 🎯 Multi-language support (6 languages) / Soporte multiidioma
- 🔄 Automatic updates from GitHub / Actualizaciones automáticas desde GitHub
- 📊 Batch image processing / Procesamiento por lotes
- 💾 CSV/TXT export / Exportación a CSV/TXT
- 🌐 Respects language selection / Respeta el idioma seleccionado

---

## 📖 Documentation / Documentación

**Select your language above / Selecciona tu idioma arriba**

---

## 🔧 For Developers

- **Build:** `build.bat`
- **Dependencies:** See `requirements.txt`
- **Update script:** `update_helper.py`
- **Source:** `app.py`, `translations.py`
- **Install script:** `actualizar.bat`

---

**Repository:** https://github.com/Aptac0/Resource-Calculator

**Latest Release:** [v1.0.0](../../releases/tag/v1.0.0)

  ![Tecnologia Maxima](Ejemplos/Tecnologia-Maxima.png)

### Qué hace cada botón
- `Agregar Imágenes`: abre el selector y añade imágenes a la lista.
- `Limpiar Lista`: vacía la lista de imágenes y datos temporales.
- `Nueva ventana`: abre otra instancia de la aplicación.
- `Recursos Totales`: procesa cada imagen y guarda el total de recursos detectados (Comida, Madera, Piedra, Oro) por cuenta.
- `Recursos de Cuenta`: guarda los recursos netos por cuenta (resta de objetos si aplica según OCR).
- `Recursos de Mochila`: extrae los valores "de objetos" (lo que están en mochila/paquetes).
- `Actualizar GitHub`: descarga `kingdoms/` e `Iconos/` desde el repo configurado y sobrescribe los datos locales. Si usas el `.exe`, te indicará la página de releases para descargar el instalador actualizado.

  ![Botones de la app](Ejemplos/Botones-App.png)

### Carpeta `GUARDADOS` y resultados
- Al procesar las imágenes, la app guarda automáticamente un archivo `.txt` en la carpeta a seleccion con el nombre `REINO_results_YYYYMMDD_HHMMSS.txt`.
- Cada entrada incluye: `Nickname`, `Nivel de ciudad`, `Nivel de depósito`, `Comida`, `Madera`, `Piedra`, `Oro` y un separador `---`.
- Puedes revisar estos archivos y copiarlos a tu herramienta de subida o registro.

### Ejemplo de flujo recomendado
1. Abrir juego y mostrar ventana de recursos en cada cuenta.
2. Tomar captura clara (PC screenshot o móvil -> transferir al PC).
3. En la app: `Agregar Imágenes` → seleccionar capturas en el orden de cuentas.
4. Seleccionar `Reino` correcto (o cargar plantilla); si prefieres, rellenar `Número de inicio`/`fin` y `Números bloqueados`.
5. Ajustar `Nivel de ciudad` y `Nivel de depósito` (1–25).
6. Pulsar `Recursos Totales`.
7. Revisar `GUARDADOS/` para el archivo resultante.

## Solución de problemas comunes
- Si la app no detecta 4 valores por imagen: revisa la calidad de la imagen (recorta y vuelve a intentar).
- Si ves números con sufijos `K/M/B` no reconocidos correctamente, prueba a aumentar el tamaño de la captura o usar la versión del juego en idioma esperado.
- Si `Actualizar GitHub` falla: comprueba que `GITHUB_OWNER` y `GITHUB_REPO` están bien configurados en `app.py` y que hay conexión a Internet.

## Uso del botón de actualización
La aplicación ahora tiene un botón `Actualizar GitHub`.

- Si el usuario ejecuta la aplicación desde el código fuente, el botón descarga y actualiza las carpetas `kingdoms/` e `Iconos/` desde el repositorio.
- Si el usuario ejecuta el `.exe` compilado, el botón también actualizará los datos locales y mostrará la URL de la página de releases para descargar el nuevo instalador.

## Recomendación
Cada vez que agregues un nuevo reino a `kingdoms/` en GitHub, crea un release nuevo con el ejecutable actualizado y avisa a los usuarios que presionen `Actualizar GitHub`.
