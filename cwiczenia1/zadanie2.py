tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie="szymon"
nazwisko="jagaczewski"
liczba1=0
liczba2=0
for i in tekst:
    if i==imie[2]:
        liczba1=liczba1+1
    if i==nazwisko[3]:
        liczba2=liczba2+1

print("W tekscie jest %i liter %c oraz %i liter %c" % (liczba1,imie[2],liczba2,imie[3]))


