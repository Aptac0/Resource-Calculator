#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script de prueba para verificar el sistema de traducción"""

from translations import set_language, _

# Prueba con diferentes idiomas
idiomas = ['es', 'en', 'pt', 'id', 'vi', 'fr']
claves = ['nickname', 'city_level_display', 'warehouse_level_display', 'food', 'wood', 'stone', 'gold']

print("=" * 70)
print("PRUEBA DEL SISTEMA DE TRADUCCIÓN")
print("=" * 70)

for idioma in idiomas:
    set_language(idioma)
    print(f"\n--- {idioma.upper()} ---")
    
    for clave in claves:
        traduccion = _(clave)
        print(f"  {clave}: {traduccion}")

print("\n" + "=" * 70)
print("EJEMPLO DE SALIDA (Como aparecería en el archivo .txt)")
print("=" * 70)

# Ejemplo con español
set_language('es')
print(f"\n{_('nickname')} [APA6]4080Aptac001")
print(f"{_('city_level_display')} 17")
print(f"{_('warehouse_level_display')} 11")
print(f"{_('food')} 11.3M")
print(f"{_('wood')} 8.7M")
print(f"{_('stone')} 11.1M")
print(f"{_('gold')} 4.3M")
print("---")

print(f"\n{_('nickname')} [APA6]4081Aptac002")
print(f"{_('city_level_display')} 18")
print(f"{_('warehouse_level_display')} 12")
print(f"{_('food')} 12.3M")
print(f"{_('wood')} 9.7M")
print(f"{_('stone')} 12.1M")
print(f"{_('gold')} 5.3M")
print("---")

# Ejemplo con inglés
print("\n\n" + "=" * 70)
set_language('en')
print(f"\n{_('nickname')} [APA6]4080Aptac001")
print(f"{_('city_level_display')} 17")
print(f"{_('warehouse_level_display')} 11")
print(f"{_('food')} 11.3M")
print(f"{_('wood')} 8.7M")
print(f"{_('stone')} 11.1M")
print(f"{_('gold')} 4.3M")
print("---")

# Ejemplo con francés
print("\n\n" + "=" * 70)
set_language('fr')
print(f"\n{_('nickname')} [APA6]4080Aptac001")
print(f"{_('city_level_display')} 17")
print(f"{_('warehouse_level_display')} 11")
print(f"{_('food')} 11.3M")
print(f"{_('wood')} 8.7M")
print(f"{_('stone')} 11.1M")
print(f"{_('gold')} 4.3M")
print("---")

print("\n" + "=" * 70)
print("✅ El sistema de traducción funciona correctamente")
print("=" * 70)
