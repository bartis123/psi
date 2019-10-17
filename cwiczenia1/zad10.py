tab=[1,2,3,4,5,2,2,3,2,6,7,2,3,2]
tmp=[]
for i in range(len(tab)):
    if tab[i] is not 2:
        tmp.append(tab[i])
print(tmp)