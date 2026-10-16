
from PIL import Image

img = Image.open("pink.png").convert("RGBA")
img = img.resize((48, 48), Image.Resampling.LANCZOS)

img.save(
    "pink.ico",
    format="ICO",
    sizes=[(48, 48)]
)

print("OK!")
