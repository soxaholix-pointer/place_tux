#!/usr/bin/env python3
import itertools as it
from PIL import Image, ImageDraw, ImageFont
import argparse


def main():
    parser = argparse.ArgumentParser(description='Process input')

    parser.add_argument("--input", "-i", help="Input file")
    parser.add_argument("--output", "-o", help="Output file")

    parser.add_argument("-x1", help="Top left X")
    parser.add_argument("-y1", help="Top left Y")
    parser.add_argument("-x2", help="Bottom right X")
    parser.add_argument("-y2", help="Bottom right Y")

    args = parser.parse_args()

    print(f"Creating an enlarged version of {args.input} with coordinates and saving it to {args.output}")

    xbounds = (int(args.x1), int(args.x2))
    ybounds = (int(args.y1), int(args.y2))

    build_image(
        input_path=args.input,
        output_path=args.output,
        xbounds=xbounds,
        ybounds=ybounds,
    )

def build_image(
    input_path: str,
    output_path: str,
    xbounds: tuple[int, int], 
    ybounds: tuple[int, int],
    text_offset: tuple[int, int] = (2, 2),
    scale: int = 32,
    grid: int = 1,
):
    with Image.open(input_path) as orig:
        new = orig.resize((orig.size[0]*scale, orig.size[1]*scale), resample=Image.NEAREST)
        draw = ImageDraw.Draw(new)
        font = ImageFont.truetype("LiberationMono-Bold.ttf", size=14)
        for x, y in it.product(range(xbounds[1] - xbounds[0]), range(ybounds[1] - ybounds[0])):
            color = orig.getpixel((x,y))
            if color[3] != 0: #not transparent
                if color[0] * 0.299 + color[1] * 0.587 + color[2] * 0.114 > 186:
                    textcolor = "black"
                else:
                    textcolor = "white"

                draw.text((text_offset[0] + x*scale*grid, text_offset[1] + y*scale*grid), f"{x + xbounds[0]}", font=font, fill=textcolor)
                draw.text((text_offset[0] + x*scale*grid, text_offset[1] + y*scale*grid + 14), f"{y + ybounds[0]}", font=font, fill=textcolor)

        for x in range(xbounds[1] - xbounds[0]):
            draw.line((x*scale*grid, 0, x*scale*grid, ybounds[1]*scale*grid), fill="black")
        for y in range(ybounds[1] - ybounds[0]):
            draw.line((0, y*scale*grid, xbounds[1]*scale*grid, y*scale*grid), fill="black")

        new.save(output_path)
    
if __name__ == "__main__":
    main()
