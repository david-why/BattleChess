#!/usr/bin/python

import os

n = 0
for color in 'RB':
  for piece in '98776655443332221110AAABB':
    os.system('barcode -b ' + color + piece + ' | convert -crop 78x26+0+703 -colors 2 - %04i.bmp' % n)
    n += 1

os.system('montage -border 1 -alpha Remove -tile 6 -geometry +0+0 *.bmp all.gif')
os.system('rm *.bmp')

