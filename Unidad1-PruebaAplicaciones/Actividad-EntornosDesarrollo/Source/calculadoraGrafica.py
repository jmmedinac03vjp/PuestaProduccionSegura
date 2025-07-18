import tkinter as tk
from tkinter import messagebox

def suma(num1, num2):
#    try:
        num1_int = int(num1)
        num2_int = int(num2)
        return num1_int + num2_int
#    except ValueError:
#        messagebox.showerror("Error", "Por favor, ingrese números enteros")

def resta(num1, num2):
    try:
        num1_int = int(num1)
        num2_int = int(num2)
        return num1_int - num2_int
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números enteros")

def multiplicacion(num1, num2):
    try:
        num1_int = int(num1)
        num2_int = int(num2)
        return num1_int * num2_int
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números enteros")

def division(num1, num2):
    try:
        num1_int = int(num1)
        num2_int = int(num2)
        if num2_int == 0:
            messagebox.showerror("Error", "División por cero")
            return None
        else:
            return num1_int / num2_int
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números enteros")

def calcular(operacion):
    num1_val = num1.get()
    num2_val = num2.get()
    if operacion == "suma":
        resultado.set(suma(num1_val, num2_val))
    elif operacion == "resta":
        resultado.set(resta(num1_val, num2_val))
    elif operacion == "multiplicacion":
        resultado.set(multiplicacion(num1_val, num2_val))
    elif operacion == "division":
        resultado.set(division(num1_val, num2_val))

app = tk.Tk()
app.title("Calculadora")

tk.Label(app, text="Número 1").grid(row=0, column=0)
tk.Label(app, text="Número 2").grid(row=1, column=0)
tk.Label(app, text="Resultado").grid(row=2, column=0)

num1 = tk.StringVar()
num2 = tk.StringVar()
resultado = tk.StringVar()

tk.Entry(app, textvariable=num1).grid(row=0, column=1)
tk.Entry(app, textvariable=num2).grid(row=1, column=1)
tk.Entry(app, textvariable=resultado, state="readonly").grid(row=2, column=1)

tk.Button(app, text="Sumar", command=lambda: calcular("suma")).grid(row=3, column=0)
tk.Button(app, text="Restar", command=lambda: calcular("resta")).grid(row=3, column=1)
tk.Button(app, text="Multiplicar", command=lambda: calcular("multiplicacion")).grid(row=4, column=0)
tk.Button(app, text="Dividir", command=lambda: calcular("division")).grid(row=4, column=1)

app.mainloop()
