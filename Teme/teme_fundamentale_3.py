# Creati o variabila care contine o lista de siruri de caractere:
#
# "ERR-Value Error-ER:10"
#
# "INF-Program launch Info-CD:5"
#
# "WRN-Low memory:WR:11"
#
# Si alta variabila, cu alte siruri de caractere:
#
# "INF-Program exit-CD:14"
#
# "WRN-Low disk space-WR:99"
#
# "WRN-Bandwith reached:WR:87"
#
# Treceti prin toate sirurile de caractere, extrageti valorile de la ERR, INF, WRN, si creati urmatorul text formatat, din sirurile de caracter date, de exemplu:
#
#
# [ERROR]
# Mesaj: Value Error
# Cod: 10
#
# [INFO]
# Mesaj: Program launch Info
# Cod: 5
#
# [WARNING]
# Mesaj: Low memory
# Cod: 11
#
# Faceti asta pentru amandoua variabile, care contin acele siruri de caracter.

lista1 = [
    "ERR-Value Error-ER:10",
    "INF-Program launch Info-CD:5",
    "WRN-Low memory-WR:11"
]
lista2 = [
    "INF-Program exit-CD:14",
    "WRN-Low disk space-WR:99",
    "WRN-Bandwith reached-WR:87"
]

for mesaj in lista1 + lista2:
    parts = mesaj.split("-")

    if parts[0] == "ERR":
        print("[ERROR]")
    elif parts[0] == "INF":
        print("[INFO]")
    else:
        print("[WARNING]")

    print("Mesaj:", parts[1])
    print("Cod:", parts[2].split(":")[1])
    print()