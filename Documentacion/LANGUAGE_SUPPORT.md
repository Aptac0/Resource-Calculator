# Sistema de Soporte de Idiomas 🌐

## Descripción

Se ha agregado un sistema completo de internacionalización (i18n) a la aplicación **RSS STORE APTAC**. Ahora la interfaz gráfica (GUI) está disponible en 6 idiomas diferentes:

- 🇪🇸 **Español** (por defecto)
- 🇬🇧 **English** (Inglés)
- 🇵🇹 **Português** (Portugués)
- 🇮🇩 **Bahasa Indonesia** (Indonesio)
- 🇻🇳 **Tiếng Việt** (Vietnamita)
- 🇫🇷 **Français** (Francés)

## Características

✅ **Solo GUI traducida**: Los archivos de salida (`.txt`) mantienen el mismo formato en todos los idiomas
✅ **Cambio de idioma en tiempo real**: Selecciona un idioma y la interfaz se actualiza inmediatamente
✅ **Selector fácil de usar**: Dropdown en la barra superior de la aplicación
✅ **Todos los textos incluidos**: Botones, labels, mensajes de error, diálogos

## Cómo Usar

### 1. Al iniciar la aplicación
- Se abre en **Español** por defecto
- En la barra superior encontrarás un selector de idiomas

### 2. Cambiar de idioma
1. Haz clic en el dropdown de idiomas en la parte superior
2. Selecciona el idioma que desees
3. Todos los textos de la interfaz se actualizarán automáticamente

## Archivos Modificados

### `translations.py` (NUEVO)
Contiene toda la lógica de traducciones:
- Diccionarios con todas las traducciones en 6 idiomas
- Clase `Translator` para gestionar idiomas
- Función global `_()` para acceder a traducciones

### `app.py` (MODIFICADO)
Cambios realizados:
- Importación del módulo `translations`
- Reemplazo de todos los textos hardcodeados con llamadas a `_('clave')`
- Agregación de selector de idiomas en la barra superior
- Método `_refresh_all_texts()` para actualizar textos dinámicamente

## Estructura de Traducciones

El archivo `translations.py` contiene un diccionario anidado:

```python
TRANSLATIONS = {
    'es': {  # Español
        'title': 'CALCULADORA DE RECURSOS',
        'add_images': 'Agregar Imágenes',
        # ... más claves ...
    },
    'en': {  # Inglés
        'title': 'RESOURCE CALCULATOR',
        'add_images': 'Add Images',
        # ... más claves ...
    },
    # ... más idiomas ...
}
```

## Agregar Nuevos Idiomas

Para agregar un nuevo idioma (ej: Ruso):

1. Abre `translations.py`
2. Agrega un nuevo diccionario en `TRANSLATIONS`:

```python
'ru': {  # Ruso
    'title': 'КАЛЬКУЛЯТОР РЕСУРСОВ',
    'add_images': 'Добавить изображения',
    # ... traduce todas las claves ...
}
```

3. Actualiza `get_language_names()` en la clase `Translator`:

```python
def get_language_names(self):
    return {
        'es': 'Español',
        'en': 'English',
        'pt': 'Português',
        'id': 'Bahasa Indonesia',
        'vi': 'Tiếng Việt',
        'fr': 'Français',
        'ru': 'Русский'  # ← Agregar esta línea
    }
```

## Notas Importantes

⚠️ **El formato de los archivos .txt NO cambia**
- Los resultados siempre se guardan en el mismo formato
- Los nombres de los campos siempre aparecen en el idioma configurado en el archivo del reino

⚠️ **Interpolación de variables**
Algunas traducciones usan variables:
- `_('save_success', path='/ruta/archivo')` → "Datos guardados en: /ruta/archivo"
- `_('images_mismatch', count=10, valid=5)` → "Error: 10 imágenes seleccionadas pero 5 cuentas válidas encontradas."

⚠️ **Compatibilidad**
- La aplicación funciona con Python 3.6+
- No requiere dependencias adicionales para las traducciones

## Pruebas

Para probar que todo funciona correctamente:

1. Inicia la aplicación
2. Cambia a cada idioma y verifica que la GUI se actualice
3. Procesa algunas imágenes en cada idioma
4. Verifica que los archivos .txt se guarden correctamente

## Soporte

Si encuentras palabras mal traducidas o errores de ortografía en algún idioma:
1. Edita la clave correspondiente en `translations.py`
2. Actualiza la traducción en el diccionario del idioma específico

---

**Versión**: 1.0.0  
**Última actualización**: 2025
