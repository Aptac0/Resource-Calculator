# RSS STORE APTAC

Aplicación de escritorio para extraer recursos de capturas de pantalla de reinos, con extracción de OCR y generación de nicknames.

## Qué incluye
- `app.py`: aplicación principal en Tkinter.
- `kingdoms/`: plantillas de reino (`.txt`) que el usuario puede seleccionar.
- `Iconos/`: iconos PNG usados por la aplicación.

## Guía de uso para usuarios

Esta sección explica cómo utilizar la aplicación paso a paso, cómo tomar capturas (PC y móvil), qué significan los campos y cómo introducir los números correctamente.

### Flujo rápido (resumen)
- Abrir la aplicación `RSS STORE APTAC.exe`.
- Pulsar `Agregar Imágenes` y seleccionar las capturas de pantalla.
- Seleccionar el `Reino` adecuado.
- Rellenar `Número de inicio` y `Número de fin` con el nuemero correcto de tus cuentas.
- Si hace falta, indicar `Números bloqueados` para saltos especificos.
- Elegir adecuadamente `Nivel de ciudad` y `Nivel de depósito` (1–25).
- Pulsar uno de los botones de recursos según la salida que necesites.

### Cómo tomar las capturas (importante)
- Capturas desde PC (recomendado):
	- Abre el juego en ventana o modo que permita capturas claras de la ventana de Recursos.
	- Haz la captura del diálogo que muestra los recursos.
	- Asegúrate que los números y etiquetas estén legibles (fuente no recortada).

  ![Captura desde PC](Ejemplos/Foto-desde-PC.png)

- Capturas desde móvil: (importante)
	- Si usas el móvil, transfiere las imágenes al PC (por USB, Airdrop, Google Drive, Telegram, etc.).
	- Evita fotos anguladas o con zonas borrosas; la app funciona mejor con screenshots limpias (sin sombras ni reflejos).

  ![Captura desde móvil](Ejemplos/Foto-desde-Movil.png)

### Formato de `Número de inicio`, `Número de fin` y `Números bloqueados`
- `Número de inicio` y `Número de fin`: deben ser solo dígitos (p. ej. `1` y `30`).
- `Números bloqueados` admite dos formatos:
	- Rango: `001-010` o `1-10` (se interpretan como todos los números del rango).
	- Lista: `1,3,5,7` o con espacios `1, 3, 5`.
- Ejemplos:
	- `start=1`, `end=10`, `bloqueados=3,5` → cuentas usadas: 1,2,4,6,7,8,9,10 (siempre según cantidad de imágenes seleccionadas).
	- Si el número de imágenes no coincide con las cuentas válidas, la app mostrará un error para corregir entradas.

### Campos `Nivel de ciudad` y `Nivel de depósito`
- Ambos son selectores (1–25). Indica el nivel del Puesto de Venta (puesto) y el Depósito que se aplicará a todas las cuentas en el guardado generado.

  ![Niveles de Puesto de Venta](Ejemplos/Niveles-Puesto-de-Venta.png)
  ![Niveles de Almacen](Ejemplos/Niveles-de-Almacen.png)
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
