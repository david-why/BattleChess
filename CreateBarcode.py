#!/usr/bin/python

import os

n = 0
for color in 'RB':
  for piece in '98776655443332221110AAABB':
    os.system('barcode -b ' + color + piece + ' > b.ps')
    os.system('convert -crop 60x22+8+703 -background white -colors 2 -resize 300%% -filter Point b.ps %04i.png' % n)
    n += 1

os.system('montage -border 1 -bordercolor yellow -extent 248x94 -tile 4x13 -gravity center -geometry +0+0 -density 300 -units PixelsPerInch *.png all.tif')
os.system('rm b.ps *.png')

