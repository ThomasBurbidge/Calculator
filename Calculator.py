from tkinter import *

root = Tk()

def number(num):
    print("ran2")
    data = inputField.get()
    inputField.delete(0, END)
    inputField.insert(0, data + str(num))
    
def operationFunc(op):
    global operation
    operation = op
    global num1
    try:
        float(inputField.get())
        num1 = float(inputField.get())
        inputField.delete(0, END)
    except ValueError:
         inputField.delete(0, END)
         inputField.insert(0, "Invalid number")
def calculate(equals):
    try:
        float(inputField.get())
        result = float(inputField.get())
        global num1
        global operation
        if operation == "/":
            result = num1 / result
        elif operation == "x":
            result = num1 * result
        elif operation == "-":
            result = num1 - result
        elif operation == "+":
            result =  num1 + result
        operation = ""
        inputField.delete(0, END)
        inputField.insert(0, str(result))
    except ValueError:
        inputField.delete(0, END)
        inputField.insert(0, "Invalid number")
buttons = [
    ("1", "0", "3", number),
    ("2", "1", "3", number),
    ("3", "2", "3", number),
    ("4", "0", "2", number),
    ("5", "1", "2", number),
    ("6", "2", "2", number),
    ("7", "0", "1", number),
    ("8", "1", "1", number),
    ("9", "2", "1", number),
    ("0", "0", "4", number),
    (".", "1", "4", number),
    ("=", "2", "4", calculate),
    ("/", "3", "1", operationFunc),
    ("x", "3", "2", operationFunc),
    ("-", "3", "3", operationFunc),
    ("+", "3", "4", operationFunc)
]

# Number, Column, Row, Function
for n, c, r, f in buttons:
    button = Button(root, text=n, command=lambda n=n, f=f: f(n), padx=25, pady=20).grid(column=c, row=r, padx=1, pady=1)

inputField = Entry(root, font=20, width=24)
inputField.grid(column=0, row=0, columnspan=4, pady=5)
root.mainloop()