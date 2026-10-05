"""
Day 01 - python basics
Topic - variables,data types, input, output and f-strings
Author - Uma
Date - 05-10-2026
"""

#===========VARIABLES===========

name = "uma"
age = 17
height = 5.6
is_student = True

print("--------------VARIABLES----------")
print("name : ",name)
print("age : ",age)
print("height : ",height)
print("student : ",is_student)

#=============DATA TYPES==========

marks = 98  #int
percentage = 95.0   #float
college = "engineering college"    #str
passed = True    #bool

print("------------DATA TYPES-----------")
print(type(marks))
print(type(percentage))
print(type(college))
print(type(passed))


#===================INPUT===============
print("------------INPUT------------")
user_name = input("enter your name : ")
user_age = int(input("enter you age : "))
print("hello", user_name)
print("your age is", user_age)

#==============TYPE CONVERSION=============
print("----------TYPE CONVERSION-----------")
num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
sum = num1 + num2
print("sum is : ",sum)

#===============F-STRINGS=================
print("------------f-string------------")
name = input("enter your name : ")
age = int(input("enter your age : "))

print(f"hello {name}")
print(f"you are {age} years old")



"""

------------SAMPLE OUTPUT-----------

--------------VARIABLES----------
name :  uma
age :  17
height :  5.6
student :  True

------------DATA TYPES-----------
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>

------------INPUT------------
enter your name : Uma
enter you age : 17
hello Uma
your age is 17

----------TYPE CONVERSION-----------
enter first number : 2
enter second number : 8
sum is :  10

------------f-string------------
enter your name : Uma 
enter your age : 17
hello Uma
you are 17 years old

--------------WHAT I LEARNED----------------

1.variables - sorting values in python
2. data types - int,float,str,bool
3. print() - displaying output
4. input() - taking input from the user
5. type conversion - converting values using int() and float()
6. type() - checking the data type of value
7. f-string - formatting strings using f".....{variable}....."

"""