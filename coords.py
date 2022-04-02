#!/usr/bin/env python3
import itertools as it
from PIL import Image, ImageDraw, ImageFont

xbounds = (20, 72)
ybounds = (679, 766)
xoffset = 2
yoffset = 2

scale = 32
grid = 1

orig = Image.open("tux.png")
new = orig.resize((orig.size[0]*scale, orig.size[1]*scale), resample=Image.NEAREST)
draw = ImageDraw.Draw(new)
font = ImageFont.truetype("LiberationMono-Bold.ttf", size=14)
for x, y in it.product(range(xbounds[1] - xbounds[0]), range(ybounds[1] - ybounds[0])):
    draw.text((xoffset + x*scale*grid, yoffset + y*scale*grid), f"{x + xbounds[0]}", font=font, fill="#666")
    draw.text((xoffset + x*scale*grid, yoffset + y*scale*grid + 14), f"{y + ybounds[0]}", font=font, fill="#666")

for x in range(xbounds[1] - xbounds[0]):
    draw.line((x*scale*grid, 0, x*scale*grid, ybounds[1]*scale*grid), fill="black")
for y in range(ybounds[1] - ybounds[0]):
    draw.line((0, y*scale*grid, xbounds[1]*scale*grid, y*scale*grid), fill="black")

new.save("tux_coords.png")
