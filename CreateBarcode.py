#!/usr/bin/python

import os

n = 0
for color in 'RB':
  for piece in '98776655443332221110AAABB':
    os.system('barcode -b ' + color + piece + ' | convert -density 225x225 -alpha Remove +antialias -crop 248x73+0+2180 - %04i.bmp' % n)
    n += 1

os.system('montage -border 1 -bordercolor yellow -tile 6 -geometry +0+0 -density 300 -units PixelsPerInch *.bmp all.tif')
os.system('rm *.bmp')

