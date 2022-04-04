#!/bin/env python3

from PIL import Image
import sys

in_fname = sys.argv[1]
out_fname = sys.argv[2]

with Image.open(in_fname) as tux_image:
    tux_image.resize((tux_image.width * 100, tux_image.height * 100), resample=Image.NEAREST).save(out_fname)
