import os

# operating system interaction

# print(os.listdir())
# if os.path.exists("manage.py"):
#     print("Avem fisierul manage.py in acest folder")
#     print(os.path.getsize("manage.py"))
# else:
#      print("File not found")


# os.listdir() returneaza o lista de nume de foldere si fisiere
# os.path.isfile(fisier) returneaza True daca "fisier" este un fisier
# os.path.getsize(fisier) returneaza marimea fisierului in bytes

#Ex: Creati o functie care trece prin fisierele din folderul curent si returneaza marimea totala a fisierelor.


def total_files_size():
    total = 0

    for nume in os.listdir():
        if os.path.isfile(nume):
            total += os.path.getsize(nume)
    return total
print(total_files_size())
