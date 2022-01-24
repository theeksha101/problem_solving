# Python program to demonstrate
# duck typing


class Bird:
    def fly(self):
        print("fly with wings")

    def eat(self):
        print("a bird eats")


class Airplane:
    def fly(self):
        print("fly with fuel")


class Fish:
    def swim(self):
        print("fish swim in sea")

    def eat(self):
        print("a fish eats")

    def __len__(self, x):
        return len(x)

# Attributes having same name are
# considered as duck typing
for obj in Bird(), Airplane(), Fish():
    obj.fly()
Bird()
Airplane()
Fish()
