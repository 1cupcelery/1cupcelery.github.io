
from PIL import Image

img = Image.open("green.png").convert("RGBA")
img = img.resize((48, 48), Image.Resampling.LANCZOS)

img.save(
    "green.ico",
    format="ICO",
    sizes=[(48, 48)]
)

print("OK!")
