# RSS STORE APTAC - Calculadora de Recursos

**[English](README_en.md) | Español | [Português](README_pt.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Français](README_fr.md)**

---

## 📱 ¿Qué es RSS STORE APTAC?

Aplicación de escritorio para extraer recursos de capturas de pantalla de reinos, con extracción automática por OCR y generación inteligente de nicknames.

## ✨ Características

- ✅ Extracción automática de recursos mediante OCR
- 🎯 Interfaz multiidioma (6 idiomas soportados)
- 🔄 Actualizaciones automáticas desde GitHub
- 📊 Procesamiento por lotes (hasta 100 imágenes)
- 💾 Exportación a archivos TXT/CSV
- 🌍 Respeta tu idioma seleccionado en todos los mensajes

## 🚀 Instalación Rápida

1. Descarga `RSS_STORE_APTAC_Installer.exe` desde [Releases](https://github.com/Aptac0/Resource-Calculator/releases)
2. Ejecuta el instalador
3. ¡Listo! La aplicación se actualizará automáticamente cuando haya nuevas versiones

## 📖 Guía de Uso

### Flujo Rápido

1. **Abrir la aplicación:** Ejecuta `RSS STORE APTAC.exe`
2. **Agregar imágenes:** Click en "Agregar Imágenes" y selecciona las capturas de pantalla
3. **Seleccionar reino:** Elige el reino adecuado del menú desplegable
4. **Configurar números:**
   - `Número de inicio`: primer número (ej: 1)
   - `Número de fin`: último número (ej: 30)
   - `Números bloqueados`: (opcional) números a saltar (ej: 3,5,7)
5. **Configurar niveles:** Selecciona "Nivel de ciudad" y "Nivel de depósito" (1-25)
6. **Procesar:** Click en el botón de tipo de recursos que necesites

### Cómo Tomar Capturas

#### Desde PC (Recomendado)
- Abre el juego en ventana
- Haz captura clara de la ventana de Recursos
- Asegúrate que números y etiquetas sean legibles

![Captura desde PC](../Ejemplos/Foto-desde-PC.png)

#### Desde Móvil
- Transfiere la imagen al PC (USB, Google Drive, etc.)
- Evita fotos anguladas o borrosas
- Asegúrate que la imagen sea nítida

![Captura desde Móvil](../Ejemplos/Foto-desde-Movil.png)

### Formatos de Entrada

#### Números de Inicio y Fin
- Solo dígitos (ej: `1` y `30`)
- Deben ser números válidos

#### Números Bloqueados (Opcional)
Dos formatos disponibles:
- **Rango:** `1-10` (todos los números del 1 al 10)
- **Lista:** `1,3,5,7` (números específicos)
- **Mixto:** `1-5,8,10-15`

**Ejemplos:**
- `inicio=1`, `fin=10`, `bloqueados=3,5` → procesa: 1,2,4,6,7,8,9,10
- La app valida que haya suficientes imágenes para el rango

#### Niveles
- `Nivel de ciudad` (Puesto de Venta): 1-25
- `Nivel de depósito` (Almacén): 1-25

![Niveles de Puesto](../Ejemplos/Niveles-Puesto-de-Venta.png)
![Niveles de Almacén](../Ejemplos/Niveles-de-Almacen.png)

## 🔄 Sistema de Actualización

### Automático
La app verifica nuevas versiones al iniciar. Si encuentra una:
- Te mostrará una notificación
- Puedes descargarla directamente desde la app
- Se instala automáticamente

### Manual
Ejecuta `actualizar.bat` desde la carpeta de instalación

## 🆘 Solución de Problemas

### "No se detectaron los 4 valores"
- Asegúrate que la captura sea legible
- Los números deben estar visibles y claros
- Intenta otra captura más clara

### "Error en la actualización"
- Verifica tu conexión a Internet
- Intenta nuevamente en unos minutos
- Si persiste, reinicia la aplicación

### Las imágenes no se procesan
- Verifica que haya seleccionado un reino
- Comprueba que los números sean válidos
- Asegúrate que tengas suficientes imágenes

## 📞 Soporte

- **GitHub:** https://github.com/Aptac0/Resource-Calculator
- **Issues:** https://github.com/Aptac0/Resource-Calculator/issues
- **Releases:** https://github.com/Aptac0/Resource-Calculator/releases

## 📝 Requisitos Técnicos

- Windows 10 o superior
- Sin necesidad de instalar Python
- Conexión a Internet (para actualizaciones)
- Tesseract OCR (incluido en el instalador)

## 🔐 Privacidad

La aplicación:
- ✅ Funciona completamente offline
- ✅ No envía tus imágenes a ningún servidor
- ✅ No requiere registro ni cuenta
- ✅ Tus datos permanecen en tu computadora

---

**Versión:** 1.0.0  
**Última actualización:** Junio 2026  
**Licencia:** GPL-3.0
