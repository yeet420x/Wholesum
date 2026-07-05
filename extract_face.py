"""Crop the human face (no horns) out of assets/blackbull.png.

Usage:
    python extract_face.py [left top right bottom]

Outputs:
    assets/wholesum-face.png       - rectangular crop, 2x upscaled
    assets/wholesum-face-oval.png  - feathered oval on transparent bg, 2x upscaled
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ASSETS = Path(__file__).parent / "assets"
SRC = ASSETS / "blackbull.png"

# default box tuned for the 512x512 Black Bull artwork; override via CLI args
BOX = (205, 95, 330, 300)
if len(sys.argv) == 5:
    BOX = tuple(int(v) for v in sys.argv[1:5])

if not SRC.exists():
    sys.exit(f"missing {SRC} - save the bull image from chat to this path first")

img = Image.open(SRC).convert("RGB")
scale = img.width / 512  # coords are in 512-space; rescale if source differs
box = tuple(round(v * scale) for v in BOX)

face = img.crop(box)
face = face.resize((face.width * 2, face.height * 2), Image.LANCZOS)
face.save(ASSETS / "wholesum-face.png")

# feathered oval mask -> transparent background
mask = Image.new("L", face.size, 0)
draw = ImageDraw.Draw(mask)
inset = round(min(face.size) * 0.04)
draw.ellipse((inset, inset, face.width - inset, face.height - inset), fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(radius=min(face.size) * 0.03))

oval = face.convert("RGBA")
oval.putalpha(mask)
oval.save(ASSETS / "wholesum-face-oval.png")

print(f"cropped box {box} from {SRC.name} ({img.width}x{img.height})")
print(f"wrote {ASSETS / 'wholesum-face.png'} and {ASSETS / 'wholesum-face-oval.png'}")
