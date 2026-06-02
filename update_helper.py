#!/usr/bin/env python3
"""
Script helper para descargar e instalar las últimas actualizaciones
Se ejecuta en un proceso separado para evitar que el .exe esté bloqueado
"""

import urllib.request
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
import time

GITHUB_OWNER = "Aptac0"
GITHUB_REPO = "Resource-Calculator"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/releases/latest"

def get_latest_version():
    """Obtiene la versión más reciente de GitHub"""
    try:
        req = urllib.request.Request(GITHUB_API_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read())
            return data.get('tag_name', None)
    except Exception as e:
        print(f"Error obteniendo versión: {e}")
        return None

def download_exe(release_data, output_path):
    """Descarga el .exe de la release"""
    try:
        assets = release_data.get('assets', [])
        exe_asset = next((a for a in assets if a['name'].endswith('.exe')), None)
        
        if not exe_asset:
            print("No se encontró .exe en la release")
            return False
        
        url = exe_asset['browser_download_url']
        print(f"Descargando desde: {url}")
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=60) as response:
            with open(output_path, 'wb') as f:
                f.write(response.read())
        
        print(f"Descargado a: {output_path}")
        return True
    except Exception as e:
        print(f"Error descargando: {e}")
        return False

def install_dependencies():
    """Instala las dependencias de requirements.txt"""
    try:
        requirements_file = Path(__file__).parent / 'requirements.txt'
        if requirements_file.exists():
            print("Instalando dependencias...")
            subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', str(requirements_file)], 
                          check=True, capture_output=True, timeout=300)
            print("Dependencias instaladas")
            return True
    except Exception as e:
        print(f"Error instalando dependencias: {e}")
        return False

def replace_exe(old_exe, new_exe):
    """Reemplaza el ejecutable viejo con el nuevo"""
    try:
        # Esperar a que el proceso anterior se cierre
        time.sleep(2)
        
        if old_exe.exists():
            backup = old_exe.with_suffix('.exe.bak')
            shutil.move(str(old_exe), str(backup))
            print(f"Ejecutable anterior respaldado: {backup}")
        
        shutil.move(str(new_exe), str(old_exe))
        print(f"Ejecutable actualizado: {old_exe}")
        return True
    except Exception as e:
        print(f"Error reemplazando ejecutable: {e}")
        return False

def main():
    print("=== Update Helper ===")
    
    if len(sys.argv) < 2:
        print("Uso: update_helper.py <current_version> [exe_path]")
        return
    
    current_version = sys.argv[1]
    exe_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(sys.executable)
    
    print(f"Versión actual: {current_version}")
    print(f"Ruta .exe: {exe_path}")
    
    # Obtener versión más reciente
    latest_version = get_latest_version()
    if not latest_version:
        print("No se pudo obtener la versión más reciente")
        return
    
    print(f"Versión más reciente: {latest_version}")
    
    if latest_version <= current_version:
        print("Ya está en la última versión")
        return
    
    # Obtener datos de la release
    try:
        req = urllib.request.Request(GITHUB_API_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            release_data = json.loads(response.read())
    except Exception as e:
        print(f"Error obteniendo datos de release: {e}")
        return
    
    # Descargar nuevo .exe
    temp_exe = exe_path.parent / f"{exe_path.stem}_new{exe_path.suffix}"
    if not download_exe(release_data, temp_exe):
        return
    
    # Instalar dependencias
    install_dependencies()
    
    # Reemplazar ejecutable
    if replace_exe(exe_path, temp_exe):
        print("\n✓ Actualización completada exitosamente")
        print(f"Nueva versión: {latest_version}")

if __name__ == '__main__':
    main()
