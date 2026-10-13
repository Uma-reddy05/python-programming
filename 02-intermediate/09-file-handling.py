"""
Day 09 - file handling
Topics - write, read and append
Author - Uma
Date - 13-10-2026
"""
with open("notes.txt", "w") as file:
    file.write("hello python! \n")
    file.write("I am learning file handling")

print("file written successfully!")

with open("notes.txt","r") as file:
    content = file.read()
    print(content)

with open("notes.txt", "a") as file:
    file.write("day 09 completed")

print("content added successfully!")

"""

------WHAT I LEARNED--------
1. open() opens a file
2. "w" writes and can overwrite existing content
3. "r" reads file content
4. "a" adds content to the end
5. write open() closes the file automatically
"""