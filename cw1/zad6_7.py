# Zadanie 6
lista_cala = list(range(1,11))
print(lista_cala)
lista1 = lista_cala[5:]
lista_cala = lista_cala[:5]
print(lista1)
print(lista_cala)


# Zadanie 7

lista_cala = lista_cala + lista1
print(lista_cala)
lista_cala.insert(0,0)
print(lista_cala)
lista_cala_kopia= lista_cala.copy()
lista_cala_kopia.sort(reverse=True)
print(lista_cala_kopia)