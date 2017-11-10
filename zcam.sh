#!/bin/sh

cd /home/pi/Documents/BattleChess/

amixer cset numid=1 -- 90%
zbarcam -Sdisable -Scode128.enable --set code128.min-length=0 --prescale=320x240 --nodisplay --raw -q | ./BattleChess.py

