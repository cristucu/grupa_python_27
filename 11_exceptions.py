# terminalul are multiple stream uri de text pe care le printeaza si le afiseaza

# STDERR este stream-ul de erori

print("======Inceput de curs exceptii:=====")
lista1 = [9, 10, 11, 33]

print(lista1)
print(lista1[3])


try:
    vari = int(input("De care index esti curios?"))
    print(lista1[vari])
    # Exception that is thrown from int() conversion is caught as a ValueError.
    # exception that is thrown when accessing a non-existing index is caught, IndexError

except IndexError:
    print("We went too far, Captain!")
except ValueError:
    print("Yu have to write an intiger number!")
except BaseException:
    print("You shall not pass!")
except BaseException:
    #DON'T DO THIS!
    pass

# exception bubble-up

print("=====Sfarsit de curs exceptii:=====")

var2 = 10

if var2 >5:
    raise Exception("My variable is to high!")