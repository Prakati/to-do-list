import tkinter
import tkinter.messagebox
from tkinter import ttk

root = tkinter.Tk()
root.title("Self checker")
root.configure(bg="pink")

tasks = []


def add_task():
    task = entry_task.get()
    if task != "":
        tasks.append({"task": task, "completed": False})
        list_tasks()
        entry_task.delete(0, tkinter.END)
        update_status("Task added successfully.")
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")
        update_status("Task addition failed.")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        del tasks[task_index]
        list_tasks()
        update_status("Task deleted successfully.")
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")
        update_status("Task deletion failed.")


def update_task_status():
    try:
        task_index = listbox_tasks.curselection()[0]
        tasks[task_index]["completed"] = not tasks[task_index]["completed"]
        list_tasks()
        update_status("Task status updated.")
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")
        update_status("Task status update failed.")


def list_tasks():
    listbox_tasks.delete(0, tkinter.END)
    for task in tasks:
        status = "[Done] " if task["completed"] else "[ ] "
        listbox_tasks.insert(tkinter.END, status + task["task"])
        listbox_tasks.itemconfig(tkinter.END, bg="PaleVioletRed3")  # Set the background color


def update_status(message):
    status_var.set(message)


frame_tasks = tkinter.Frame(root, bg="pink")  # Setting the background color
frame_tasks.grid(row=0, column=0, padx=10, pady=10)

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50, bg="PaleVioletRed3")  # Set the background color
listbox_tasks.grid(row=0, column=0, sticky=tkinter.W)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.grid(row=0, column=1, sticky=tkinter.N + tkinter.S)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.grid(row=1, column=0, padx=10, pady=10)

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.grid(row=2, column=0, padx=10, pady=5)

button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.grid(row=3, column=0, padx=10, pady=5)

button_update_status = tkinter.Button(root, text="Update status", width=48, command=update_task_status)
button_update_status.grid(row=4, column=0, padx=10, pady=5)

status_var = tkinter.StringVar()
status_bar = tkinter.Label(root, textvariable=status_var, bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W)
status_bar.grid(row=5, column=0, padx=10, pady=5, sticky=tkinter.W + tkinter.E)

list_tasks()

root.mainloop()