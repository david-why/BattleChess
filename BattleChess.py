#!/usr/bin/python
# written by David Wang

from time import time
from pygame.mixer import init, Sound

init()
Sound('Start.wav').play()
last_time = 0
while True:
  piece = raw_input()
  if len(piece) != 2:
    continue
  if time() - last_time < 3: 
    if piece[0] != last_piece[0]:
      if piece[1] == '0' and last_piece[1] == '0':
        break
      if piece[1] == '0' or last_piece[1] == '0':
        voice = 'End'
      elif piece[1] == 'B' or last_piece[1] == 'B':
        voice = 'Draw' 
      elif piece[1] == 'A':
        if last_piece[1] == '1':
          voice = last_piece[0]
        else:
          voice = piece[0]
      elif last_piece[1] == 'A':
        if piece[1] == '1':
          voice = piece[0]
        else:
          voice = last_piece[0]
      else:
        if piece[1] < last_piece[1]:
          voice = last_piece[0]
        elif piece[1] > last_piece[1]:
          voice = piece[0]
        else:
          voice = 'Draw'
      Sound(voice + '.wav').play()
  last_piece = piece
  last_time = time()

