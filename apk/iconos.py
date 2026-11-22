"""Genera el ícono y la pantalla de carga de FisicApp para Android (se ejecuta una vez; los PNG quedan en apk/res)."""
from PIL import Image, ImageDraw
import os
RED, RED_DK, INK, WHITE = (212,42,59), (158,22,39), (26,26,34), (255,255,255)
OUT = os.path.join(os.path.dirname(__file__), "res")

def lens(d, cx, cy, R):
    """Lente azul con aro blanco y borde negro, R = radio exterior."""
    d.ellipse([cx-R, cy-R, cx+R, cy+R], fill=INK)
    r1 = R*0.90; d.ellipse([cx-r1, cy-r1, cx+r1, cy+r1], fill=WHITE)
    r2 = R*0.70; d.ellipse([cx-r2, cy-r2, cx+r2, cy+r2], fill=INK)
    r3 = R*0.64
    for i in range(60, 0, -1):                     # degradado radial
        t = i/60; rr = r3*t
        c = tuple(int(a + (b-a)*t) for a, b in zip((150,225,255), (10,63,128)))
        ox, oy = -r3*0.18*(1-t), -r3*0.22*(1-t)
        d.ellipse([cx+ox-rr, cy+oy-rr, cx+ox+rr, cy+oy+rr], fill=c)
    h = r3*0.22; d.ellipse([cx-r3*0.38-h, cy-r3*0.42-h, cx-r3*0.38+h, cy-r3*0.42+h], fill=(232,248,255))

def leds(d, x, y, s):
    for i, c in enumerate([(255,75,75), (255,207,51), (69,224,127)]):
        cx = x + i*s*1.5; d.ellipse([cx-s/2, y-s/2, cx+s/2, y+s/2], fill=c, outline=INK, width=max(1, int(s*0.16)))

def draw(size, shape):
    S = size*4; im = Image.new("RGBA", (S, S), (0,0,0,0)); d = ImageDraw.Draw(im)
    if shape == "square": d.rounded_rectangle([S*0.04, S*0.04, S*0.96, S*0.96], radius=S*0.2, fill=RED)
    elif shape == "round": d.ellipse([S*0.02, S*0.02, S*0.98, S*0.98], fill=RED)
    if shape == "fg":   # capa frontal del ícono adaptable: zona segura de 66/108
        lens(d, S/2, S*0.53, S*0.24); leds(d, S*0.40, S*0.245, S*0.055)
    else:
        if shape == "square": d.rectangle([S*0.04, S*0.70, S*0.96, S*0.74], fill=RED_DK)
        lens(d, S/2, S*0.47 if shape == "square" else S/2, S*0.30); leds(d, S*0.355 if shape == "square" else S*0.39, S*0.14 if shape == "square" else S*0.17, S*0.07)
    return im.resize((size, size), Image.LANCZOS)

dens = {"mdpi":1, "hdpi":1.5, "xhdpi":2, "xxhdpi":3, "xxxhdpi":4}
for n, k in dens.items():
    p = os.path.join(OUT, f"mipmap-{n}"); os.makedirs(p, exist_ok=True)
    draw(int(48*k), "square").save(os.path.join(p, "ic_launcher.png"))
    draw(int(48*k), "round").save(os.path.join(p, "ic_launcher_round.png"))
    draw(int(108*k), "fg").save(os.path.join(p, "ic_launcher_foreground.png"))

def splash(w, h):
    im = Image.new("RGB", (w*2, h*2), RED); d = ImageDraw.Draw(im); m = min(w, h)*2
    lens(d, w, h, m*0.16); leds(d, w - m*0.06, h - m*0.24, m*0.035)
    return im.resize((w, h), Image.LANCZOS)
sizes = {"land-mdpi":(480,320), "land-hdpi":(800,480), "land-xhdpi":(1280,720), "land-xxhdpi":(1600,960), "land-xxxhdpi":(1920,1280),
         "port-mdpi":(320,480), "port-hdpi":(480,800), "port-xhdpi":(720,1280), "port-xxhdpi":(960,1600), "port-xxxhdpi":(1280,1920), "":(480,320)}
for n, (w, h) in sizes.items():
    p = os.path.join(OUT, "drawable" + ("-" + n if n else "")); os.makedirs(p, exist_ok=True)
    splash(w, h).save(os.path.join(p, "splash.png"), optimize=True)

os.makedirs(os.path.join(OUT, "values"), exist_ok=True)
open(os.path.join(OUT, "values", "ic_launcher_background.xml"), "w").write(
    '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#D42A3B</color>\n</resources>\n')
print("listo")
