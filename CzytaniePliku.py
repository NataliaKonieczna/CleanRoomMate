#!/usr/bin/env python
#wczytanie pliku do programu
#ze ścieżki bezwzględnej (np. ’/home/std/praca’)
plik=open("nazwa pliku")
try:
    tekst=plik.read()
finally:
    plik.close()
    
print tekst

#pobieranie wiersza z pliku
import linecache
wiersz=linecache.getline("nazwa pliku",NUMER_WIERSZA)
print wiersz
