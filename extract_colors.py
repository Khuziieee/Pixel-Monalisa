from PIL import Image
import json

img= Image.open("Mona lisa.png")
img= img.resize((96,128), Image.Resampling.NEAREST)
img= img.convert("RGB")

pixels = []
for y in range(img.height):
    for x in range(img.width):
        r,g,b = img.getpixel((x,y))
        pixels.append(f"rgb({r},{g},{b})")

with open("colors.json","w") as f:
    json.dump(pixels,f)
print("all done")

with open("colors.json") as f:
    colors = json.load(f)
cols = 96
rows = 128
size = 4

html = [
    "<!DOCTYPE html>",
    "<html>",
    "<head>",
    "<title>CSS Grid Mona Lisa</title>",
    "<style>",
    f"body{{background:#000000;display:flex;justify-content:center;align-items:center;min-height:100vh;}}",
    f".mona-grid{{display:grid;grid-template-columns:repeat({cols},{size}px);grid-auto-rows:{size}px;}}",
    f".pixel{{width:{size}px;height:{size}px;}}",
    "</style>",
    "</head>",
    "<body>",
    "<div class='mona-grid'>"
]

for c in colors:
    html.append(f"<div class='pixel' style='background:{c}'></div>")

html += ["</div>", "</body>", "</html>"]

with open("mona.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html))

print("Open it in your browser.")