#!/usr/bin/env powershell
<#
.SYNOPSIS
Crea una Release en GitHub con el ejecutable compilado

.DESCRIPTION
Requiere un token personal de GitHub con permisos 'repo'

.PARAMETER Token
Token personal de GitHub (PAT)

.PARAMETER Version
Versión a liberar (ej: v1.0.0)

.EXAMPLE
.\create_release.ps1 -Token "ghp_xxxxxxxxxxxx" -Version "v1.0.0"
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$Token,
    
    [Parameter(Mandatory=$false)]
    [string]$Version = "v1.0.0"
)

$ErrorActionPreference = "Stop"

$Owner = "Aptac0"
$Repo = "Resource-Calculator"
$ExePath = "dist\RSS STORE APTAC.exe"
$ApiUrl = "https://api.github.com/repos/$Owner/$Repo/releases"

Write-Host "=== Creando Release en GitHub ===" -ForegroundColor Cyan
Write-Host "Propietario: $Owner"
Write-Host "Repositorio: $Repo"
Write-Host "Versión: $Version"
Write-Host "Ejecutable: $ExePath"
Write-Host ""

# Verificar que el archivo existe
if (-not (Test-Path $ExePath)) {
    Write-Host "ERROR: No se encontró el archivo: $ExePath" -ForegroundColor Red
    exit 1
}

$FileSize = (Get-Item $ExePath).Length / 1MB
Write-Host "Tamaño del archivo: $($FileSize.ToString('F2')) MB"

# Crear headers con autenticación
$Headers = @{
    "Authorization" = "token $Token"
    "Accept" = "application/vnd.github.v3+json"
    "Content-Type" = "application/json"
}

# Datos de la Release
$ReleaseBody = @{
    tag_name = $Version
    target_commitish = "main"
    name = "RSS STORE APTAC $Version"
    body = @"
## Cambios en esta versión

### ✨ Nuevas características
- Sistema de auto-actualización con verificación de versiones en GitHub
- Descarga e instalación automática de nuevas versiones
- Auto-instalación de dependencias
- Interfaz completamente traducida a múltiples idiomas

### 🐛 Correcciones
- Traducción de todos los mensajes de error
- Botones funcionan sin mostrar ventana de comandos

### 📦 Instalación
1. Descarga `RSS_STORE_APTAC_Installer.exe`
2. Ejecuta y sigue el instalador
3. ¡Listo! La app se actualizará automáticamente

### 🔄 Actualización automática
La app verifica nuevas versiones automáticamente. Cuando encuentre una, te mostrará una notificación para descargarla.

---
Para reportar bugs: https://github.com/$Owner/$Repo/issues
"@
    draft = $false
    prerelease = $false
} | ConvertTo-Json

Write-Host "Creando release..."

try {
    $ReleaseResponse = Invoke-RestMethod -Uri $ApiUrl -Method Post -Headers $Headers -Body $ReleaseBody
    $UploadUrl = $ReleaseResponse.upload_url -replace '\{.*\}'
    $ReleaseId = $ReleaseResponse.id
    
    Write-Host "✓ Release creada: $($ReleaseResponse.html_url)" -ForegroundColor Green
    Write-Host ""
    Write-Host "Subiendo ejecutable..."
    
    # Subir el archivo
    $FileContent = [System.IO.File]::ReadAllBytes($ExePath)
    $FileName = Split-Path $ExePath -Leaf
    
    $UploadHeaders = @{
        "Authorization" = "token $Token"
        "Content-Type" = "application/octet-stream"
    }
    
    $UploadResponse = Invoke-RestMethod -Uri "$UploadUrl`?name=$FileName" `
        -Method Post -Headers $UploadHeaders -Body $FileContent
    
    Write-Host "✓ Ejecutable subido: $($UploadResponse.browser_download_url)" -ForegroundColor Green
    Write-Host ""
    Write-Host "=== Release completada ===" -ForegroundColor Green
    Write-Host "Versión: $Version"
    Write-Host "URL: $($ReleaseResponse.html_url)"
    
} catch {
    Write-Host "ERROR: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "Posibles causas:"
    Write-Host "- Token inválido o expirado"
    Write-Host "- Permisos insuficientes"
    Write-Host "- La versión ya existe"
    exit 1
}
