"""
Day 10 - classes and objects
Author - Uma
Date - 14-10-2026
"""

#------CLASS AND OBJECT--------
class student:
    def display(self):
        print("hello I'm a student")
        print("I'm learning python")

student1 = student()  # creating an object

student1.display()  # calling the method


#-------CLASS AND OBJECT---------
class student:
    def display(self):
        print("I am a CSE student")

student1 = student()
student1.display()


#-------CONSTRUCTOR------------
class message():
    def __init__(self):
        print("object created")
student1 = message()
student2 = message()


#------CONSTRUCTOR WITH DATA----------
class StudentDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("name : ",self.name)
        print("age : ",self.age)

student2 = StudentDetails("Uma", 17)
student3 = StudentDetails("Tanushree", 18)

student2.display()
print("--------")
student3.display()

"""
-------SAMPLE OUTPUT-------
hello I'm a student
I'm learning python

I am a CSE student

object created
object created

name :  Uma
age :  17
--------
name :  Tanushree
age :  18


-------WHAT I LEARNED---------
1. a class is a blueprint foe objects
2. an object is an instance of class
3. a method is a function inside a class
4. __init__() intializes object data
5. self refers to the current object
6. one class can create multiple objects

"""