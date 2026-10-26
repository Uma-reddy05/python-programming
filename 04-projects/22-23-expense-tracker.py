"""
Day 22-23 - project 1
Topic - expense trackers(CLI + File handling)
Author - Uma
Date - 26-10-2026 and 27-10-2026
"""

import os

FILE_NAME = "expenses.txt"

def add_expense():
    name = input("enter expense name : ")
    amount = float(input("enter amount : "))

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{amount}\n")

    print("expense added successfully!")

def view_expense():
    if not os.path.exists(FILE_NAME):
        print("no expenses found")
        return

    with open(FILE_NAME, "r") as file:
        expenses = file.readlines()

    if not expenses:
        print("no expenses found")
        return

    print("------YOUR EXPENSES------")

    for expense in expenses:
        name, amount = expense.strip().rsplit(",",1)
        print(f"{name} : ${float(amount):.2f}")


def show_total():
    total = 0

    if not os.path.exists(FILE_NAME):
        print("no expenses found")
        return

    with open(FILE_NAME, "r") as file:
        for expense in file:
            name, amount = expense.strip().rsplit(",",1)
            total += float(amount)

    print(f"total spending : ${total:.2f}")


def main():
    while True:
        print("------EXPENSE TRACKER-------")
        print("1. add expense")
        print("2. view expense")
        print("3. show toatl")
        print("4. exit")

        choice = int(input("choose an option : "))

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expense()
        elif choice == 3:
            show_total()
        elif choice == 4:
            print("thank you for using expense tracker")
            break
        else:
            print("invalid choice try again")

main()