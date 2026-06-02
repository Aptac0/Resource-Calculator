#!/usr/bin/env python3
"""
Script de prueba para diagnosticar qué está fallando en los botones
"""
import sys
from pathlib import Path

# Importar la app
sys.path.insert(0, str(Path(__file__).parent))

from app import ResourceExtractorApp
import tkinter as tk

print("=" * 60)
print("SCRIPT DE PRUEBA - DIAGNÓSTICO DE BOTONES")
print("=" * 60)

root = tk.Tk()
app = ResourceExtractorApp(root)

print("\n✓ Aplicación iniciada correctamente")
print("\nAhora:")
print("  1. Carga una o dos IMÁGENES (.png, .jpg)")
print("  2. Asegúrate de tener un REINO seleccionado")
print("  3. Completa NÚMERO DE INICIO y NÚMERO DE FIN (ej: 1 y 2)")
print("  4. Clickea 'Recursos Totales'")
print("  5. Mira QUÉ DICE LA TERMINAL - copia TODO lo que aparezca")
print("=" * 60)

try:
    root.mainloop()
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
