#functii

def greet():
    print("Hello")
print("bau")
greet()


def add(a, b):
    return(a + b)

print(add(5, 10))
print(add(60, 90))
print(add(100, 333))

def mul(a, b):
    return(a * b)

var1 = mul(5, 15)
add(var1, 35)

# creati sub care cade a - b, div care imparte a  b, si pow care ridica a**

def sub(a, b):
    return a - b

print(sub(34, 15))

def divs(a, b):
    return(a / b)

print(divs(14, 3))

def power(a, b):
    return(a ** b)

print(power(2, 3))

rezultat = sub(6, mul(4, 10))
print(rezultat)

# 5+4*8**2

rezultat1 = add(5, mul(4, pow(8, 2)))
print(rezultat1)

# 5 + 3**2 *3

rezultat2 = add(5, mul(pow(3, 2), 3))
print(rezultat2)

def speak(word="woof!"):
    print(word)

speak()
speak("Meow!")

def drive(car_model, max_speed=130):
    print(f"{car_model} is driving at a max speed of {max_speed}.")

drive("Audi")
drive("Mazda", "red")

# typed functions
# a % b

def modulo(a: int, b: int) -> int:
    """
    Returns the remainder of division between a and b.
    :param a: the number to divide
    :param b: the number to divide by
    :return: remainder of division between a and b
    """
    return a % b

print(modulo(13, 5))


nr = [10, 11, 21, 5, -1, 20, 3]

def even_numbers(list1):
    res = []
    for n in list1:
        if n % 2 == 0:
            print(f"am gasit numar par: {n}")
            res.append(n)
    return res

result = even_numbers(nr)
print(result)

var1 = [
    "ERR-Value Error-ER:10",
    "INF-Program launch Info-CD:5",
    "WRN-Low memory-WR:11"
]

var2 = [
     "ERR-Value Error-ER:10",
     "INF-Program launch Info-CD:5",
     "WRN-Low memory-WR:11"
 ]

#
# for s in var2:
#     print(f"Tip mesaj: {s.split("-")[0]}")
#     print(f"Mesaj: {s.split("-")[1]}")
#     print(s.split("-")[2])


def format_logs(param1):
    chunks =[]
    for s in param1:
        if s.split("-")[0] == "ERR":
            chunks.append("ERROR")
        elif s.split("-")[0] == "WRN":
            chunks.append("WARNING")
        elif s.split("-")[0] == "INF":
            chunks.append("INF")
        else:
            chunks.append(s.split("-")[0])

        chunks.append(f"Mesaj: {s.split("-")[1]}")

        chunks.append(f"Cod: {s.split("-")[2].split("-")[1]}\n")

    str_result = "\n".join(chunks)
    return str_result
result = format_logs(var2)
print(result)