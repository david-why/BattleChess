#!/usr/bin/python

import os

n = 0
for color in 'RB':
  for piece in '98776655443332221110AAABB':
    os.system('barcode -b ' + color + piece + ' > b.ps')
    os.system('convert -crop 60x22+8+703 -background white -colors 2 -resize 300%% -filter Point b.ps %04i.png' % n)
    #qrcode.make(color + piece, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 4, border = 0).save('%04i.png' % n)
    n += 1

os.system('rm b.ps')

