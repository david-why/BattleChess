#!/usr/bin/python
# written by David Wang, 2017

#!/usr/bin/python

import os, time, pygame

pygame.mixer.init()
pygame.mixer.music.load('Start.wav')
pygame.mixer.music.play()
last_time = 0
while True:
  piece = raw_input()
  print piece
  if len(piece) != 2:
    continue
  if time.time() - last_time < 3: 
    if piece[0] != last_piece[0]:
      if piece[1] == '0' and last_piece[1] == '0':
        break
      if piece[1] == '0' or last_piece[1] == '0':
        voice = 'End'
      elif piece[1] == 'B' or last_piece[1] == 'B':
        voice = 'Draw' 
      elif piece[1] == 'A':
        if last_piece[1] != '1':
          voice = piece[0]
        else:
          voice = last_piece[0]
      elif last_piece[1] == 'A':
        if piece[1] != '1':
          voice = last_piece[0]
        else:
          voice = piece[0]
      else:
        if piece[1] < last_piece[1]:
          voice = last_piece[0]
        elif piece[1] > last_piece[1]:
          voice = piece[0]
        else:
          voice = 'Draw'
      pygame.mixer.music.load(voice + '.wav')
      pygame.mixer.music.play()
  last_piece = piece
  last_time = time.time()
os.system('poweroff')

