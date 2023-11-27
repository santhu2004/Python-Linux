"""
The shortest calculator program can be done in a single line using the "eval()" function in python:
print(eval(input("Enter the expression as a string: ")))
"""

import tkinter as tk

def calculate():
    """
    Perform calculation based on the expression entered in the entry field.
    If successful, display the result. If there's an error, display 'Error'.
    """
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def add_to_display(value):
    """
    Add a value to the entry field when a button is clicked.

    Args:
    - value: The value to be added to the entry field.
    """
    entry.insert(tk.END, value)

def clear_display():
    """Clear the content in the entry field."""
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Colorful Calculator")

# Entry field for display
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

# Create and place buttons in a grid layout
row_num = 1
col_num = 0

for row in buttons:
    col_num = 0
    for button_text in row:
        if button_text == '=':
            button = tk.Button(root, text=button_text, padx=40, pady=20, command=calculate, bg='orange')
        elif button_text == 'C':
            button = tk.Button(root, text=button_text, padx=40, pady=20, command=clear_display, bg='red')
        else:
            button = tk.Button(root, text=button_text, padx=40, pady=20, command=lambda value=button_text: add_to_display(value))
        button.grid(row=row_num, column=col_num, padx=5, pady=5)
        col_num += 1
    row_num += 1

root.mainloop()  # Start the main event loop
