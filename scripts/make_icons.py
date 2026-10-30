"""Genera los iconos de Android a partir de assets/icon.png y los copia al proyecto android/."""
import glob, os, sys
from PIL import Image, ImageDraw

RES = sys.argv[1] if len(sys.argv) > 1 else "android/app/src/main/res"
src = Image.open("assets/icon.png").convert("RGBA")
w, h = src.size
# Color de fondo = color del panel oscuro del icono
px = [src.getpixel((int(w * .3) + i, int(h * .12) + j))[:3] for i in range(10) for j in range(10)]
bg = tuple(sorted(c[k] for c in px)[len(px) // 2] for k in range(3))
hexbg = "#%02X%02X%02X" % bg
full = Image.new("RGBA", src.size, bg + (255,))
full.alpha_composite(src)  # cuadrado completo sin esquinas transparentes

for old in glob.glob(f"{RES}/**/ic_launcher*", recursive=True):
    os.remove(old)
dens = {"mdpi": 1, "hdpi": 1.5, "xhdpi": 2, "xxhdpi": 3, "xxxhdpi": 4}
for d, k in dens.items():
    folder = f"{RES}/mipmap-{d}"
    os.makedirs(folder, exist_ok=True)
    s = int(48 * k)
    src.resize((s, s), Image.LANCZOS).save(f"{folder}/ic_launcher.png")
    r = full.resize((s, s), Image.LANCZOS)
    m = Image.new("L", (s * 4, s * 4), 0)
    ImageDraw.Draw(m).ellipse((0, 0, s * 4 - 1, s * 4 - 1), fill=255)
    r.putalpha(m.resize((s, s), Image.LANCZOS))
    r.save(f"{folder}/ic_launcher_round.png")
    f = int(108 * k)
    fg = Image.new("RGBA", (f, f), (0, 0, 0, 0))
    inner = int(f * .62)
    fg.paste(full.resize((inner, inner), Image.LANCZOS), ((f - inner) // 2, (f - inner) // 2))
    fg.save(f"{folder}/ic_launcher_foreground.png")

os.makedirs(f"{RES}/mipmap-anydpi-v26", exist_ok=True)
for n in ("ic_launcher", "ic_launcher_round"):
    open(f"{RES}/mipmap-anydpi-v26/{n}.xml", "w").write(
        '<?xml version="1.0" encoding="utf-8"?>\n<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n'
        '  <background android:drawable="@color/ic_launcher_background"/>\n'
        '  <foreground android:drawable="@mipmap/ic_launcher_foreground"/>\n</adaptive-icon>\n')
os.makedirs(f"{RES}/values", exist_ok=True)
open(f"{RES}/values/ic_launcher_background.xml", "w").write(
    f'<?xml version="1.0" encoding="utf-8"?>\n<resources>\n  <color name="ic_launcher_background">{hexbg}</color>\n</resources>\n')
# Pantalla de arranque: color liso del icono (sustituye el logo por defecto de Capacitor)
for p in glob.glob(f"{RES}/**/splash*.png", recursive=True):
    Image.new("RGB", (16, 16), bg).save(p)
print("Iconos generados. Fondo", hexbg)
