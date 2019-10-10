imie="szymon jagaczewski"
odwrocone=""
dlugosc=len(imie)
print(imie)
for i in range(dlugosc,0,-1):
  odwrocone=odwrocone+(imie[i-1])
print(odwrocone)