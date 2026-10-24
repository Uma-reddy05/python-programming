"""
Day 20 - tkinter GUI basics
Author - Uma
Date - 24-10-2026
"""


import tkinter as tk

# create the main window
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200")

# function for button click
def say_hello():
    label.config(text = "welcome to python")
 
# create a label
label = tk.Label(root, text="hello, user!")
label.pack(pady=20)

# create a button
button = tk.Button(
    root,
    text = "click me",
    command = say_hello
)
button.pack()

#run the appliction
root.mainloop()


"""
------WHAT I LEARNED--------

1. tk.Tk() — creates the main window.
2. title() — sets the window title.
3. geometry() — sets the window size.
4. Label() — displays text.
5. Button() — creates a clickable button.
6. pack() — places a widget in the window.
7. config() — updates a widget.
8. mainloop() — keeps the GUI running.
"""