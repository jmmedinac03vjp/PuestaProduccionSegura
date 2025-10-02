import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.result = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=2, relief="ridge")
        self.result.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]

        for (text, row, col) in buttons:
            tk.Button(master, text=text, width=4, height=2, font=('Arial', 18),
                      command=lambda t=text: self.on_click(t)).grid(row=row, column=col)

    def on_click(self, char):
        if char == '=':
            try:
                self.result.delete(0, tk.END)
                self.result.insert(tk.END, str(eval(self.result.get())))
            except Exception:
                self.result.delete(0, tk.END)
                self.result.insert(tk.END, "Error")
        else:
            self.result.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()