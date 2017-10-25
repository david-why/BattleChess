#!/usr/bin/python

import os, time, pygame

pygame.mixer.init()
pygame.mixer.music.load('Start.wav')
pygame.mixer.music.play()
last_piece = None
while True:
  s = raw_input().split(':')
  print s
  if len(s) != 2 or s[0] != 'CODE-128': 
    continue
  piece = s[1]
  if last_piece:
    if last_time < time.time() - 3:
      last_piece = None
    else:
      if piece[0] == last_piece[0]:
        continue
      print piece, last_piece,
      if piece[1] == '0' or last_piece[1] == '0':
        print 'The end. ()()'
        wav = 'End.wav'
        if piece[1] == '0' and last_piece[1] == '0':
          break
      elif piece[1] == 'B' or last_piece[1] == 'B':
        print 'Draw. ()()'
        wav = 'Draw.wav' 
      elif piece[1] == 'A':
        if last_piece[1] != '1':
          print piece[0], 'win. ()()'
          wav = piece[0] + '.wav'
        else:
          print last_piece[0], 'win. ()()'
          wav = last_piece[0] + '.wav'
      elif last_piece[1] == 'A':
        if piece[1] != '1':
          print last_piece[0], 'win. ()()'
          wav = last_piece[0] + '.wav'
        else:
          print piece[0], 'win. ()()'
          wav = piece[0] + '.wav'
      elif last_piece[1] == '0' or piece[1] == '0':
        print 'The end. ()()'
        wav = 'End.wav'
      else:
        if piece[1] < last_piece[1]:
          print last_piece[0], 'win. ()()'
          wav = last_piece[0] + '.wav'
        elif piece[1] > last_piece[1]:
          print piece[0], 'win. ()()'
          wav = piece[0] + '.wav'
        else:
          print 'Draw. ()()'	
          wav = 'Draw.wav'
      pygame.mixer.music.load(wav)
      pygame.mixer.music.play()
  last_piece = piece
  last_time = time.time()

print 'Quit.'

