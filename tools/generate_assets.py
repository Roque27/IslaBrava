"""Generate the install icon and social preview for Isla Brava."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
NAVY = "#102432"
LIME = "#c1f777"


def font(size, bold=True):
    candidates = (
        [Path("C:/Windows/Fonts/arialbd.ttf"), Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")]
        if bold
        else [Path("C:/Windows/Fonts/arial.ttf"), Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")]
    )
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def icon(size):
    scale = 4
    side = size * scale
    image = Image.new("RGB", (side, side), NAVY)
    draw = ImageDraw.Draw(image)
    p = lambda x, y: (round(x * side), round(y * side))
    draw.rounded_rectangle((0, 0, side - 1, side - 1), radius=side // 5, fill=NAVY)
    draw.ellipse((side * .12, side * .11, side * .88, side * .87), outline="#2e6471", width=max(1, side // 45))
    draw.polygon([p(.19, .46), p(.50, .27), p(.81, .46), p(.50, .65)], fill=LIME)
    draw.polygon([p(.19, .46), p(.50, .65), p(.50, .78), p(.19, .59)], fill="#468850")
    draw.polygon([p(.50, .65), p(.81, .46), p(.81, .59), p(.50, .78)], fill="#2d6549")
    draw.polygon([p(.35, .48), p(.50, .39), p(.65, .48), p(.50, .57)], fill="#d8c994")
    draw.polygon([p(.50, .34), p(.58, .39), p(.50, .44), p(.42, .39)], fill="#79b7ff")
    draw.polygon([p(.42, .39), p(.50, .44), p(.50, .54), p(.42, .49)], fill="#4e83e1")
    draw.polygon([p(.50, .44), p(.58, .39), p(.58, .49), p(.50, .54)], fill="#315aa8")
    draw.rectangle((p(.472, .395), p(.488, .413)), fill="#112836")
    draw.rectangle((p(.518, .395), p(.534, .413)), fill="#112836")
    draw.line([p(.76, .25), p(.83, .19), p(.88, .24)], fill="#f9f8e8", width=max(2, side // 55), joint="curve")
    return image.resize((size, size), Image.Resampling.LANCZOS)


for size in (32, 180, 192, 512):
    icon(size).save(ROOT / f"icon-{size}.png", optimize=True)


width, height = 1200, 630
image = Image.new("RGB", (width, height), NAVY)
draw = ImageDraw.Draw(image)
for y in range(height):
    fraction = y / height
    color = (round(16 + 40 * fraction), round(36 + 105 * fraction), round(50 + 102 * fraction))
    draw.line((0, y, width, y), fill=color)
draw.ellipse((690, 55, 1260, 625), fill="#86c2c3", outline="#a9dcd4", width=3)
draw.polygon([(760, 358), (934, 254), (1108, 358), (934, 466)], fill="#bdf074")
draw.polygon([(760, 358), (934, 466), (934, 538), (760, 430)], fill="#4a8955")
draw.polygon([(934, 466), (1108, 358), (1108, 430), (934, 538)], fill="#2e6950")
draw.polygon([(866, 355), (934, 314), (1002, 355), (934, 396)], fill="#d9c99a")
draw.polygon([(902, 306), (934, 288), (966, 306), (934, 325)], fill="#78b8ff")
draw.polygon([(902, 306), (934, 325), (934, 365), (902, 344)], fill="#568ade")
draw.polygon([(934, 325), (966, 306), (966, 344), (934, 365)], fill="#325d9f")
draw.rectangle((914, 315, 923, 321), fill="#122938")
draw.rectangle((944, 315, 953, 321), fill="#122938")
draw.rounded_rectangle((62, 66, 208, 212), radius=30, fill=NAVY, outline=LIME, width=4)
image.paste(icon(112), (79, 83))
draw.text((62, 248), "ISLA", fill="#f9f8e8", font=font(115), stroke_width=0)
draw.text((62, 352), "BRAVA", fill=LIME, font=font(115), stroke_width=0)
draw.rounded_rectangle((62, 521, 613, 583), radius=23, fill="#183847")
draw.text((87, 534), "EXPLORÁ · COMBATÍ · VENCÉ AL GÓLEM", fill="#f9f8e8", font=font(22), stroke_width=0)
image.save(ROOT / "social-preview.png", optimize=True)
