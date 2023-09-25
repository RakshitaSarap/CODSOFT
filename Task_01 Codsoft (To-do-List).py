import tkinter as tk
from tkinter import messagebox

BG_COLOR = "#f2f2f2"
TASK_BG_COLOR = "#ffffff"
BUTTON_BG_COLOR = "#4caf50"
BUTTON_TEXT_COLOR = "white"
TASK_COMPLETED_COLOR = "light green"

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def save_tasks():
    tasks = task_list.get(0, tk.END)
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
        task_list.delete(0, tk.END)
        for task in tasks:
            task = task.strip()
            task_list.insert(tk.END, task)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No saved tasks found!")

def mark_as_completed():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.itemconfig(selected_task_index, {'bg': TASK_COMPLETED_COLOR})
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

root.configure(bg=BG_COLOR)

task_list = tk.Listbox(root, selectmode=tk.SINGLE, bg=TASK_BG_COLOR)
task_list.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=5, padx=10, fill=tk.X)

add_button = tk.Button(root, text="Add Task", command=add_task, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
complete_button = tk.Button(root, text="Mark as Completed", command=mark_as_completed, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
add_button.pack(pady=5, padx=10, fill=tk.X)
delete_button.pack(pady=5, padx=10, fill=tk.X)
complete_button.pack(pady=5, padx=10, fill=tk.X)

save_button = tk.Button(root, text="Save Tasks", command=save_tasks, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
load_button = tk.Button(root, text="Load Tasks", command=load_tasks, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
save_button.pack(pady=5, padx=10, fill=tk.X)
load_button.pack(pady=5, padx=10, fill=tk.X)

load_tasks()
root.mainloop()
