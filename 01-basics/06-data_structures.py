"""
Day 06 - python data structures
Topic - list, tuple, set and their operations
Author - Uma
Date - 10-10-2026
"""
#----------LIST - CREATION AND ACCESS----------
numbers = [10, 20, 30, 40]
print("original list : ", numbers)
print("first element : ",numbers[0])
print("last element : ",numbers[-1])
print("sliced element : ",numbers[1:4])
print("list length : ",len(numbers))

#--------LIST - ADDING ELEMENTS----------
numbers.append(50)    # add one element at the end
numbers.insert(1,15)   # Insert at a specific index
numbers.extend([60,70])    # Add multiple elements
print("after adding : ",numbers)

#--------LIST - REMOVING ELEMENTS---------
numbers.remove(20)    # Remove the first matching value
last_item = numbers.pop()   # Remove and return last element
del numbers[0]    # Delete element at index 0
print("atfer removing : ",numbers)
print("popped item : ",last_item)

#----------LIST - SEARCHING,COUNTING AND SORTING--------
values = [40, 10, 30, 10, 20]
print("count of 10 : ",values.count(10))
print("index of 30 : ",values.index(30))
print("10 exsists : ", 10 in values)

values.sort()
print("ascending : ",values)

values.sort(reverse=True)
print("descending : ", values)

values.reverse()
print("reversed : ",values)

copied_values = values.copy()
print("copied values : ",copied_values)

values.clear()
print("cleared list : ",values)


#---------TUPLE - CREATION AND ACCESS--------
fruits = ("apple", "banana", "mango", "banana")
print("original tuple : ",fruits)
print("first fruit : ",fruits[0])
print("last fruit : ",fruits[-1])
print("sliced tuple : ",fruits[1:3])
print("tuple length : ",len(fruits))

#---------TUPLE - COUNT, INDEX AND MEMBERSHIP-------
print("banana count : ",fruits.count("banana"))
print("mango index : ",fruits.index("mango"))
print("apple exists : ", "apple" in fruits)
fruit_list = list(fruits)
fruit_list.append("orange")
fruits = tuple(fruit_list)
print("tuple after adding orange : ",fruits)

#--------TUPLE - INPACKING AND CONCATENATION---------
person = ("uma", 17, "CSE")
name, age, branch = person

print("name : ",name)
print("age : ",age)
print("branch : ",branch)

combined = (1, 2) + (3, 4)
print("combined tuple : ",combined)

repeated = "hi"*5
print("repeated tuple : ",repeated)

#---------SET - CREATION AND BASIC OPERATIONS----------
number_set = {10, 20, 30, 20, 40}
print("original set : ",number_set)
print("set length : ",len(number_set))
print("20 exists : ", 20 in number_set)

#-------SET - ADDING AND REMOVING---------
number_set.add(50)
number_set.update([60,70])
print("after adding : ",number_set)

number_set.remove(20)
number_set.discard(100)
removed_item = number_set.pop()
print("after removing : ",number_set)
print("popped item : ",removed_item)

temporary_set = {1, 2, 3}
temporary_set.clear()
print("cleared set : ", temporary_set)

#---------SET - UNION, INTERSECTION AND DIFFERENCE-------
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("union : ",a | b)
print("intersection : ",a & b)
print("differnce  :",a-b)
print("differnce : ",b-a)
print("symmetric difference : ",a^b)
print("is subset : ",{1, 2}.issubset(a))
print("is superset : ",a.issuperset({1, 2}))
print("are disjoint : ",{1, 2}.isdisjoint({5, 6}))


"""
1. Lists: append, insert, extend, remove, pop, del,
    sort, reverse, count, index, copy and clear. 
 2. Tuples: indexing, slicing, count, index, unpacking,
    concatenation and repetition.
3. Sets: add, update, remove, discard, pop, clear,
    union, intersection, difference and subset checks.
4. Membership can be checked using the 'in' operator.
"""