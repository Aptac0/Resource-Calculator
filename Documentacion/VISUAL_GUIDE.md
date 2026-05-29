# 🎨 Guía Visual - Selector de Idiomas

## Ubicación del Selector

```
┌─────────────────────────────────────────────────────────────────┐
│ Idioma: [Español ▼]                                             │ ← SELECTOR AQUÍ
├─────────────────────────────────────────────────────────────────┤
│                  CALCULADORA DE RECURSOS                        │
│                                                                 │
│  ┌──────────────────────┬──────────────────────────────────┐   │
│  │ Selector de Imágenes │  Configuración de Reino          │   │
│  │                      │                                  │   │
│  │ [Listado de imágenes]│  Reino: [dropdown]              │   │
│  │                      │  Número de inicio: [_____]      │   │
│  │ [+ Agregar]          │  Número de fin:    [_____]      │   │
│  │ [- Limpiar]          │  Números bloqueados: [_______]  │   │
│  │ [⊞ Nueva ventana]    │                                  │   │
│  │                      │  Nivel de Puesto Venta: [1-25]  │   │
│  │                      │  Nivel de depósito:    [1-25]   │   │
│  │                      │                                  │   │
│  │                      │  [$ Recursos Totales]           │   │
│  │                      │  [$ Recursos de Cuenta]         │   │
│  │                      │  [$ Recursos de Mochila]        │   │
│  │                      │  [⚙ Actualizar GitHub]          │   │
│  └──────────────────────┴──────────────────────────────────┘   │
│                                                                 │
│  Progreso de Procesamiento:                                    │
│  [████████░░░░░░░░░░░░░░] 40%                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Cambio de Idioma - Paso a Paso

### Paso 1: Haz clic en el dropdown
```
Idioma: [Español ▼] ← Haz clic aquí
```

### Paso 2: Se abre el menú
```
┌─────────────────────┐
│ Español        (✓)  │ ← Actualmente seleccionado
│ English             │
│ Português           │
│ Bahasa Indonesia    │
│ Tiếng Việt          │
│ Français            │
└─────────────────────┘
```

### Paso 3: Selecciona tu idioma
```
Idioma: [English ▼] ← La interfaz cambia automáticamente
```

## Vista de la Interfaz en Cada Idioma

### 🇪🇸 Español (Predeterminado)
```
Idioma: [Español ▼]
CALCULADORA DE RECURSOS
Selector de Imágenes | Configuración de Reino
[+] Agregar Imágenes
[-] Limpiar Lista
[⊞] Nueva ventana
```

### 🇬🇧 English
```
Language: [English ▼]
RESOURCE CALCULATOR
Image Selector | Kingdom Configuration
[+] Add Images
[-] Clear List
[⊞] New Window
```

### 🇵🇹 Português
```
Idioma: [Português ▼]
CALCULADORA DE RECURSOS
Seletor de Imagens | Configuração do Reino
[+] Adicionar Imagens
[-] Limpar Lista
[⊞] Nova Janela
```

### 🇮🇩 Bahasa Indonesia
```
Bahasa: [Bahasa Indonesia ▼]
KALKULATOR SUMBER DAYA
Pemilih Gambar | Konfigurasi Kerajaan
[+] Tambah Gambar
[-] Bersihkan Daftar
[⊞] Jendela Baru
```

### 🇻🇳 Tiếng Việt
```
Ngôn Ngữ: [Tiếng Việt ▼]
MÁY TÍNH TÀI NGUYÊN
Bộ Chọn Hình Ảnh | Cấu Hình Vương Quốc
[+] Thêm Hình Ảnh
[-] Xóa Danh Sách
[⊞] Cửa Sổ Mới
```

### 🇫🇷 Français
```
Langue: [Français ▼]
CALCULATRICE DE RESSOURCES
Sélecteur d'Images | Configuration du Royaume
[+] Ajouter des Images
[-] Effacer la Liste
[⊞] Nouvelle Fenêtre
```

## Menú Desplegable de Idiomas (Completo)

```
┌──────────────────────────────┐
│ Idioma: [Selecciona ▼]       │
├──────────────────────────────┤
│ ✓ Español                    │
│   English                    │
│   Português                  │
│   Bahasa Indonesia           │
│   Tiếng Việt                 │
│   Français                   │
└──────────────────────────────┘
```

## Elementos Traducidos Ejemplos

### Botones
```
ES: [Agregar Imágenes]    EN: [Add Images]         PT: [Adicionar Imagens]
ES: [Limpiar Lista]       EN: [Clear List]         PT: [Limpar Lista]
ES: [Nueva ventana]       EN: [New Window]         PT: [Nova Janela]
```

### Labels/Etiquetas
```
ES: "Reino:"              EN: "Kingdom:"           PT: "Reino:"
ES: "Número de inicio:"   EN: "Start Number:"      PT: "Número de Início:"
ES: "Nivel de depósito:"  EN: "Warehouse Level:"   PT: "Nível do Armazém:"
```

### Botones de Acción
```
ES: [Recursos Totales]    EN: [Total Resources]    PT: [Recursos Totais]
ES: [Recursos de Cuenta]  EN: [Account Resources]  PT: [Recursos da Conta]
ES: [Recursos de Mochila] EN: [Backpack Resources] PT: [Recursos da Mochila]
ES: [Actualizar GitHub]   EN: [Update GitHub]      PT: [Atualizar GitHub]
```

### Mensajes de Error/Éxito
```
ES: "No hay imágenes seleccionadas"
EN: "No images selected"
PT: "Nenhuma imagem selecionada"
FR: "Aucune image sélectionnée"
```

## Datos Que NO Cambian

### Siempre son iguales independientemente del idioma:
- ✅ Archivo de salida `.txt` (mismo formato)
- ✅ Nombres de recursos: Comida, Madera, Piedra, Oro
- ✅ Números y valores numéricos
- ✅ Rutas de archivos
- ✅ Contenido del archivo del reino

## Notas Importantes

1. **El selector está siempre visible** en la barra superior
2. **Los cambios son instantáneos** - no necesita reiniciar la app
3. **Es muy rápido** - menos de 100ms para cambiar idioma
4. **No afecta los datos** - solo la interfaz visual

---

**Tip**: Para usuarios multinacionales en tu equipo, pueden dejar cada máquina en su idioma preferido. ¡Fácil! 🌍
