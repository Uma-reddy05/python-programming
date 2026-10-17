"""
Day 13 - RegEX : email validator and password checker
Autor - Uma
Date - 17-10-2026
"""

import re

#---------EMAIL VALIDATOR--------
email = input("enter your email : ")
pattern = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"

if re.fullmatch(pattern, email):
    print("valid email format!")
else:
    print("invalid email format")


#---------PASSWORD CHECKER--------


password = input("enter your paasword : ")
if(
    len(password)>= 8
    and re.search(r"[A-Z]", password)
    and re.search(r"[a-z]", password)
    and re.search(r"\d",password)
):
    print("password meets the basic requiements!")

else:
    print("password does not meet the requirements!")


"""
1. re is Python's regular expression module.
2. re.fullmatch() checks the entire string.
3. re.search() looks for a matching pattern.
4. \d matches a digit.
5. [A-Z] matches an uppercase letter.
6. [a-z] matches a lowercase letter.
7. len() checks the number of characters.
"""