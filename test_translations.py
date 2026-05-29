#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para validar el sistema de traducciones
Verifica que todos los idiomas tengan las mismas claves y que no haya errores
"""

import sys
from pathlib import Path

# Agregar el directorio del script al path
sys.path.insert(0, str(Path(__file__).parent))

from translations import TRANSLATIONS, get_translator, set_language, _

def test_translations():
    """Prueba el sistema de traducciones"""
    
    print("=" * 70)
    print("PRUEBA DEL SISTEMA DE TRADUCCIONES - RSS STORE APTAC")
    print("=" * 70)
    
    # Test 1: Verificar que todos los idiomas existen
    print("\n[TEST 1] Verificando idiomas disponibles...")
    languages = list(TRANSLATIONS.keys())
    expected_languages = ['es', 'en', 'pt', 'id', 'vi', 'fr']
    
    if sorted(languages) == sorted(expected_languages):
        print(f"✓ Se encontraron {len(languages)} idiomas: {', '.join(languages)}")
    else:
        print(f"✗ Error: Idiomas esperados {expected_languages}, encontrados {languages}")
        return False
    
    # Test 2: Obtener todas las claves del idioma español
    print("\n[TEST 2] Obteniendo claves de traducción...")
    spanish_keys = set(TRANSLATIONS['es'].keys())
    print(f"✓ Total de claves traducibles: {len(spanish_keys)}")
    
    # Test 3: Verificar que todos los idiomas tienen las mismas claves
    print("\n[TEST 3] Validando consistencia de claves en todos los idiomas...")
    all_consistent = True
    for lang_code, translations_dict in TRANSLATIONS.items():
        lang_keys = set(translations_dict.keys())
        if lang_keys != spanish_keys:
            print(f"✗ {lang_code}: Faltan claves: {spanish_keys - lang_keys}")
            print(f"✗ {lang_code}: Claves extra: {lang_keys - spanish_keys}")
            all_consistent = False
        else:
            print(f"✓ {lang_code}: {len(lang_keys)} claves OK")
    
    if not all_consistent:
        return False
    
    # Test 4: Probar la función de traducción
    print("\n[TEST 4] Probando función de traducción...")
    test_keys = ['title', 'add_images', 'close', 'language']
    
    for key in test_keys:
        result = _(key)
        if result and result != f"[{key}]":
            print(f"✓ '{key}' → '{result}'")
        else:
            print(f"✗ Error traduciendo '{key}'")
            return False
    
    # Test 5: Probar cambio de idioma
    print("\n[TEST 5] Probando cambio dinámico de idioma...")
    
    set_language('es')
    es_title = _('title')
    
    set_language('en')
    en_title = _('title')
    
    set_language('fr')
    fr_title = _('title')
    
    set_language('es')  # Volver a español
    
    if es_title != en_title and en_title != fr_title:
        print(f"✓ ES: {es_title}")
        print(f"✓ EN: {en_title}")
        print(f"✓ FR: {fr_title}")
    else:
        print("✗ Error: Los idiomas no se están cambiando correctamente")
        return False
    
    # Test 6: Probar interpolación de variables
    print("\n[TEST 6] Probando interpolación de variables en traducciones...")
    
    # Este es un ejemplo con format
    try:
        # Buscar una clave que use formato
        result = _('save_success', path='/ruta/archivo.txt')
        if '/ruta/archivo.txt' in result:
            print(f"✓ Interpolación exitosa: {result}")
        else:
            print(f"✗ Interpolación no funcionó: {result}")
            return False
    except Exception as e:
        print(f"✗ Error en interpolación: {e}")
        return False
    
    # Test 7: Probar método get_language_names
    print("\n[TEST 7] Verificando nombres de idiomas...")
    translator = get_translator()
    lang_names = translator.get_language_names()
    
    if len(lang_names) == len(languages):
        print(f"✓ Hay {len(lang_names)} nombres de idiomas")
        for code, name in lang_names.items():
            print(f"  • {code}: {name}")
    else:
        print(f"✗ Error: Número de nombres ({len(lang_names)}) no coincide con idiomas ({len(languages)})")
        return False
    
    # Test 8: Probar método get_available_languages
    print("\n[TEST 8] Probando método get_available_languages...")
    available = translator.get_available_languages()
    print(f"✓ Idiomas disponibles: {available}")
    
    # Resumen final
    print("\n" + "=" * 70)
    print("✓ TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
    print("=" * 70)
    
    print("\nResumen:")
    print(f"  • Idiomas: {len(languages)}")
    print(f"  • Claves de traducción: {len(spanish_keys)}")
    print(f"  • Estado: ✓ Funcional y listo para usar")
    
    return True

if __name__ == '__main__':
    try:
        success = test_translations()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n✗ ERROR CRÍTICO: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
