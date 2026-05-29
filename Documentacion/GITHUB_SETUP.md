# 📋 Guía: Subir a GitHub y Configurar Actualizaciones

## 🚀 Paso 1: Preparar el Repositorio Local

### 1.1 Abrir PowerShell en la carpeta del proyecto

```powershell
cd "c:\Users\Aptac\Desktop\Bot Resources"
```

### 1.2 Inicializar Git localmente

```powershell
# Si es la primera vez
git init
git config user.name "Tu Nombre"
git config user.email "tu.email@example.com"
```

### 1.3 Agregar archivos al repositorio

```powershell
git add .
git commit -m "Initial commit - RSS STORE APTAC Application"
```

## 🌐 Paso 2: Crear el Repositorio en GitHub

1. Ve a https://github.com/new
2. **Repository name**: `Resource-Calculator` (o el nombre que prefieras)
3. **Description**: "RSS STORE APTAC - Resource Calculator Application"
4. **Visibility**: Public (si quieres que los usuarios descarguen actualizaciones)
5. **NO** inicialices con README, .gitignore ni license
6. Haz clic en "Create repository"

## 📤 Paso 3: Subir tu Código a GitHub

Después de crear el repositorio en GitHub, en PowerShell ejecuta:

```powershell
git branch -M main
git remote add origin https://github.com/Aptac00/Resource-Calculator.git
git push -u origin main
```

**Nota**: Reemplaza `Aptac00` con tu usuario de GitHub si es diferente.

## ✅ Paso 4: Configurar la Aplicación para Actualizaciones

El código ya está configurado. Verifica que en `app.py` tenga:

```python
GITHUB_OWNER = "Aptac00"           # Tu usuario de GitHub
GITHUB_REPO = "Resource-Calculator" # Nombre del repositorio
GITHUB_BRANCH = "main"
```

## 📁 Cómo Funciona la Actualización

### Usuarios presionan "Actualizar GitHub" y:

1. ✅ Descarga el ZIP del repositorio
2. ✅ Extrae los archivos de `kingdoms/` 
3. ✅ Extrae los archivos de `Iconos/`
4. ✅ Reemplaza los archivos locales
5. ✅ Recarga la lista de reinos

### La app actualiza automáticamente:
- Nuevos archivos `.txt` en `kingdoms/`
- Nuevos iconos en `Iconos/`

## 🔄 Workflows Recomendados

### Agregar un nuevo Reino

1. Crea el archivo: `kingdoms/XXXX.txt` (ej: `kingdoms/5000.txt`)
2. En PowerShell:
   ```powershell
   git add kingdoms/5000.txt
   git commit -m "Add kingdom 5000"
   git push
   ```
3. Los usuarios presionan "Actualizar GitHub" en la app ✓

### Actualizar Recursos de un Reino

1. Edita el archivo: `kingdoms/XXXX.txt`
2. En PowerShell:
   ```powershell
   git add kingdoms/XXXX.txt
   git commit -m "Update kingdom XXXX resources"
   git push
   ```
3. Los usuarios presionan "Actualizar GitHub" ✓

### Agregar Nuevos Iconos

1. Coloca el icono en `Iconos/`
2. En PowerShell:
   ```powershell
   git add Iconos/nuevo-icono.png
   git commit -m "Add new icon"
   git push
   ```

## 🎯 Crear Releases (Opcional)

Si quieres distribuir versiones compiladas del `.exe`:

1. Compila con PyInstaller: `build.bat`
2. En GitHub, ve a "Releases"
3. Haz clic en "Create a new release"
4. Tag version: `v1.0.1`
5. Sube el `.exe` compilado
6. Describe los cambios
7. Publica la release

Los usuarios verán un mensaje sugiriendo actualizar desde releases.

## 🔧 Comandos Útiles de Git

```powershell
# Ver estado
git status

# Ver cambios pendientes
git diff

# Ver historial
git log --oneline

# Deshacer último commit (sin perder cambios)
git reset HEAD~1

# Ver qué hay en el repositorio remoto
git remote -v

# Actualizar tu copia local desde GitHub
git pull origin main
```

## ❌ Solución de Problemas

### Error: "fatal: 'origin' does not appear to be a 'git' repository"

```powershell
git remote add origin https://github.com/Aptac00/Resource-Calculator.git
```

### Error de autenticación al hacer push

GitHub ya no permite contraseñas. Usa:
- **Token Personal**: https://github.com/settings/tokens
- **SSH Keys**: https://github.com/settings/keys

### La app no actualiza

1. Verifica que el repositorio sea **público**
2. Verifica los valores en `app.py`:
   - `GITHUB_OWNER`
   - `GITHUB_REPO`
   - `GITHUB_BRANCH`
3. Asegúrate de que los archivos están en las carpetas correctas: `kingdoms/` e `Iconos/`

---

**¡Listo!** Ahora tus usuarios pueden mantener sus datos actualizados presionando un botón. 🎉
