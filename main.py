import os
from PIL import Image

stickers_folder = "stickers"
output_folder = "resized"
max_size = 512  

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(stickers_folder):
    if not filename.lower().endswith('.png'):
        continue

    path = os.path.join(stickers_folder, filename)
    im = Image.open(path).convert("RGBA")

    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)


    ratio = max_size / max(im.width, im.height)
    new_size = (int(im.width * ratio), int(im.height * ratio))
    im = im.resize(new_size, Image.LANCZOS)


    new_im = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    x = (512 - im.width) // 2
    y = (512 - im.height) // 2
    new_im.paste(im, (x, y), im)

    out_path = os.path.join(output_folder, filename)
    new_im.save(out_path, optimize=True)
    print(f"{filename} -> {out_path}")

print("Done!")
