"""
Day 05 - strings in python
Topics - string basics,indexing,slicing,methods,palindrome and anagram
Author - Uma
Date - 09-10-2026
"""

#--------CREATING STRINGS--------
name = "python"
message = "hello, world"
print(name)
print(message)


#----------STRING LENGTH--------
language = "python"
print(len(language))


#-------STRING INDEXING---------
word = "python"
print(word[0])
print(word[1])
print(word[-1])


#---------STRING SLICING--------------
word = "python"
print(word[0:3])
print(word[2:])
print(word[0:4])
print(word[::-1])



#-----------COMMON STRING METHODS---------------
text = "banana"
print(text.count('a')) # count occurrences of a substring

text = "hello, world"
print(text.find('python')) # find returns the first index or -1 if not found
print(text.find('world'))

text = " apple banana mango"
print(text.split())  # splits a string into alist

words = ["python", "is", "fun"]
print(" ".join(words))  # joins a string using separator

text = "i like java"
print(text.replace("java","python"))  # replaces part of a string

text = "  hello python  "
print(text.upper()) # converts letters to uppercase
print(text.lower()) # converts letters to lowercase
print(text.strip()) # removes leading and tailing whitespace 


language = "python"
print(language.startswith("py")) # checks the beginning of a string
print(language.endswith("on")) # checks the ending os a string
print(language.isalpha()) # checks whether all characters are letters


#----PALINDROME----------
# a palindrome reads the same word forward and backward
word = "madam"
if word == word[::-1]:
    print("palindrome")
else:
    print("not a palindrome")


#----------ANAGRAM-----------
#angram contains the same letter in a different order
word1 = "listen"
word2 = "silent"
if sorted(word1.lower()) == sorted(word2.lower()):
    print("anagram")
else:
    print("not an anagram")

