"""
Day 8 - exception handling and modules
Topics - try,except, else, finally, raise, import
Author - Uma
Date - 12-10-2026
"""

#---------BASIC EXCEPTION HANDLING-------
try:
    number = int(input("enter a number : "))
except ValueError:
    print("Error : please ener a valid integer")


#-------HANDLING ZERO DIVISION-----------
try:
    a = int(input("enter the first number : "))
    b = int(input("enter the secind number : "))
    result = a/b
    print("result : ", result)

except ValueError:
    print("error : enter numbers only")
except ZeroDivisionError:
    print("Error : cannot divide by zero")


#----------ELSE BLOCK--------
try:
    num = int(input("enter a number : "))
except ValueError:
    print("invalid input")
else:
    print("you entered : ",num)


#----------FINAL BLOCK--------
try:
    print("inside the try block")
except ValueError:
    print("an error occcurred")
finally:
    print("finally block executed")


#--------HANDLING MULTIPLE EXCEPTIONS---------
try:
    numbers = [10, 20, 30]
    index = int(input("enter an index(0-2) : "))
    print(numbers[index])
except ValueError:
    print("please enter an integer")
except IndexError:
    print("index is out of range")



#-------RAISING AN EXCEPTION---------
try:
    age = int(input("enter your age : "))
    if age<0:
        raise ValueError("age cannot be negative ")
    print("age : ",age)

except ValueError as error:
    print("error : ",error)


#------IMPORTING A BUILT-IN MODULE-------
import math
print("square root : ",math.sqrt(9))
print("factorial : ",math.factorial(5))
print("value of pi : ",math.pi)


#-------IMPORTING SPECIFIC FUNCTIONS----------
from math import sqrt, pow
print("square root of 49 : ",sqrt(49))
print("2 raised to 3 : ",pow(2,3))


#--------USING THE RANDOM MODULE------
import random
fruits = ["apple", "banana", "mango"]
print("random fruit : ", random.choice(fruits))


#---------USING THE DATETIME MODULE------
import datetime
today = datetime.date.today()
print("todays date : ",today)


