import re
from pathlib import Path
import sys

# Permitir pasarle el archivo como argumento, sino usar 3942.txt como default
archivo = sys.argv[1] if len(sys.argv) > 1 else '3942.txt'
p = Path(__file__).parent / 'kingdoms' / archivo
if not p.exists():
    print('File not found:', p)
    print(f'Uso: python parse_kingdom_test.py [archivo.txt]')
    print(f'Ejemplo: python parse_kingdom_test.py 3942.txt')
    raise SystemExit(1)
lines = [ln.rstrip('\n') for ln in p.read_text(encoding='utf-8').splitlines()]
# parse similar to app.parse_kingdom_template
tpl = {'nickname_line': None, 'prefix': None, 'index': 1, 'index_width': 3, 'fields': {}, 'blocked': set(), 'replacements': {}}
collecting_blocked = False
for ln in lines:
    if ln.lower().startswith('nickname:'):
        tpl['nickname_line'] = ln
        parts = ln.split(':',1)
        if len(parts) > 1:
            val = parts[1].strip()
            m = re.search(r'(.*?)(\d+)$', val)
            if m:
                prefix = m.group(1)
                digits = m.group(2)
                tpl['prefix'] = prefix
                tpl['index_width'] = len(digits)
                try:
                    tpl['index'] = int(digits) + 1
                except:
                    tpl['index'] = 1
            else:
                tpl['prefix'] = val
                tpl['index'] = 1
        collecting_blocked = False
    ln_strip = ln.strip()
    ln_low = ln_strip.lower()
    if ln_low.startswith('bloqueados'):
        found = re.findall(r'\d+', ln_strip)
        for num in found:
            try:
                tpl['blocked'].add(int(num))
            except:
                pass
        collecting_blocked = True
        continue
    if collecting_blocked:
        if not ln_strip or ':' in ln_strip or ln_strip.startswith('---'):
            collecting_blocked = False
        else:
            found = re.findall(r'\d+', ln_strip)
            for num in found:
                try:
                    tpl['blocked'].add(int(num))
                except:
                    pass
            continue
    if ':' in ln:
        k,v = ln.split(':',1)
        tpl['fields'][k.strip()] = v.strip()

# post-process: expand ranges
lines_text = '\n'.join(lines)
range_pattern = r'(\d+)\s*-\s*(\d+)'
for match in re.finditer(range_pattern, lines_text):
    try:
        start = int(match.group(1))
        end = int(match.group(2))
        for i in range(start, end + 1):
            tpl['blocked'].add(i)
    except:
        pass

# Parse replacements: "XX reemplaza YY" means number YY should be replaced with XX
replacement_pattern = r'(\d+)\s+reemplaza\s+(\d+)'
for match in re.finditer(replacement_pattern, lines_text, re.IGNORECASE):
    try:
        replacement_num = int(match.group(1))  # XX (el reemplazo)
        original_num = int(match.group(2))      # YY (el original bloqueado)
        tpl['replacements'][original_num] = replacement_num
    except:
        pass

print('Parsed template:')
print(' prefix:', repr(tpl.get('prefix')))
print(' start index:', tpl.get('index'))
print(' index width:', tpl.get('index_width'))
print(' blocked (sorted):', sorted(tpl.get('blocked')))
print(' replacements:', tpl.get('replacements'))
