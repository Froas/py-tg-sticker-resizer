# Sticker Resizer for Telegram

A simple Python script to crop, resize, and center LINE (or other) sticker PNGs into 512x512 px squares, perfect for use in Telegram, and other messengers where is a 512x512 px limit.


---

## How to Use

### 1. Download Stickers

Use [https://line-stickers.github.io/](https://line-stickers.github.io/) to download the sticker pack you want.

### 2. Extract PNG Files

* From the folder:
  `Windows_StickersEditor/StickersEditorWorkspace/ImagesCache/Remote/LINE_XXXXXXXX`
* Copy all `.png` files into the `stickers` folder at the root of your project.

**Your project should look like this:**

```
your_project/
├── main.py
├── stickers/
│   ├── XXXXXXXX.png
│   ├── XXXXXXXY.png
│   └── ...
```

### 3. Install Dependencies

```bash
pip install pillow
```

### 4. Run the Script

```bash
python main.py
```

### 5. Check the Output

Resized and centered stickers will appear in the `resized` folder (created automatically):

```
your_project/
├── resized/
│   ├── XXXXXXXX.png
│   ├── XXXXXXXY.png
│   └── ...
```

---

## What the Script Does

* Finds all PNG files in the `stickers` folder
* Crops transparent edges
* Resizes the image so the largest side is 512 px (proportionally)
* Centers the resized image on a transparent 512x512 px square
* Saves the result in the `resized` folder

---

## Requirements

* Python 3.10
* Pillow (`pip install pillow`)

---

## Need Help?

If you have questions or issues, feel free to ask!


---

**Made with ❤️ by [Froas](https://github.com/Froas)**

---
