import tkinter as tk
from tkinter import messagebox
# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
# Create an entry widget for input and result display
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=2, justify='right')
entry.grid(row=0, column=0, columnspan=4)
def btn_click(item):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(item))
def btn_clear():
    entry.delete(0, tk.END)
def btn_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)


# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Arrange buttons in the grid
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18),
                        command=btn_equal)
    elif button == 'C':
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18),
                        command=btn_clear)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18),
                        command=lambda button=button: btn_click(button))

    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
clear_button = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=btn_clear)
clear_button.grid(row=row_val, column=col_val)
# Run the main loop
root.mainloop()
