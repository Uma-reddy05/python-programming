"""
day 12 - decorators and generatora
Auhor - Uma
Date - 16-10-2026
"""

#---------DECORATORS-------
def my_decorator(func):
    def wrapper():
        print("before function")
        func()
        print("after function")
    return wrapper

@my_decorator
def greet():
    print("hello, python")

greet()


#-------GENERATORS--------
def count_nums():
    yield 1
    yield 2
    yield 3

for number in count_nums():
    print(number)


"""
--------WHAT I LEARNED-------

1.  a decorator adds behavior to a function
2. @my_decorator applies the decorator to greet()
3. a generator uses yield to produce values
4. generators produce values one at a time

"""