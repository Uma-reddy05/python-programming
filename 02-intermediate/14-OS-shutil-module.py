"""
Day 14 - OS and shutil modules
Author - Uma
Date - 18-10-2026
"""

import os
import shutil

print("current directory : ",os.getcwd())

if not os.path.exists("my folder"):
    os.mkdir("my folder")
    print("folder created")

print("items : ",os.listdir("."))


with open("sample.txt", "w") as file:
    file.write("learning python automation!")

shutil.copy("sample.txt","smaple_copy.txt")
print("file copied!")


"""
------WHAT I LEARNED-------
1. os.getcwd() gets the current directory.
2. os.mkdir() creates a folder.
3. os.path.exists() checks whether a path exists.
4. os.listdir() lists directory content
5. shutil.copy() copies a file.
"""