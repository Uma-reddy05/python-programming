"""
Day 02 - operators, if-else and switch
Topic - operators, conditional statements and switch
Author - Uma
Date - 06-10-2026
"""

#----------------ARITHMETIC OPERATORS--------------
a = 5
b = 6
print("addition : ",a+b)
print("subtraction : ",a-b)
print("multiplication : ",a*b)
print("division : ",a/b)
print("floor division : ",a//b)
print("modulus : ",a%b)
print("exponent : ",a**b)

#---------------COMPARISION OPERATOR--------------
x = 10
y = 20
print("x==y : ",x==y)
print("x!=y : ",x!=y)
print("x>y : ",x>y)
print("x<y : ",x<y)
print("x>=y : ",x>=y)
print("x<=y : ",x<=y)

#----------------LOGICAL OPERATORS----------------
age = 20
is_student = True

print("age>=18 and is_student : ",age>=18 and is_student)
print("age<18 or is_student : ",age<18 or is_student)
print("not is_student : ",not is_student)

#-----------------ASSIGNMENT OPERATORS---------------
num = 10
num += 5
print("after += : ",num)

num -= 3
print("after -= : ",num)

num *= 2
print("after *= : ",num)

num //= 2
print("after //= : ",num)

#------------IF ELSE(even or odd)----------------
num = int(input("enter a number : "))
if num%2 == 0:
    print("the number is even")
else:
    print("the number is odd")

#----------------IF ELIF ELSE--------------------
marks = int(input("enter your marks : "))

if marks >= 90:
    print("grade A")
elif marks >= 75:
    print("grade B")
elif marks >= 60:
    print("grade C")
elif marks >= 40:
    print("grade D")
else:
    print("grade F")


#---------------------SWITCH CASE---------------------

print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

choice = int(input("enter a number(1-4) : "))

match choice:
    case 1:
        print("you selected addition")
    case 2:
        print("you selected subtraction")
    case 3:
        print("you selected multiplication")
    case 4:
        print("you selected division")
    case _:
        print("INVALID CHOICE")

#---------------MATCH CASE(even or odd)---------------
num = int(input("enter a number : ")) 
match num%2:
    case 0:
        print("number is even")
    case 1:
        print("number is odd")


"""
----------SAMPLE OUTPUT-------------

----------ARITHMETIC OPERATORS--------------
addition :  11
subtraction :  -1
multiplication :  30
division :  0.8333333333333334
floor division :  0
modulus :  5
exponent :  15625

---------------COMPARISION OPERATOR--------------
x==y :  False
x!=y :  True
x>y :  False
x<y :  True
x>=y :  False
x<=y :  True

----------------LOGICAL OPERATORS----------------
age>=18 and is_student :  True
age<18 or is_student :  True
not is_student :  False

-----------------ASSIGNMENT OPERATORS---------------
after += :  15
after -= :  12
after *= :  24
after //= :  12

----------IF ELSE(even or odd)----------------
enter a number : 3
the number is odd

---------------IF ELIF ELSE--------------------
enter your marks : 98
grade A

--------------------SWITCH CASE---------------------
1. addition
2. subtraction
3. multiplication
4. division
enter a number(1-4) : 2
you selected subtraction

--------------MATCH CASE(even or odd)---------------
enter a number : 4
number is even



---------------------WHAT I LEARNED------------------
1.arithmetic operators
2. comparision operator
3. logical operators
4. assignment operator
5. if-elif-else statements
6. match case statements
7. match can be used like switch case
8. the _ case works like default case

"""