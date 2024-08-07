import tkinter as tk

def add():
    result = float(entry1.get()) + float(entry2.get())
    display.delete(0, tk.END)
    display.insert(tk.END, result)

def subtract():
    result = float(entry1.get()) - float(entry2.get())
    display.delete(0, tk.END)
    display.insert(tk.END, result)

def multiply():
    result = float(entry1.get()) * float(entry2.get())
    display.delete(0, tk.END)
    display.insert(tk.END, result)

def divide():
    num2 = float(entry2.get())
    if num2 != 0:
        result = float(entry1.get()) / num2
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    else:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error: Cannot divide by zero")

root = tk.Tk()
root.title("Calculator")

entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=2, padx=5, pady=5)

display = tk.Entry(root, width=10)
display.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

add_button = tk.Button(root, text="+", width=5, command=add)
add_button.grid(row=2, column=0, padx=5, pady=5)

subtract_button = tk.Button(root, text="-", width=5, command=subtract)
subtract_button.grid(row=2, column=1, padx=5, pady=5)

multiply_button = tk.Button(root, text="*", width=5, command=multiply)
multiply_button.grid(row=2, column=2, padx=5, pady=5)

divide_button = tk.Button(root, text="/", width=5, command=divide)
divide_button.grid(row=3, column=0, padx=5, pady=5)

root.mainloop()
