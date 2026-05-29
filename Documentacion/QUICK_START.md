# ⚡ Resumen Rápido - 5 Pasos

## 1️⃣ Abre PowerShell

```powershell
cd "c:\Users\Aptac\Desktop\Bot Resources"
```

## 2️⃣ Configura Git (solo la primera vez)

```powershell
git config user.name "Tu Nombre"
git config user.email "tu.email@example.com"
```

## 3️⃣ Sube tu código a GitHub

```powershell
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/Aptac00/Resource-Calculator.git
git push -u origin main
```

## 4️⃣ Verifica que `app.py` tenga:

```python
GITHUB_OWNER = "Aptac00"
GITHUB_REPO = "Resource-Calculator"
GITHUB_BRANCH = "main"
```

✅ **Ya está en tu código, listo**

## 5️⃣ Recompila la aplicación

```powershell
.\build.bat
```

## ✅ ¡Listo!

Ahora cuando ejecutes la app compilada y presiones **"Actualizar GitHub"**:

1. ✅ Descarga los últimos `kingdoms/*.txt` desde GitHub
2. ✅ Descarga los últimos `Iconos/*.png` 
3. ✅ Reemplaza los archivos locales
4. ✅ Recarga la lista de reinos

## 📝 Para Agregar Nuevos Reinos

```powershell
# 1. Crea/edita el archivo
# kingdoms/5000.txt

# 2. Sube a GitHub
git add kingdoms/5000.txt
git commit -m "Add kingdom 5000"
git push
```

Los usuarios presionan "Actualizar" ✓

---

**Archivo GitHub**: https://github.com/Aptac00/Resource-Calculator

**📚 Guías completas**:
- `GITHUB_SETUP.md` → Guía detallada
- `ARCHITECTURE.md` → Explicación técnica
