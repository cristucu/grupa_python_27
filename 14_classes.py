print("=============Classes Course Start ============")


class Cat:
    # constructor
    def __init__(self, name, owner, temperament="Loving"):
        self.name = name
        self.owner = owner
        self.temperament = temperament

    def __str__(self):
        return f"Cat: name = {self.name}, owner is  {self.owner}, and temperament is {self.temperament}"

    def __repr__(self):
        return f"Cat('{self.name}', '{self.owner}', '{self.temperament}')"

    def speak(self):
        print(f'{self.name} says: "Meow"')

    def eat(self, food):
        print(f'{self.name} takes a bite out of {food}!')


cat1 = Cat("Shadow", "Mark")
cat2 = Cat("Spot", "John", temperament="Shy")

print(cat1)
cat2.name = "Ouroborus"
print(cat2)
cat2.speak()
cat2.eat(cat1.owner)

cats = [cat1, cat2]
print(cats)

stray_cats = [Cat("Shadow", "Mark", temperament="Loving"), Cat("Spot", "John")]

# cat1.name = "Shadow"
# cat2.name = "Spot"
# cat1.owner = "Mark"

print("========= Complex functionality with classes ==========")


class BankAccount:
    bank = "ING"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner} has {self.balance} Euro"

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance = self.balance - amount


acc1 = BankAccount("Adrian", 10)
# acc1.balance +=100
acc1.deposit(200)
acc1.withdraw(300)
print(acc1)

acc2 = BankAccount("Bob", 3000)
print(acc2)

acc1.bank = "BNR"
print(acc1.bank)
print(acc2.bank)


# creati o clasa Rectangle care are 2 atribute interne, x si y. Initiati-le din constructor
# creati doua metode, area() si perimeter() care calculeaza aria si perimetrul acelui Rectangle, si returneaza acea valoare., folosind formulele:
# # area: x * y
# # perimeter: 2 * x + 2 * y


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Rectangle has a width of {self.x}, and a height of {self.y}"

    def area(self):
        return f"Rectangle has an area of {self.x * self.y}"

    def perimeter(self):
        return f"Rectangle has a perimeter of  {2 * (self.x + self.y)}"


x = int(input("Enter the width (x): "))
y = int(input("Enter the height (y): "))

rect1 = Rectangle(x, y)
print(rect1)
print(rect1.area())
print(rect1.perimeter())

