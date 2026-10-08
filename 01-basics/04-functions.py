"""
Day 04 - function in py
Author - Uma
Date - 08-10-2026
"""
# ------------CREATING A FUNCTION-----------
def greet():
    print("hello! welcome to functions in python.")
#--------CALLING A FUNCTION------------
greet()
greet()


#--------FUNCTION WITH MULTIPLE STATEMENTS--------
def welcome():
    print("welcome to python programming.")
    print("Let's start learning functions")

welcome()


#--------FUNCTION WITH CALCULATION-------
def calculation():
    a = 10
    b = 20
    sum = a + b
    print(f"sum is = {sum}")
calculation()


#----------FUNCTION WITH RETURN--------
def get_number():
    return 100
number = get_number()
print(f"number is = {number}")



#-------FUNCTION WITH RETURNING A CALCULATION------
def calculate_sum():
    a = 50
    b = 40
    return a + b
result = calculate_sum()
print(f"result = {result}")



#----------CALLING MULTIPLE FUNCTIONS--------
def first_function():
    print("this is the first function.")

def second_function():
    print("this is the second function")

first_function()
second_function()


"""
--------SAMPLE OUTPUT-------
hello! welcome to functions in python.
hello! welcome to functions in python.

welcome to python programming.
Let's start learning functions

sum is = 30

number is = 100

result = 90

this is the first function.
this is the second function
--------------WHAT I LEARNED---------------
1. function is a reusable block of code
2. functions are created using the def keyword
3. a function runs when it is called
4. a function can contain multiple statements
5. the return statement send the value back

"""