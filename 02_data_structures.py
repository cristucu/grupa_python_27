# Liste

list1 = [4, 5, 10, 20, 30, 100, 500, 999, 1000]
#        0  1   2   3   4    5    6    7     8

print(list1[0])
print(list1[-1])

index = len(list1) // 2
print (list1[index])


list2 = [0, 1, 2, 50, 100, 100, 100, 100, 2, 2, 2, 9, 10, 99]
print(list2)
#putem schimba un element din lista folosind [] si punand indexul elementului in ele
list2[3] = 100

print(list2)

#Dictionare

#unordered list:
persoana = {
    "key": "valoare",
    "nume": "Alex",
    "varsta": 30,
    "cetatean_roman": True,
    "bolnav": False,
    "greutate": 75.7,
}

#seturi:
#cutie de bomboane, toate diferite.

elemset = {3, 6, 10, 9, 8, 100, 3}
print(elemset)

list2 = [0, 1, 2, 50, 100, 100, 100, 100, 2, 2, 2, 9, 10, 99]
list2_no_duplicates = set(list2)
print(list2_no_duplicates)

#tuple, like a list, but imutable

coordinates = (0, 10)
coordinates3d = (0, 15, -5)

#Metode:


# catel = "Spot"
# catel.latra("cioara")
# catel.mananca("peste")
# catel.miroase("adrian")
# catel.musca("adrian")

#obiecte.actiune/functie/metoda (parametri)

lista5 = [7, 8, 100, 99]
lista5.append(-50)
print(lista5)
lista5.pop(1)
print(lista5)
lista5.reverse()
print(lista5)

set2 = {7, 6, 8, 8, 10, 90, 100}
set2.add(-5)
set2.remove(90)

#remove
print(set2)

#chei de dictionare

dict_2 = {
    "key": "value",
    "number": "one",
    3.14: "PI",
    True: False,
    (2,3): "coordinates",
    "bizar": {
        "number": "two",
    }
}
print(dict_2)