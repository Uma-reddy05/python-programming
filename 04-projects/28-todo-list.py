import tkinter as tk
from tkinter import messagebox

#main window
root = tk.Tk()
root.title("my to-do list")
root.geometry("400x500")
root.config(bg="#202b38")

#title
title = tk.Label(
    root,
    text = "MY TO DO LIST",
    font = ("Arial", 22, "bold"),
    bg = "#202b38",
    fg = "white"
)

title.pack(pady=20)

#task input
task_entry = tk.entry(
    root,
    font = ("arial", 14),
    width = 25
)
task_entry.pack(pady=10)


# add tak function
def add_task():
    task = task_entry.get()

    if task.strip() == "":
        messagebox.showwarning("warning", "enter a task")
    else:
        task_list.insert(tk.END,task)
        task_entry.delete(0, tk.END)

# Delete task function
def delete_task():
    selected = task_list.curselection()

    if selected:
        task_list.delete(selected[0])
    else:
        messagebox.showwarning("Warning", "Select a task!")


# Complete task function
def complete_task():
    selected = task_list.curselection()

    if selected:
        task = task_list.get(selected[0])
        task_list.delete(selected[0])
        task_list.insert(tk.END, "✔ " + task)
    else:
        messagebox.showwarning("Warning", "Select a task!")


# Task list
task_list = tk.Listbox(
    root,
    font=("Arial", 13),
    width=30,
    height=12
)
task_list.pack(pady=15)


# Add button
add_button = tk.Button(
    root,
    text="Add Task",
    command=add_task,
    bg="#00b894",
    fg="white",
    width=15
)
add_button.pack(pady=5)


# Complete button
complete_button = tk.Button(
    root,
    text="Complete Task",
    command=complete_task,
    bg="#0984e3",
    fg="white",
    width=15
)
complete_button.pack(pady=5)


# Delete button
delete_button = tk.Button(
    root,
    text="Delete Task",
    command=delete_task,
    bg="#d63031",
    fg="white",
    width=15
)
delete_button.pack(pady=5)


# Run application
root.mainloop()
