#!/bin/sh

cd /home/pi/Documents/BattleChess/

amixer cset numid=1 -- 90%
zbarcam -Sdisable -Scode128.enable --prescale=320x320 --nodisplay --raw -q | ( ./BattleChess.py ; sudo poweroff )

