import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageOps, ImageFilter, ImageTk, ImageDraw, ImageFont
import pytesseract
import os
import threading
import time
from pathlib import Path
import re
import math
from datetime import datetime
import subprocess
import sys
import concurrent.futures
import urllib.request
import urllib.parse
import zipfile
import tempfile
import webbrowser
from translations import get_translator, set_language, _

# Si Tesseract no está en la ruta del sistema, pon aquí la ruta correcta:
# TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TESSERACT_CMD = None
if TESSERACT_CMD:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

GITHUB_OWNER = "Aptac0"
GITHUB_REPO = "Resource-Calculator"
GITHUB_BRANCH = "main"
GITHUB_REPO_ZIP_URL = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/archive/refs/heads/{GITHUB_BRANCH}.zip"
GITHUB_RELEASES_URL = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/releases/latest"
GITHUB_EXE_NAME = "RSS STORE APTAC.exe"
APP_NAME = "RSS STORE APTAC"
APP_VERSION = "1.0.0"

class ResourceExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title(_('title'))
        self.root.state('zoomed')  # Pantalla completa en Windows
        self.root.configure(bg="#1a3a4a")
        
        self.selected_images = []
        self.extracted_data = []  # lista plana con valores y '-' después de cada imagen procesada
        self.failed_images = []
        self.icons = {}  # Almacenar referencias de iconos
        # Variables para niveles (1..25)
        self.city_level_var = tk.StringVar(value='1')
        self.warehouse_level_var = tk.StringVar(value='1')
        # Variable para idioma
        self.language_var = tk.StringVar(value='es')
        # Diccionario para guardar referencias de labels traducibles
        self.labels_dict = {}
        # Cargar icono de la ventana
        self._load_window_icon()
        
        # Cargar iconos de botones
        self._load_icons()
        
        # Estilo
        self.setup_styles()
        self.create_widgets()
        
    def _get_data_base(self):
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            return Path(sys._MEIPASS)
        return Path(__file__).parent

    def _get_install_base(self):
        if getattr(sys, 'frozen', False):
            return Path(sys.executable).parent
        return Path(__file__).parent

    def _resolve_path(self, *parts):
        install_base = self._get_install_base()
        candidate = install_base.joinpath(*parts)
        if candidate.exists():
            return candidate
        data_base = self._get_data_base()
        return data_base.joinpath(*parts)

    def _load_window_icon(self):
        """Cargar Aptac.png como icono de ventana"""
        icon_path = self._resolve_path('Iconos', 'Aptac.png')
        if icon_path.exists():
            try:
                img = Image.open(str(icon_path))
                icon = ImageTk.PhotoImage(img)
                self.root.iconphoto(False, icon)
                self.window_icon = icon  # Mantener referencia
            except Exception as e:
                print(f"Error cargando Aptac.png: {e}")
        else:
            print(f"No encontrado: {icon_path}")

    def _load_icons(self):
        """Cargar iconos desde la carpeta Iconos"""
        icons_dir = self._resolve_path('Iconos')
        icon_files = {
            'agregar': 'Agregar.png',
            'eliminar': 'Eliminar.png',
            'ventana': 'Nueva-Ventana.png',
            'totales': 'Recursos-Totales.png',
            'cuenta': 'Recursos-Cuenta.png',
            'mochila': 'Mochila.png'
        }
        for key, filename in icon_files.items():
            icon_path = icons_dir / filename
            if icon_path.exists():
                try:
                    img = Image.open(str(icon_path))
                    img.thumbnail((24, 24), Image.Resampling.LANCZOS)
                    self.icons[key] = ImageTk.PhotoImage(img)
                except Exception as e:
                    print(f"Error cargando icono {filename}: {e}")
            else:
                print(f"No encontrado: {icon_path}")

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', font=('Arial', 10, 'bold'), padding=6, foreground='white')
        style.configure('Primary.TButton', background='#5cb85c', foreground='white')
        style.configure('Secondary.TButton', background='#0275d8', foreground='white')
        style.configure('Accent.TButton', background='#6f42c1', foreground='white')
        style.configure('Danger.TButton', background='#d9534f', foreground='white')
        style.configure('Default.TButton', background='#4da6c7', foreground='white')
        style.configure('Title.TLabel', font=('Arial', 14, 'bold'), background="#1a3a4a", foreground="#00d9ff")
        style.configure('Section.TLabel', font=('Arial', 12, 'bold'), background="#1f5670", foreground="#00ff41")
        style.configure('Label.TLabel', font=('Arial', 10, 'bold'), background="#1f5670", foreground="#00d9ff")
        style.configure('Help.TLabel', font=('Arial', 9, 'bold'), background="#1a3a4a", foreground="#ffffff")
        style.configure('TEntry', fieldbackground='#ffffff', foreground='#000000', background='#ffffff', font=('Arial', 10, 'bold'))
        style.configure('TCombobox', fieldbackground='#ffffff', foreground='#000000', background='#ffffff', font=('Arial', 10, 'bold'))
        
    def create_widgets(self):
        # Barra de idiomas en la parte superior
        lang_frame = tk.Frame(self.root, bg="#0d2633")
        lang_frame.pack(fill=tk.X, padx=0, pady=0)
        
        ttk.Label(lang_frame, text=_('language'), style='Help.TLabel').pack(side=tk.LEFT, padx=12, pady=8)
        
        translator = get_translator()
        lang_names = translator.get_language_names()
        lang_codes = list(lang_names.keys())
        lang_display = [lang_names[code] for code in lang_codes]
        
        lang_combo = ttk.Combobox(lang_frame, values=lang_display, state='readonly', width=15, style='TCombobox')
        lang_combo.set(lang_names['es'])
        lang_combo.pack(side=tk.LEFT, padx=0, pady=8)
        
        def on_language_change(event):
            selected_idx = lang_combo.current()
            if selected_idx >= 0:
                new_lang = lang_codes[selected_idx]
                self.language_var.set(new_lang)
                set_language(new_lang)
                self._refresh_all_texts()
        
        lang_combo.bind('<<ComboboxSelected>>', on_language_change)
        
        title = ttk.Label(self.root, text=_('title'), style='Title.TLabel')
        title.pack(pady=14)

        main_frame = tk.Frame(self.root, bg="#1a3a4a")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=16, pady=8)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=0)

        left_panel = tk.Frame(main_frame, bg="#15374a")
        left_panel.grid(row=0, column=0, sticky='nsew', padx=(0,8), pady=4)
        right_panel = tk.Frame(main_frame, bg="#15374a")
        right_panel.grid(row=0, column=1, sticky='nsew', padx=(8,0), pady=4)
        left_panel.columnconfigure(0, weight=1)
        right_panel.columnconfigure(0, weight=1)

        selector_frame = tk.Frame(left_panel, bg="#1f5670", bd=0, relief=tk.RIDGE)
        selector_frame.pack(fill=tk.BOTH, expand=True, pady=(0,8))

        self.selector_label = ttk.Label(selector_frame, text=_('selector_images'), style='Section.TLabel')
        self.selector_label.pack(pady=10)
        self.labels_dict['selector_label'] = ('selector_images', self.selector_label)

        listbox_frame = tk.Frame(selector_frame, bg="#1f5670")
        listbox_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0,10))
        scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.image_listbox = tk.Listbox(listbox_frame, height=12, bg="#173d52", fg="#e0f7ff",
                                       selectmode=tk.BROWSE, bd=0, activestyle='none', relief=tk.FLAT,
                                       yscrollcommand=scrollbar.set)
        self.image_listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.image_listbox.yview)

        button_frame = tk.Frame(selector_frame, bg="#1f5670")
        button_frame.pack(fill=tk.X, padx=12, pady=(0,12))
        self.add_images_btn = self._add_side_button(button_frame, _('add_images'), self.add_images, "#4da6c7", 'agregar')
        self.add_images_btn.pack(side=tk.LEFT, padx=3, pady=4, expand=True, fill=tk.X)
        self.labels_dict['add_images_btn'] = ('add_images', self.add_images_btn)
        
        self.clear_list_btn = self._add_side_button(button_frame, _('clear_list'), self.clear_images, "#d9534f", 'eliminar')
        self.clear_list_btn.pack(side=tk.LEFT, padx=3, pady=4, expand=True, fill=tk.X)
        self.labels_dict['clear_list_btn'] = ('clear_list', self.clear_list_btn)
        
        self.new_window_btn = self._add_side_button(button_frame, _('new_window'), self.open_new_window, "#28a745", 'ventana')
        self.new_window_btn.pack(side=tk.LEFT, padx=3, pady=4, expand=True, fill=tk.X)
        self.labels_dict['new_window_btn'] = ('new_window', self.new_window_btn)

        options_frame = tk.Frame(right_panel, bg="#1f5670", bd=0, relief=tk.RIDGE)
        options_frame.pack(fill=tk.BOTH, expand=True, pady=(0,8))

        self.options_label = ttk.Label(options_frame, text=_('config_kingdom'), style='Section.TLabel')
        self.options_label.pack(pady=8)
        self.labels_dict['options_label'] = ('config_kingdom', self.options_label)

        reino_frame = tk.Frame(options_frame, bg="#1f5670")
        reino_frame.pack(fill=tk.X, padx=12, pady=(0,8))
        self.reino_label = ttk.Label(reino_frame, text=_('kingdom'), style='Label.TLabel')
        self.reino_label.grid(row=0, column=0, sticky='w')
        self.labels_dict['reino_label'] = ('kingdom', self.reino_label)
        self.reino_combobox = ttk.Combobox(reino_frame, values=[], state='readonly', width=22, style='TCombobox')
        self.reino_combobox.grid(row=0, column=1, padx=8, pady=3, sticky='ew')
        reino_frame.columnconfigure(1, weight=1)
        self.reino_combobox.bind('<<ComboboxSelected>>', lambda e: self._on_reino_selected())
        self._populate_reinos()

        range_frame = tk.Frame(options_frame, bg="#1f5670")
        range_frame.pack(fill=tk.X, padx=12, pady=(0,8))
        self.start_label = ttk.Label(range_frame, text=_('start_number'), style='Label.TLabel')
        self.start_label.grid(row=0, column=0, sticky='w')
        self.labels_dict['start_label'] = ('start_number', self.start_label)
        self.start_entry = ttk.Entry(range_frame, width=10, style='TEntry')
        self.start_entry.grid(row=0, column=1, padx=6, pady=3, sticky='ew')
        self.end_label = ttk.Label(range_frame, text=_('end_number'), style='Label.TLabel')
        self.end_label.grid(row=0, column=2, sticky='w', padx=(12,0))
        self.labels_dict['end_label'] = ('end_number', self.end_label)
        self.end_entry = ttk.Entry(range_frame, width=10, style='TEntry')
        self.end_entry.grid(row=0, column=3, padx=6, pady=3, sticky='ew')
        range_frame.columnconfigure(1, weight=1)
        range_frame.columnconfigure(3, weight=1)

        blocked_frame = tk.Frame(options_frame, bg="#1f5670")
        blocked_frame.pack(fill=tk.X, padx=12, pady=(0,8))
        self.blocked_label = ttk.Label(blocked_frame, text=_('blocked_numbers'), style='Label.TLabel')
        self.blocked_label.grid(row=0, column=0, sticky='w')
        self.labels_dict['blocked_label'] = ('blocked_numbers', self.blocked_label)
        self.blocked_entry = ttk.Entry(blocked_frame, width=28, style='TEntry')
        self.blocked_entry.grid(row=0, column=1, padx=6, pady=3, sticky='ew')
        blocked_frame.columnconfigure(1, weight=1)

        # Niveles: Ciudad y Depósito (1-25)
        levels_frame = tk.Frame(options_frame, bg="#1f5670")
        levels_frame.pack(fill=tk.X, padx=12, pady=(0,8))
        self.city_level_label = ttk.Label(levels_frame, text=_('city_level'), style='Label.TLabel')
        self.city_level_label.grid(row=0, column=0, sticky='w')
        self.labels_dict['city_level_label'] = ('city_level', self.city_level_label)
        self.city_level_cb = ttk.Combobox(levels_frame, values=[str(i) for i in range(1,26)], state='readonly', width=6, textvariable=self.city_level_var, style='TCombobox')
        self.city_level_cb.grid(row=0, column=1, padx=6, pady=3, sticky='w')
        self.warehouse_level_label = ttk.Label(levels_frame, text=_('warehouse_level'), style='Label.TLabel')
        self.warehouse_level_label.grid(row=0, column=2, sticky='w', padx=(12,0))
        self.labels_dict['warehouse_level_label'] = ('warehouse_level', self.warehouse_level_label)
        self.warehouse_level_cb = ttk.Combobox(levels_frame, values=[str(i) for i in range(1,26)], state='readonly', width=6, textvariable=self.warehouse_level_var, style='TCombobox')
        self.warehouse_level_cb.grid(row=0, column=3, padx=6, pady=3, sticky='w')
        levels_frame.columnconfigure(1, weight=1)
        levels_frame.columnconfigure(3, weight=1)

        action_frame = tk.Frame(options_frame, bg="#1f5670")
        action_frame.pack(fill=tk.X, padx=12, pady=(8,0))
        self.recursos_totales_btn = self._add_side_button(action_frame, _('total_resources'), lambda: self.process_resources('totales'), "#5cb85c", 'totales')
        self.recursos_totales_btn.pack(side=tk.LEFT, padx=3, pady=6, expand=True, fill=tk.X)
        self.recursos_cuenta_btn = self._add_side_button(action_frame, _('account_resources'), lambda: self.process_resources('cuenta'), "#0275d8", 'cuenta')
        self.recursos_cuenta_btn.pack(side=tk.LEFT, padx=3, pady=6, expand=True, fill=tk.X)
        self.backpack_btn = self._add_side_button(action_frame, _('backpack_resources'), lambda: self.process_resources('backpack'), "#9b59b6", 'mochila')
        self.backpack_btn.pack(side=tk.LEFT, padx=3, pady=6, expand=True, fill=tk.X)

        update_frame = tk.Frame(options_frame, bg="#1f5670")
        update_frame.pack(fill=tk.X, padx=12, pady=(8,0))
        self.update_btn = self._add_side_button(update_frame, _('update_github'), self.update_from_github, "#f0ad4e")
        self.update_btn.pack(side=tk.LEFT, padx=3, pady=6, expand=True, fill=tk.X)

        progress_frame = tk.Frame(main_frame, bg="#15374a")
        progress_frame.grid(row=1, column=0, columnspan=2, sticky='ew', padx=12, pady=(8,0), ipadx=20)
        progress_inner = tk.Frame(progress_frame, bg="#1f5670")
        progress_inner.pack(fill=tk.X, padx=12, pady=12)
        self.processing_progress_label = ttk.Label(progress_inner, text=_('processing_progress'), style='Label.TLabel')
        self.processing_progress_label.pack(anchor='center', pady=(0,8))
        self.labels_dict['processing_progress_label'] = ('processing_progress', self.processing_progress_label)
        self.progress_bar = ttk.Progressbar(progress_inner, mode='determinate')
        self.progress_bar.pack(fill=tk.X, pady=6)
        self.progress_label = ttk.Label(progress_inner, text="0%", style='Label.TLabel')
        self.progress_label.pack(anchor='center')

    def _refresh_all_texts(self):
        """Actualiza todos los textos de la interfaz al cambiar de idioma"""
        self.root.title(_('title'))
        
        # Actualizar etiquetas de botones
        self.recursos_totales_btn.config(text=_('total_resources'))
        self.recursos_cuenta_btn.config(text=_('account_resources'))
        self.backpack_btn.config(text=_('backpack_resources'))
        self.update_btn.config(text=_('update_github'))
        
        # Actualizar todos los labels guardados en labels_dict
        for key, (translation_key, label_widget) in self.labels_dict.items():
            label_widget.config(text=_(translation_key))
        # pero aquí refrescamos dinámicamente elementos que ya fueron creados

    def _add_side_button(self, parent, text, command, color, icon_key=None):
        icon = self.icons.get(icon_key) if icon_key else None
        btn = tk.Button(parent, text=text, command=command, image=icon, compound=tk.LEFT,
                       bg=color, fg="white", font=('Arial', 11, 'bold'), bd=0, padx=8, pady=8,
                       activebackground='#ffffff', activeforeground='white')
        btn.image = icon  # Mantener referencia al icono
        return btn
        
    def add_images(self):
        filetypes = [(_('image_files'), "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff"), (_('all_files'), "*.*")]
        files = filedialog.askopenfilenames(filetypes=filetypes, title=_('select_images_title'))
        if files:
            for file in files:
                if len(self.selected_images) < 100:
                    self.selected_images.append(file)
                    self.image_listbox.insert(tk.END, Path(file).name)
            if len(self.selected_images) >= 100:
                messagebox.showwarning(_('no_processable_data_title'), _('limit_reached'))
    
    def clear_images(self):
        self.selected_images.clear()
        self.image_listbox.delete(0, tk.END)
        self.extracted_data.clear()
        self.failed_images.clear()
    
    def preprocess_image_for_ocr(self, img):
        img = img.convert("L")
        w, h = img.size
        scale = 1.6
        img = img.resize((int(w * scale), int(h * scale)), Image.BICUBIC)
        img = ImageOps.autocontrast(img, cutoff=1)
        img = img.filter(ImageFilter.SHARPEN)
        return img

    def parse_shorthand_to_number(self, s):
        if not s:
            return None
        s = s.strip().upper().replace(' ', '')
        m = re.match(r'^([\d,.]+)([KMB])?$', s)
        if not m:
            num = re.sub(r'[^\d.,]', '', s)
            try:
                return float(num.replace(',', ''))
            except:
                return None
        val_str = m.group(1).replace(',', '')
        suffix = m.group(2)
        try:
            f = float(val_str)
        except:
            return None
        mult = 1.0
        if suffix == 'K':
            mult = 1e3
        elif suffix == 'M':
            mult = 1e6
        elif suffix == 'B':
            mult = 1e9
        return f * mult

    def _parse_numeric_value(self, text):
        if text is None:
            return None
        value = text.strip()
        if value == '':
            return None
        if not re.fullmatch(r'\d+', value):
            return None
        return int(value)

    def _parse_blocked_numbers(self, text):
        blocked = set()
        if not text:
            return blocked
        text = text.replace(' ', '')
        if not text:
            return blocked
        for part in text.split(','):
            if not part:
                continue
            if '-' in part:
                bounds = part.split('-', 1)
                if len(bounds) != 2:
                    return None
                start = self._parse_numeric_value(bounds[0])
                end = self._parse_numeric_value(bounds[1])
                if start is None or end is None:
                    return None
                if start <= end:
                    blocked.update(range(start, end + 1))
                else:
                    blocked.update(range(end, start + 1))
            else:
                num = self._parse_numeric_value(part)
                if num is None:
                    return None
                blocked.add(num)
        return blocked

    def _build_nickname_list(self, tpl, expected_count):
        start_text = self.start_entry.get().strip()
        end_text = self.end_entry.get().strip()
        blocked_text = self.blocked_entry.get()

        if start_text or end_text:
            if not start_text or not end_text:
                raise ValueError(_('select_start_end'))
            start_num = self._parse_numeric_value(start_text)
            end_num = self._parse_numeric_value(end_text)
            if start_num is None or end_num is None:
                raise ValueError(_('only_numbers'))
            if end_num < start_num:
                raise ValueError(_('end_greater_start'))
            blocked = self._parse_blocked_numbers(blocked_text)
            if blocked is None:
                raise ValueError(_('blocked_format'))
            width = max(len(start_text), len(end_text), tpl.get('index_width', 3))
            prefix = tpl.get('prefix') or tpl.get('nickname_line') or 'NIC'
            all_numbers = list(range(start_num, end_num + 1))
            final_numbers = [n for n in all_numbers if n not in blocked]
            if len(final_numbers) != expected_count:
                raise ValueError(_('images_mismatch', count=expected_count, valid=len(final_numbers)))
            return [f"{prefix}{str(n).zfill(width)}" for n in final_numbers]

        blocked = set(tpl.get('blocked', []))
        replacements = tpl.get('replacements', {})
        blocked = blocked - set(replacements.keys())
        start_idx = tpl.get('index', 1)
        width = tpl.get('index_width', 3)
        prefix = tpl.get('prefix') or tpl.get('nickname_line') or 'NIC'
        nick_list = []
        cur = start_idx
        while len(nick_list) < expected_count:
            if cur in blocked:
                cur += 1
                continue
            val = replacements.get(cur, cur)
            nick_list.append(f"{prefix}{str(val).zfill(width)}")
            cur += 1
        return nick_list

    def format_number_shorthand(self, n):
        if n is None:
            return ""
        try:
            n = float(n)
        except:
            return ""
        if abs(n) >= 1e9:
            return f"{n / 1e9:.1f}B"
        if abs(n) >= 1e6:
            return f"{n / 1e6:.1f}M"
        if abs(n) >= 1e3:
            return f"{n / 1e3:.1f}K"
        if n.is_integer():
            return str(int(n))
        return f"{n:.1f}"

    def extract_resources_from_image(self, image_path):
        try:
            img = Image.open(image_path)
        except Exception as e:
            print("No se pudo abrir imagen:", image_path, e)
            return []

        img_proc = self.preprocess_image_for_ocr(img)

        # Quitar la whitelist para permitir lectura de letras (nombres de recurso)
        tconfig = r'--oem 3 --psm 6'
        try:
            data = pytesseract.image_to_data(img_proc, output_type=pytesseract.Output.DICT, config=tconfig)
        except Exception as e:
            print("Error pytesseract.image_to_data:", e)
            return []

        texts = data.get('text', [])
        confs = data.get('conf', [])
        lefts = data.get('left', [])
        tops = data.get('top', [])
        widths = data.get('width', [])
        heights = data.get('height', [])

        entries = []
        for i, t in enumerate(texts):
            txt = (t or "").strip()
            if not txt:
                continue
            try:
                conf = float(confs[i])
            except:
                try:
                    conf = float(str(confs[i]).strip())
                except:
                    conf = -1.0
            entries.append({
                'text': txt,
                'conf': conf,
                'left': lefts[i],
                'top': tops[i],
                'width': widths[i],
                'height': heights[i],
                'cx': lefts[i] + widths[i] / 2,
                'cy': tops[i] + heights[i] / 2
            })

        resource_names = ['alimentos', 'madera', 'piedra', 'oro']
        num_re = re.compile(r'^\d+\.?\d*\s*[KMB]?$', re.IGNORECASE)

        found = []
        # Primera estrategia: buscar por nombre (etiqueta de recurso) y tomar números a la derecha en la misma fila
        for rname in resource_names:
            chosen_pair = (None, None)
            candidates = [e for e in entries if rname in e['text'].lower()]
            if candidates:
                name_e = sorted(candidates, key=lambda x: -x['conf'])[0]
                row_y = name_e['cy']
                row_h = max(8, name_e['height'])
                nums = [e for e in entries if num_re.match(e['text']) and e['cx'] > name_e['cx'] + 6 and abs(e['cy'] - row_y) < row_h * 1.6]
                if nums:
                    nums_sorted = sorted(nums, key=lambda x: x['cx'])
                    if len(nums_sorted) >= 2:
                        de_obj = nums_sorted[0]['text']
                        total = nums_sorted[-1]['text']
                        chosen_pair = (de_obj, total)
                    else:
                        total = nums_sorted[-1]['text']
                        chosen_pair = (None, total)
            found.append(chosen_pair)

        # Si no encontramos todas las filas por nombre, usar fallback robusto: cluster por cy (filas) y tomar primer/último por cx.
        if not all(p[1] for p in found):
            all_nums = [e for e in entries if num_re.match(e['text'])]
            if all_nums:
                # cluster by cy (merge items whose cy are close)
                clusters = []
                # sort by cy ascending (top to bottom)
                for n in sorted(all_nums, key=lambda x: x['cy']):
                    if not clusters:
                        clusters.append({'items':[n], 'cy_mean': n['cy']})
                    else:
                        # distancia en Y tolerada (ajustable): 36 px por defecto
                        if abs(n['cy'] - clusters[-1]['cy_mean']) > 36:
                            clusters.append({'items':[n], 'cy_mean': n['cy']})
                        else:
                            clusters[-1]['items'].append(n)
                            clusters[-1]['cy_mean'] = sum(i['cy'] for i in clusters[-1]['items'])/len(clusters[-1]['items'])
                fallback = []
                for c in clusters:
                    items_sorted = sorted(c['items'], key=lambda x: x['cx'])
                    if items_sorted:
                        # si hay >=2 valores en la fila, tomar primero como de_obj y último como total
                        if len(items_sorted) >= 2:
                            de = items_sorted[0]['text']
                            tot = items_sorted[-1]['text']
                        else:
                            de = ""
                            tot = items_sorted[-1]['text']
                        fallback.append((de or None, tot))
                    if len(fallback) >= 4:
                        break
                if len(fallback) >= 4:
                    found = fallback[:4]

        # Normalizar / limpiar textos detectados
        cleaned = []
        for de_obj, tot in found:
            de_clean = (de_obj or "").replace(" ", "").upper() if de_obj else ""
            tot_clean = (tot or "").replace(" ", "").upper() if tot else ""
            cleaned.append((de_clean, tot_clean))

        totals = [t for _, t in cleaned if t]
        if len(totals) >= 4:
            result = []
            for i in range(4):
                de_v, tot_v = cleaned[i]
                result.append((de_v, tot_v))
            # Also return the raw OCR entries and processed image for preview/debug
            return result, entries, img_proc
        return [], entries, img_proc

    def preview_selected_image(self):
        sel = self.image_listbox.curselection()
        if not sel:
            messagebox.showinfo("Info", _('select_image'))
            return
        idx = sel[0]
        image_path = self.selected_images[idx]

        # Ejecutar en hilo para no bloquear GUI
        threading.Thread(target=self._preview_thread, args=(image_path,)).start()

    def _preview_thread(self, image_path):
        rows_and_entries = self.extract_resources_from_image(image_path)
        # extract_resources_from_image now returns (result, entries, img_proc) OR ([] , entries, img_proc)
        if isinstance(rows_and_entries, tuple) and len(rows_and_entries) == 3:
            result, entries, img_proc = rows_and_entries
        else:
            result = []
            entries = []
            img_proc = None

        # Crear imagen anotada
        try:
            orig = Image.open(image_path)
        except:
            orig = None
        annotated = (img_proc.copy() if img_proc is not None else (orig.copy() if orig is not None else None))
        if annotated is None:
            messagebox.showerror("Error", "No se pudo abrir imagen para anotación")
            return

        draw = ImageDraw.Draw(annotated)
        try:
            font = ImageFont.load_default()
        except:
            font = None

        # Dibujar todos los cuadros OCR (entries)
        for e in entries:
            left = e['left']
            top = e['top']
            right = left + e['width']
            bottom = top + e['height']
            draw.rectangle([left, top, right, bottom], outline=(200,200,200), width=1)
            text_label = f"{e['text']} ({int(e['conf']) if isinstance(e.get('conf'), (int,float)) else ''})"
            draw.text((left+2, top+1), text_label, fill=(220,220,220), font=font)

        # Resaltar números detectados y los elegidos
        num_re = re.compile(r'^\d+\.?\d*\s*[KMB]?$', re.IGNORECASE)
        # marcar cada número detectado en amarillo
        for e in entries:
            if num_re.match(e['text']):
                left = e['left']; top = e['top']; right = left + e['width']; bottom = top + e['height']
                draw.rectangle([left, top, right, bottom], outline=(200,180,0), width=2)

        # Marcar los pares seleccionados (de_obj azul, total verde)
        # 'result' es lista de 4 tuples (de_obj, total) si se extrajo correctamente
        if result:
            # buscar en entries los textos correspondientes y marcar
            for idx, (de_obj, tot) in enumerate(result):
                # buscar entry con ese texto y confianza alta
                if de_obj:
                    matches = [e for e in entries if e['text'].replace(" ", "").upper() == de_obj.replace(" ", "").upper()]
                    if matches:
                        e = sorted(matches, key=lambda x: -x['conf'])[0]
                        left = e['left']; top = e['top']; right = left + e['width']; bottom = top + e['height']
                        draw.rectangle([left, top, right, bottom], outline=(0,120,255), width=3)
                        draw.text((left, bottom+1), "DeObj", fill=(0,120,255), font=font)
                if tot:
                    matches = [e for e in entries if e['text'].replace(" ", "").upper() == tot.replace(" ", "").upper()]
                    if matches:
                        e = sorted(matches, key=lambda x: -x['conf'])[0]
                        left = e['left']; top = e['top']; right = left + e['width']; bottom = top + e['height']
                        draw.rectangle([left, top, right, bottom], outline=(0,200,0), width=3)
                        draw.text((left, bottom+1), "Total", fill=(0,200,0), font=font)

        # Mostrar en ventana nueva
        self.root.after(0, lambda: self._show_annotated_window(annotated, image_path, result))

    def show_ocr_values(self):
        sel = self.image_listbox.curselection()
        if not sel:
            messagebox.showinfo("Info", _('select_image_ocr'))
            return
        idx = sel[0]
        image_path = self.selected_images[idx]
        threading.Thread(target=self._show_ocr_thread, args=(image_path,)).start()

    def _show_ocr_thread(self, image_path):
        rows_and_entries = self.extract_resources_from_image(image_path)
        if isinstance(rows_and_entries, tuple) and len(rows_and_entries) == 3:
            result, entries, img_proc = rows_and_entries
        else:
            result = []
            entries = []
            img_proc = None

        lines = []
        lines.append("OCR entries (index, text, conf, left, top, width, height, cx, cy):\n")
        for i, e in enumerate(entries):
            txt = e.get('text', '')
            conf = e.get('conf', '')
            left = e.get('left', '')
            top = e.get('top', '')
            w = e.get('width', '')
            h = e.get('height', '')
            cx = e.get('cx', 0)
            cy = e.get('cy', 0)
            lines.append(f"{i}\t{repr(txt)}\tconf={conf}\tleft={left}\ttop={top}\tw={w}\th={h}\tcx={cx:.1f}\tcy={cy:.1f}")
        lines.append("\nDetected result pairs (de_obj, total) (if any):")
        lines.append(repr(result))
        text_all = "\n".join(lines)
        self.root.after(0, lambda: self._show_text_window(text_all, Path(image_path).name))

    def _show_text_window(self, text, title):
        win = tk.Toplevel(self.root)
        win.title(f"OCR Raw - {title}")
        text_frame = tk.Frame(win)
        text_frame.pack(fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        txt = tk.Text(text_frame, width=120, height=30, yscrollcommand=scrollbar.set, wrap='none')
        txt.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=txt.yview)
        txt.insert("1.0", text)
        txt.config(state=tk.DISABLED)
        btn_frame = tk.Frame(win)
        btn_frame.pack(fill=tk.X, pady=6)
        save_btn = tk.Button(btn_frame, text="Guardar como .txt", command=lambda: self._save_text(text),
                             bg="#5bc0de", fg="white")
        save_btn.pack(side=tk.LEFT, padx=6)
        close_btn = tk.Button(btn_frame, text="Cerrar", command=win.destroy)
        close_btn.pack(side=tk.LEFT, padx=6)

    def _save_text(self, text):
        fp = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[(_('text_files'),"*.txt"), (_('all_files'),"*.*")], title=_('save_ocr_raw'))
        if not fp:
            return
        try:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(text)
            messagebox.showinfo(_('success'), _('save_success', path=fp))
        except Exception as e:
            messagebox.showerror("Error", _('save_error', error=str(e)))

    def _show_annotated_window(self, annotated_img, image_path, result):
        win = tk.Toplevel(self.root)
        win.title(f"{_('ocr_preview_title')} - {Path(image_path).name}")
        # escala si es muy grande
        screen_w = win.winfo_screenwidth()
        screen_h = win.winfo_screenheight()
        max_w = int(screen_w * 0.8)
        max_h = int(screen_h * 0.8)
        w, h = annotated_img.size
        scale = min(1.0, max_w / w, max_h / h)
        display_img = annotated_img if scale == 1.0 else annotated_img.resize((int(w*scale), int(h*scale)), Image.ANTIALIAS)

        photo = ImageTk.PhotoImage(display_img)
        canvas = tk.Canvas(win, width=display_img.width, height=display_img.height, bg='black')
        canvas.pack()
        canvas.create_image(0,0, anchor='nw', image=photo)
        # mantener referencia
        canvas.image = photo

        info_frame = tk.Frame(win)
        info_frame.pack(fill=tk.X, pady=6)
        save_btn = tk.Button(info_frame, text=_('save_annotated'), command=lambda: self._save_annotated(annotated_img),
                             bg="#5bc0de", fg="white")
        save_btn.pack(side=tk.LEFT, padx=6)
        close_btn = tk.Button(info_frame, text=_('close'), command=win.destroy)
        close_btn.pack(side=tk.LEFT, padx=6)

        # texto con los pares seleccionados (si existen)
        if result:
            lbl = tk.Label(win, text="Valores extraídos (De objetos, Total) por fila (Alimentos, Madera, Piedra, Oro):", anchor='w')
            lbl.pack(fill=tk.X, padx=8)
            for pair in result:
                tk.Label(win, text=str(pair), anchor='w').pack(fill=tk.X, padx=8)
        else:
            tk.Label(win, text=_('no_correct_detection'), fg='red').pack(fill=tk.X, padx=8)

    def _save_annotated(self, pil_img):
        fp = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[(_('png_image'), "*.png")], title=_('save_annotated'))
        if not fp:
            return
        try:
            pil_img.save(fp)
            messagebox.showinfo(_('success'), _('save_success', path=fp))
        except Exception as e:
            messagebox.showerror("Error", _('save_error', error=str(e)))

    def _get_default_save_dir(self):
        # Guardar en la carpeta de instalación/exe cuando sea un .exe, o en el directorio del script en modo desarrollo.
        base_dir = self._get_install_base()
        default_dir = base_dir / 'GUARDADOS'
        default_dir.mkdir(parents=True, exist_ok=True)
        return default_dir

    def _save_results_file(self, default_filename):
        default_dir = self._get_default_save_dir()
        initial_path = default_dir / default_filename
        fp = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[(_('text_files'), "*.txt"), (_('all_files'), "*.*")],
            initialdir=str(default_dir),
            initialfile=default_filename,
            title=_('save_results')
        )
        if not fp:
            fp = str(initial_path)
        try:
            with open(fp, 'w', encoding='utf-8') as f:
                for idx, e in enumerate(self.output_entries, start=1):
                    if e is None:
                        f.write(f"Cuenta {idx}: No se pudo procesar la imagen.\n")
                        f.write("---\n")
                        continue
                    f.write(f"Nickname: {e.get('Nickname','')}\n")
                    f.write(f"Nivel de ciudad: {e.get('Nivel de ciudad','')}\n")
                    f.write(f"Nivel de depósito: {e.get('Nivel de depósito','')}\n")
                    f.write(f"Comida: {int(e['Comida']) if e.get('Comida') is not None else 0}\n")
                    f.write(f"Madera: {int(e['Madera']) if e.get('Madera') is not None else 0}\n")
                    f.write(f"Piedra: {int(e['Piedra']) if e.get('Piedra') is not None else 0}\n")
                    f.write(f"Oro: {int(e['Oro']) if e.get('Oro') is not None else 0}\n")
                    f.write("---\n")
            msg = _('save_success', path=fp)
            if self.failed_images:
                msg += "\n\n" + _('failed_images', images=", ".join(self.failed_images))
            messagebox.showinfo(_('success'), msg)
        except Exception as e:
            messagebox.showerror("Error", _('save_error', error=str(e)))

    def load_kingdom_file(self):
        fp = filedialog.askopenfilename(filetypes=[(_('text_files'),"*.txt"), (_('all_files'),"*.*")], title=_('select_kingdom'))
        if not fp:
            return
        self.kingdom_template_path = fp
        # display filename in combobox
        name = Path(fp).name
        self.reino_combobox['values'] = [name]
        self.reino_combobox.set(name)

    def parse_kingdom_template(self):
        # Returns a dict with template fields and starting nickname index
        tpl = {'nickname_line': None, 'prefix': None, 'index': 1, 'index_width': 3, 'fields': {}, 'blocked': set(), 'replacements': {}}
        path = getattr(self, 'kingdom_template_path', None)
        if not path or not os.path.isfile(path):
            return tpl
        try:
            with open(path, 'r', encoding='utf-8') as f:
                lines = [ln.rstrip('\n') for ln in f]
        except:
            return tpl
        collecting_blocked = False
        for ln in lines:
            if ln.lower().startswith('nickname:'):
                tpl['nickname_line'] = ln
                # parse nickname value
                parts = ln.split(':',1)
                if len(parts) > 1:
                    val = parts[1].strip()
                    # find trailing digits
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
            # detect bloqueados section: either inline on the same line or following lines with numbers
            ln_strip = ln.strip()
            ln_low = ln_strip.lower()
            if ln_low.startswith('bloqueados'):
                # inline numbers
                found = re.findall(r'\d+', ln_strip)
                for num in found:
                    try:
                        tpl['blocked'].add(int(num))
                    except:
                        pass
                collecting_blocked = True
                continue
            if collecting_blocked:
                # stop collecting if we hit a new key or separator
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
            # simple capture of levels and resource keys
            if ':' in ln:
                k,v = ln.split(':',1)
                tpl['fields'][k.strip()] = v.strip()
        
        # post-process: expand ranges like "41-60" into individual numbers
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
        
        return tpl

    def _populate_reinos(self):
        # scan ./kingdoms for .txt files and populate combobox
        kdir = self._resolve_path('kingdoms')
        vals = []
        try:
            if kdir.exists() and kdir.is_dir():
                for p in sorted(kdir.glob('*.txt')):
                    vals.append(p.name)
        except Exception:
            vals = []
        self.reino_combobox['values'] = vals
        if vals:
            self.reino_combobox.set(vals[0])
            self.kingdom_template_path = str(kdir / vals[0])

    def _on_reino_selected(self):
        sel = self.reino_combobox.get()
        if not sel:
            return
        base = Path(__file__).parent
        kpath = base / 'kingdoms' / sel
        if kpath.exists():
            self.kingdom_template_path = str(kpath)

    def process_resources(self, tipo):
        if not self.selected_images:
            messagebox.showerror("Error", _('no_images'))
            return

        self.recursos_totales_btn.config(state=tk.DISABLED)
        self.recursos_cuenta_btn.config(state=tk.DISABLED)
        self.backpack_btn.config(state=tk.DISABLED)

        thread = threading.Thread(target=self._process_thread, args=(tipo,))
        thread.start()

    def open_new_window(self):
        # Spawn a new process running the same script so user can open multiple independent GUIs
        try:
            base = Path(__file__).parent
            python = sys.executable
            script = str(Path(__file__).resolve())
            subprocess.Popen([python, script], cwd=str(base))
        except Exception as e:
            messagebox.showerror("Error", _('cannot_open_window', error=str(e)))

    def update_from_github(self):
        if not messagebox.askyesno(_('update_confirm_title'), _('update_confirm')):
            return
        threading.Thread(target=self._update_from_github_thread, daemon=True).start()

    def _update_from_github_thread(self):
        self.root.after(0, lambda: self.update_btn.config(state=tk.DISABLED, text="Descargando..."))
        try:
            self._download_repo_resources()
            self.root.after(0, lambda: self._populate_reinos())
            self.root.after(0, lambda: messagebox.showinfo(_('update_complete_title'), _('update_complete')))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", _('update_error', error=str(e))))
        finally:
            self.root.after(0, lambda: self.update_btn.config(state=tk.NORMAL, text=_('update_github')))

    def _download_repo_resources(self):
        url = GITHUB_REPO_ZIP_URL
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_zip = Path(tmpdir) / 'repo.zip'
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            
            try:
                with urllib.request.urlopen(req, timeout=30) as response:
                    if response.getcode() != 200:
                        raise Exception(f"Respuesta inválida de GitHub: {response.getcode()}")
                    
                    # Mostrar progreso de descarga
                    total_size = int(response.headers.get('content-length', 0))
                    downloaded = 0
                    chunk_size = 8192
                    
                    with open(tmp_zip, 'wb') as f:
                        while True:
                            chunk = response.read(chunk_size)
                            if not chunk:
                                break
                            downloaded += len(chunk)
                            f.write(chunk)
                            
                            if total_size > 0:
                                progress = min(100, int(downloaded * 100 / total_size))
                                self.root.after(0, lambda p=progress: self.update_btn.config(
                                    text=f"Actualizando... {p}%"
                                ))
            except Exception as e:
                raise Exception(f"Error descargando de GitHub: {e}")
            
            try:
                with zipfile.ZipFile(tmp_zip, 'r') as zf:
                    root_prefix = None
                    for name in zf.namelist():
                        if name.endswith('/'):
                            continue
                        root_prefix = name.split('/', 1)[0] + '/'
                        break
                    
                    if not root_prefix:
                        raise Exception('No se encontró el contenido del repositorio en el ZIP')
                    
                    install_dir = self._get_install_base()
                    files_updated = 0
                    
                    for name in zf.namelist():
                        if not name.startswith(root_prefix):
                            continue
                        
                        rel_path = name[len(root_prefix):]
                        
                        # Saltar directorios vacíos
                        if not rel_path or name.endswith('/'):
                            continue
                        
                        # Actualizar TODOS los archivos, no solo kingdoms e iconos
                        target = install_dir / rel_path
                        target.parent.mkdir(parents=True, exist_ok=True)
                        
                        try:
                            with zf.open(name) as src, open(target, 'wb') as dst:
                                dst.write(src.read())
                            files_updated += 1
                            print(f"Actualizado: {rel_path}")
                        except Exception as e:
                            print(f"Advertencia: No se pudo actualizar {rel_path}: {e}")
                    
                    if files_updated == 0:
                        raise Exception("No se encontraron archivos para actualizar en el repositorio")
                    
                    print(f"Actualización completada: {files_updated} archivos actualizados")
                    
            except zipfile.BadZipFile:
                raise Exception("El archivo descargado no es un ZIP válido")
            except Exception as e:
                error_str = str(e)
                print(f"ERROR EN EXTRACCIÓN: {error_str}")
                raise Exception(f"Error extrayendo archivos: {error_str}")
        
        return True

    def _process_thread(self, tipo):
        try:
            self.extracted_data.clear()
            self.failed_images.clear()
            # reset output entries each run
            self.output_entries = [None] * len(self.selected_images)

            total_images = len(self.selected_images)

            # Prepare nickname list in selection order to preserve sequence even with parallel processing
            tpl = self.parse_kingdom_template()
            try:
                nick_list = self._build_nickname_list(tpl, total_images)
            except ValueError as err:
                err_msg = str(err)
                self.root.after(0, lambda err_msg=err_msg: messagebox.showerror("Error", err_msg))
                return

            # mapping image_path -> index for placing results
            index_map = {p: i for i, p in enumerate(self.selected_images)}

            # configure worker count (limit to avoid oversubscription)
            max_workers = min(8, (os.cpu_count() or 2) * 2)
            completed = 0

            def _process_single(image_path):
                try:
                    res = self.extract_resources_from_image(image_path)
                    if isinstance(res, tuple) and len(res) == 3:
                        rows, entries, img_proc = res
                    else:
                        rows, entries, img_proc = [], [], None
                    if rows and len(rows) == 4:
                        values = []
                        for de_obj, tot in rows:
                            if tipo == 'cuenta':
                                tot_num = self.parse_shorthand_to_number(tot) if tot else None
                                de_num = self.parse_shorthand_to_number(de_obj) if de_obj else 0.0
                                if tot_num is None:
                                    values.append(None)
                                else:
                                    values.append(int(round(tot_num - (de_num or 0.0))))
                            elif tipo == 'backpack':
                                de_num = self.parse_shorthand_to_number(de_obj) if de_obj else None
                                values.append(int(round(de_num)) if de_num is not None else None)
                            else:
                                tot_num = self.parse_shorthand_to_number(tot) if tot else None
                                values.append(int(round(tot_num)) if tot_num is not None else None)
                        return (image_path, values)
                    else:
                        return (image_path, None)
                except Exception as e:
                    return (image_path, None)

            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as ex:
                futures = {ex.submit(_process_single, p): p for p in self.selected_images}
                for fut in concurrent.futures.as_completed(futures):
                    image_path = futures[fut]
                    try:
                        img_path, values = fut.result()
                    except Exception:
                        img_path, values = image_path, None
                    idx = index_map.get(image_path, None)
                    if values is None:
                        self.failed_images.append(Path(image_path).name)
                    else:
                        nick = nick_list[idx] if idx is not None and idx < len(nick_list) else f"NIC{idx or 0}"
                        entry = {
                            'Nickname': nick,
                            'Nivel de ciudad': (self.city_level_var.get() if getattr(self, 'city_level_var', None) else tpl.get('fields', {}).get('Nivel de ciudad', '')),
                            'Nivel de depósito': (self.warehouse_level_var.get() if getattr(self, 'warehouse_level_var', None) else tpl.get('fields', {}).get('Nivel de depósito', '')),
                            'Comida': values[0] if len(values) > 0 else None,
                            'Madera': values[1] if len(values) > 1 else None,
                            'Piedra': values[2] if len(values) > 2 else None,
                            'Oro': values[3] if len(values) > 3 else None,
                        }
                        if idx is not None:
                            self.output_entries[idx] = entry
                        else:
                            self.output_entries.append(entry)
                    completed += 1
                    self._update_progress(int((completed / total_images) * 100))
                    time.sleep(0.02)

            self._update_progress(100)
            time.sleep(0.25)

            if not getattr(self, 'output_entries', None):
                self.root.after(0, lambda: messagebox.showwarning(_('no_processable_data_title'), _('no_processable_data')))
            else:
                try:
                    kname = 'results'
                    if getattr(self, 'kingdom_template_path', None):
                        try:
                            kname = Path(self.kingdom_template_path).stem
                        except:
                            kname = 'results'
                    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
                    default_filename = f"{kname}_results_{ts}.txt"
                    self.root.after(0, lambda default_filename=default_filename: self._save_results_file(default_filename))
                except Exception as e:
                    err_msg = _('save_error', error=str(e))
                    self.root.after(0, lambda err_msg=err_msg: messagebox.showerror("Error", err_msg))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", _('processing_error', error=str(e))))
        finally:
            self.root.after(0, lambda: self.recursos_totales_btn.config(state=tk.NORMAL))
            self.root.after(0, lambda: self.recursos_cuenta_btn.config(state=tk.NORMAL))
            self.root.after(0, lambda: self.backpack_btn.config(state=tk.NORMAL))
            self.root.after(0, lambda: self._update_progress(0))

    def _update_progress(self, value):
        self.root.after(0, lambda: self.progress_bar.configure(value=value))
        self.root.after(0, lambda: self.progress_label.config(text=f"{value}%"))
        self.root.update_idletasks()

    def _show_failed_images_notice(self):
        if self.failed_images:
            self.root.after(0, lambda: messagebox.showinfo("Aviso", "Algunas imágenes no fueron procesadas: " + ", ".join(self.failed_images)))

def main():
    root = tk.Tk()
    app = ResourceExtractorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
