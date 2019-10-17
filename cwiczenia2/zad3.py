def zad3(letter, text):
    tmp=""
    for i in range(len(text)):
        if text[i] is not letter:
            tmp=tmp+(text[i])
    return tmp

print(zad3('a',"Szymon Jagaczewski"))
