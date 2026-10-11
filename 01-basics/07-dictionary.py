"""
DAy 07 - dictionary
Topic - creating, accessing, adding, updating, removing, looping, membership and copying
Author - Uma
Date - 11-10-2026
"""

student = {'name':'uma', 'age':17, 'course':'CSE'}
print("student dictionary : ",student)
print("student name : ",student['name'])
print("student age : ",student['age'])
print("keys : ",student.keys())
print("missing keys : ",student.get('city', 'not found'))
print("all keys : ", student.keys())
print("all values : ",student.values())
print("all pairs : ",student.items())
print("dictionary length : ",len(student))


student['college'] = "engineering college"
student['age'] = 18
student.update({'city': 'bengaluru'})
print("after updating : ",student)

print("removed city : ", student.pop("city"))

print("removed last pair : ", student.popitem())


for key in student:
    print(key, ":", student[key])

print("name exists : ", 'name' in student)
print("city exists ; ", 'city' in student)
print("copied dictionary : ", student.copy())
print("after setdefault : ", student.setdefault('course', 'python'))

student.clear()
print("cleared dictionary : ", student)

"""
1. Dictionaries: access, get, keys, values, items,update, pop, popitem, setdefault, copy and clear.
2. Membership can be checked using the 'in' operator.
"""