"""
Day 11 - OOPS
Topic - inheritance, polymorphism and encapsulation
Author - Uma
Date - 15-10-2026
"""

# -------INHERITANCE--------

class Animal:
    def sound(self):
        print("animals make sound")

class Dog(Animal):
    def bark(self):
        print("dog barks")

dog = Dog()
dog.sound()
dog.bark()



#--------POLYMORPHISM--------
class Cat:
    def sound(self):
        print("cat meows")

class Bird:
    def sound(self):
        print("bird chirps")

cat = Cat()
bird = Bird()
cat.sound()
bird.sound()



#--------ENCAPSULATION-----------
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("balance : ", self.__balance)

account = BankAccount(1000)
account.show_balance


"""

------WHAT I LEARNED------
1. inheritance : a child class reuses a parent class
2. polymorphism : the same method name can behave differently
3. encapsulation : data and methods are grouped inside a class
4. __balance uses name mangling to discourage direct access
"""