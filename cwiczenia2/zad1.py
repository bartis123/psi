def zadanie1(a_list, b_list):
    tmp = []
    for i in range(len(a_list)):
        if not i % 2:
            tmp.append(a_list[i])
    for i in range(len(b_list)):
        if i % 2:
            tmp.append(b_list[i])
    return tmp

a_list=[1, 2, 3, 4, 5]
b_list=[6, 7, 8, 9, 10]

list3=zadanie1(a_list,b_list)
print(list3)