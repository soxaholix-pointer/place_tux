#!/bin/env python3

import matplotlib.pyplot as plt
import numpy
import sys

raw_fname = sys.argv[1]
out_fname = sys.argv[2]

img = plt.imread(raw_fname)

mask = numpy.invert(numpy.all(img==0, axis=-1))
img[mask] = (0,0,0,1)

plt.imsave(out_fname, img, dpi=100, format="png")