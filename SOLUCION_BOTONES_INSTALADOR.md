# Solución: Botones no funcionaban después de instalar

## Problema Identificado
Cuando la aplicación se ejecutaba desde el workspace funcionaba correctamente, pero después de instalar con el archivo .exe, los botones no respondían.

## Causa Raíz
El código estaba usando `Path(__file__).parent` directamente en dos funciones, lo que NO funciona correctamente cuando la aplicación está empaquetada con **PyInstaller**:

1. **`_on_reino_selected()` (línea 905)**: Cuando el usuario cambiaba de reino, no encontraba los archivos porque buscaba en la ruta incorrecta.
2. **`open_new_window()` (línea 959)**: Al abrir una nueva ventana, no podía encontrar el script nuevamente.

## Solución Implementada

### Cambio 1: `_on_reino_selected()` 
```python
# ANTES (incorrecto):
base = Path(__file__).parent
kpath = base / 'kingdoms' / sel

# DESPUÉS (correcto):
kdir = self._resolve_path('kingdoms')
kpath = kdir / sel
```

### Cambio 2: `open_new_window()`
```python
# ANTES (incorrecto):
base = Path(__file__).parent
python = sys.executable
script = str(Path(__file__).resolve())
subprocess.Popen([python, script], cwd=str(base))

# DESPUÉS (correcto):
install_base = self._get_install_base()
python = sys.executable
if getattr(sys, 'frozen', False):  # Si está empaquetado
    script = str(sys.executable)
else:  # Si está ejecutando desde Python
    script = str(Path(__file__).resolve())
subprocess.Popen([python, script], cwd=str(install_base))
```

## Por qué funcionaba `_populate_reinos()`
Esa función YA estaba usando `self._resolve_path('kingdoms')`, por eso funcionaba correctamente y cargaba los reinos al inicio.

## Por qué otros botones funcionaban
Los botones "Agregar Imágenes", "Limpiar Lista", etc., no dependen de archivos de datos, por eso funcionaban. Los problemas solo aparecían cuando:
- Cambias de reino (selector de reinos)
- Intentabas abrir una nueva ventana

## Método `_resolve_path()` - La solución correcta
Este método ya estaba implementado en el código y maneja automáticamente:
- Búsqueda en `sys._MEIPASS` (carpeta de PyInstaller)
- Búsqueda en el directorio del ejecutable instalado
- Búsqueda en el directorio del script (cuando corres en desarrollo)

```python
def _resolve_path(self, *parts):
    install_base = self._get_install_base()
    candidate = install_base.joinpath(*parts)
    if candidate.exists():
        return candidate
    data_base = self._get_data_base()
    return data_base.joinpath(*parts)
```

## Archivos que se generaron
- ✅ **dist/RSS STORE APTAC.exe** - Ejecutable actualizado
- ✅ **Output/RSS_STORE_APTAC_Installer.exe** - Instalador actualizado

## Próximas pruebas recomendadas
1. Desinstala cualquier versión anterior de la aplicación
2. Ejecuta el nuevo instalador desde `Output/RSS_STORE_APTAC_Installer.exe`
3. Verifica que:
   - Los botones "Recursos Totales", "Recursos de Cuenta", "Mochila" funcionan
   - Puedes cambiar de reino sin problemas
   - El botón "Nueva Ventana" abre instancias adicionales
   - Los iconos se muestran correctamente

## Recomendación para el futuro
**NUNCA uses `Path(__file__)` directamente cuando trabajes con PyInstaller.**

Siempre usa los métodos ya definidos:
- `self._resolve_path('carpeta/archivo')` para acceder a datos
- `self._get_install_base()` para la carpeta de instalación
- `self._get_data_base()` para la carpeta de datos empaquetados
