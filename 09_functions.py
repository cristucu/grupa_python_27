import random
from lib.core import even_numbers, is_even

# print(random.sample(range(0, 1000) , 15))

random_numbers = [978, 91, 256, 616, 187, 958, 358, 645, 482, 705, 22, 325, 94, 813, 350]

#filter(), map(), reduce(), zip()

# lambda functions:

def mult_2(param1):
    return param1 * 2



print(mult_2(10))

#efemera
square = lambda x: x * 2
print(square(10))

# filtrati toate numerele multiplu de 7

rezultat = list(filter(lambda x: x % 2 == 0, random_numbers))
print(rezultat)

rezultat2 = list(filter(is_even, random_numbers))