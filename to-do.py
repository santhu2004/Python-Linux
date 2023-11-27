import tkinter as tk

def add_task():
    """Add a task to the to-do list."""
    task = entry.get()
    if task:
        tasks.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    """Remove a selected task from the to-do list."""
    try:
        index = tasks.curselection()[0]
        tasks.delete(index)
    except IndexError:
        pass

def complete_task():
    """Mark a selected task as completed."""
    try:
        index = tasks.curselection()[0]
        tasks.itemconfig(index, fg="gray")
    except IndexError:
        pass

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Create task list
tasks = tk.Listbox(root, bg="lightyellow", width=50)
tasks.pack(padx=10, pady=10)

# Create entry for new tasks
entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)

# Create buttons
add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
add_button.pack(padx=10, pady=5)

remove_button = tk.Button(root, text="Remove Task", width=10, command=remove_task)
remove_button.pack(padx=10, pady=5)

complete_button = tk.Button(root, text="Complete Task", width=12, command=complete_task)
complete_button.pack(padx=10, pady=5)

root.mainloop()
