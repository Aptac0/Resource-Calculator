# RSS STORE APTAC - Resource Calculator

**[Español](README_es.md) | English | [Português](README_pt.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Français](README_fr.md)**

Desktop application to automatically extract kingdom resources from screenshots using OCR with smart nickname generation.

---

## 📖 Table of Contents

1. [Quick Guide](#-quick-guide)
2. [How to Take Screenshots](#-how-to-take-screenshots)
3. [Input Formats](#-input-formats)
4. [Buttons and Functions](#-buttons-and-functions)
5. [Results and Saved Files](#-results-and-saved-files)
6. [Troubleshooting](#-troubleshooting)
7. [Update System](#-update-system)

---

## 🚀 Quick Guide

### Step by Step

1. **Open the application**
   - Run `RSS STORE APTAC.exe`
   - Select the language in the main menu

2. **Add images**
   - Click the `Add Images` button
   - Select your screenshot captures
   - Images load into the list

3. **Configure kingdom**
   - Choose the `Kingdom` from the dropdown
   - Available kingdoms update from GitHub

4. **Fill in numbers**
   - `Start number`: First account number (e.g., 1)
   - `End number`: Last account number (e.g., 30)
   - `Blocked numbers` (optional): Accounts to skip (e.g., 3,5,7)

5. **Set levels**
   - `City Level`: Market Shop level (1–25)
   - `Warehouse Level`: Storage level (1–25)

6. **Process resources**
   - Click the resource button you need:
     - `Total Resources`: Total per account
     - `Account Resources`: Net values
     - `Backpack Resources`: Inventory only

7. **Find results**
   - Auto-saved to `GUARDADOS/`
   - Name: `KINGDOM_results_YYYYMMDD_HHMMSS.txt`

## 📸 How to Take Screenshots

### From PC (Recommended)

✅ **Correct way:**
- Open the game in windowed mode
- Capture the Resources window clearly
- Ensure numbers are not cut off
- Image must be sharp without shadows

![Screenshot from PC](../Ejemplos/Foto-desde-PC.png)

**Tips:**
- Use Windows screenshot tool (Win + Shift + S)
- Include only the resources dialog
- Numbers and labels must be readable

### From Mobile

⚠️ **Important:**
1. Take screenshot on mobile
2. **Transfer to PC** (USB, Google Drive, Telegram, etc.)
3. Avoid angled or blurry photos
4. Screenshot must be sharp and clear

![Screenshot from Mobile](../Ejemplos/Foto-desde-Movil.png)

**Recommendations:**
- Use native mobile screenshot (better than photo)
- Good lighting
- No reflections or shadows
- Transfer without compression

## 🔢 Input Formats

### Start Number and End Number

- **Numbers only**: `1` to `30` (e.g., start=1, end=30)
- **Must be positive integers**
- **Number of images must match** valid accounts

### Blocked Numbers (Optional)

**Two formats allowed:**

**Format 1: Range**
```
1-10      → 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
3-5       → 3, 4, 5
```

**Format 2: List**
```
1,3,5,7   → 1, 3, 5, 7
3, 5, 8   → 3, 5, 8 (spaces allowed)
```

**Format 3: Mixed**
```
1-5,8,10-15  → 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 14, 15
```

### Practical Example

| Field | Value | Result |
|-------|-------|--------|
| Start | 1 | Account 1 |
| End | 10 | Account 10 |
| Blocked | 3,5 | Processes: 1,2,4,6,7,8,9,10 |
| Images | 8 | ✅ Valid (matches) |

⚠️ If number of images ≠ valid accounts, you'll see an error.

### Levels

- `City Level` (Market Shop): 1-25
- `Warehouse Level` (Storage): 1-25

![Market Shop Levels](../Ejemplos/Niveles-Puesto-de-Venta.png)
![Storage Levels](../Ejemplos/Niveles-de-Almacen.png)

## 🎯 Buttons and Functions

### Add Images
- Opens file selector
- Select multiple captures
- Adds to processing list

### Clear List
- Empties all loaded images
- Removes temporary data
- Useful for starting a new batch

### New Window
- Opens another app instance
- Useful for multiple tasks

### Update GitHub
- Downloads latest `kingdoms/` and `Iconos/` from repo
- Overwrites local data
- If using .exe, shows releases page for new installer

### Total Resources
- Processes images for each account
- Saves: Food, Wood, Stone, Gold amounts
- Shows total per account
- Useful for inventory tracking

### Account Resources
- Calculates net resources (total - inventory)
- Subtracts backpack items
- Shows actual account resources
- Better for account management

### Backpack Resources
- Shows only inventory items
- Extracts "from objects" values
- Useful for packing analysis

## 💾 Results and Saved Files

### File Location

```
GUARDADOS/
├── KINGDOM_results_20260602_143022.txt
├── KINGDOM_results_20260602_145015.txt
└── KINGDOM_results_20260603_101530.txt
```

### File Format

```
Nickname: Account_1
City Level: 15
Warehouse Level: 18
Food: 45.0K
Wood: 32.5K
Stone: 28.7K
Gold: 5.6K
---
Nickname: Account_2
City Level: 15
Warehouse Level: 18
Food: 41.2K
Wood: 35.1K
Stone: 26.8K
Gold: 6.1K
---
```

### How to Use Results

1. Open the `.txt` file in an editor
2. Copy the data you need
3. Paste it into your management tool
4. Nicknames generate automatically

---

## 🆘 Troubleshooting

### "Could not detect 4 values"
- Screenshot quality issue - try clearer image
- Numbers must be clearly visible
- Try recropping or retaking screenshot
- Adjust brightness if numbers are dark

### "Error: X images selected but Y valid accounts"
- Number of images doesn't match valid accounts
- Check start/end numbers and blocked numbers
- Use the formula: (end - start + 1) - blocked = total needed
- Add or remove images to match

### "Update error"
- Check internet connection
- Try again in a few minutes
- Restart the application if error persists
- Check firewall settings

### Images won't process
- Verify kingdom is selected
- Check all number fields are filled
- Ensure image count matches expected accounts
- Try previewing image first to check OCR quality

### "Cannot open window"
- Another instance may be running
- Close existing windows and retry
- Try running as Administrator

---

## 🔄 Update System

### Automatic
- The app **checks for new versions at startup**
- If an update is available, notification appears
- Automatic download from GitHub
- Installation without intervention

### Manual
- Run `actualizar.bat` in the installation folder
- It updates directly from the repository

### What Updates
- `kingdoms/` → New templates
- `Iconos/` → New icons
- .exe version → From Releases

---

## 📋 Available Levels

### City Level (Market Shop)
- Range: 1 to 25
- Applies to all resources
- Saved in results

![Market Shop Levels](../Ejemplos/Niveles-Puesto-de-Venta.png)

### Warehouse Level (Storage)
- Range: 1 to 25
- Available storage
- Saved in results

![Storage Levels](../Ejemplos/Niveles-de-Almacen.png)

### Maximum Technology
- Affects resource capacity
- Reference in the app

![Maximum Technology](../Ejemplos/Tecnologia-Maxima.png)

---

## 🎯 Complete Example

**Scenario:** You have 5 accounts, you want total resources

1. **Prepare screenshots**
   - Take 5 screenshots (one per account)
   - Transfer to PC
   - Save in an accessible folder

2. **Configure the app**
   - Add Images → select 5
   - Kingdom → choose correct one
   - Start number: 1
   - End number: 5
   - Blocked numbers: (empty)
   - City Level: 15
   - Warehouse Level: 18

3. **Process**
   - Click `Total Resources`
   - Wait for completion
   - You will see progress in %

4. **Results**
   - File saved automatically
   - Open `GUARDADOS/REINO_results_*.txt`
   - Copy data to your tool
