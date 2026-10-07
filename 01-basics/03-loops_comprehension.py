"""
Day 03 - loops and comprehension
Topic - for loops, while loop, break, continue, and list comprehension
Author - Uma
Date - 07-10-2026
"""
#------------FOR LOOP-----------
print("------------FOR LOOP WITH LIST----------")
fruits = ["apple","banana","mango","orange"]
for fruit in fruits:
    print(fruit)

print("---------FOR LOOP WITH RANGE----------")
for i in range(1,11):
    print(i)

print("-----------MULTIPLICATION TABLE-----------")
num = int(input("enter a number : "))
for i in range(1,11):
    print(f"{num}x{i} = {num*i}")


#---------------WHILE LOOP------------------
print("------WHILE LOOP-----------")
count = 1
while count <= 5:
    print(count)
    count += 1

#--------BREAK----------
print("----------BREAK-------")
for i in range(1,11):
    if i==6:
        break
    print(i)

#---------------CONTINUE------------
print("----------CONTINUE----------")
for i in range(1,11):
    if i==6:
        continue
    print(i)

#---------------NESTED LOOPS----------------
print("-------------NESTED LOOPS------------")
for i in range(1,4):
    for j in range(1,4):
        print(f"i = {i},j = {j}")


#----------------EVEN NUMBERS USING FOR LOOP--------------
print("---------EVEN NUMERS---------")
for i in range(1,21):
    if i%2 == 0:
        print(i)

#---------------LIST COMPREHENSION--------------
print("---------LIST COMPREHENSION----------")
nums = [1,2,3,4,5]
squares = [num**2 for num in nums]
print(f"numbers : {nums}")
print(f"squares : {squares}")

#------------LIST COMPREHENSION WITH CONDITION------------
print("-------------LIST COMPREHENSION WITH CONDITION------------")
nums = range(1,11)
even_nums = [num for num in nums if num%2 == 0]
print(f"even numbers : {even_nums}")

#----------SQUARES OF EVEN NUMBERS-------------
print("----------SQUARES OF EVEN NUMBERS------------")
nums = range(1,11)
even_square = [num**2 for num in nums if num%2 == 0]
print(f"even_squares : {even_square}")

"""
-------------SAMPLE OUTPUT--------------

------------FOR LOOP WITH LIST----------
apple
banana
mango
orange

---------FOR LOOP WITH RANGE----------
1
2
3
4
5
6
7
8
9
10


-----------MULTIPLICATION TABLE-----------
enter a number : 5
5x1 = 5
5x2 = 10
5x3 = 15
5x4 = 20
5x5 = 25
5x6 = 30
5x7 = 35
5x8 = 40
5x9 = 45
5x10 = 50

------WHILE LOOP-----------
1
2
3
4
5

----------BREAK-------
1
2
3
4
5

----------CONTINUE----------
1
2
3
4
5
7
8
9
10

-------------NESTED LOOPS------------
i = 1,j = 1
i = 1,j = 2
i = 1,j = 3
i = 2,j = 1
i = 2,j = 2
i = 2,j = 3
i = 3,j = 1
i = 3,j = 2
i = 3,j = 3


---------EVEN NUMERS---------
2
4
6
8
10
12
14
16
18
20


---------LIST COMPREHENSION----------
numbers : [1, 2, 3, 4, 5]
squares : [1, 4, 9, 16, 25]


-------------LIST COMPREHENSION WITH CONDITION------------
even numbers : [2, 4, 6, 8, 10]


----------SQUARES OF EVEN NUMBERS------------
even_squares : [4, 16, 36, 64, 100]



------------WHAT I LEARNED------------
1. for loop
2. while loop
3. range()
4. looping through lists
5. break
6. continue
7. nested loops
8. list comprehension
9. list comprehension with condition

list comprehension syntax:
[expression for item in iterable]
with condition:
[expression for item in iterable if condition]

"""