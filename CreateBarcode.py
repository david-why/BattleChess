#!/usr/bin/python

import os

n = 0
for color in 'RB':
  for piece in '98776655443332221110AAABB':
    os.system('barcode -b ' + color + piece + ' > b.ps')
    os.system('convert -crop 60x22+8+703 -colors 2 b.ps %04i.bmp' % n)
    n += 1

os.system('montage -border 1 -extent 78x28 -tile 6x9 -gravity center -geometry +0+0 *.bmp all.gif')
os.system('rm b.ps *.bmp')

