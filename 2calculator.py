import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.configure(bg="#e8f5e9")

        self.create_widgets()

    def create_widgets(self):
        self.entry1 = tk.Entry(self.root, width=10, font=("Courier", 18), borderwidth=2)
        self.entry1.pack(pady=10)

        self.entry2 = tk.Entry(self.root, width=10, font=("Courier", 18), borderwidth=2)
        self.entry2.pack(pady=10)

        self.operations = ["+", "-", "*", "/"]
        self.operation_var = tk.StringVar(value=self.operations[0])
        self.operation_menu = tk.OptionMenu(self.root, self.operation_var, *self.operations)
        self.operation_menu.configure(font=("Courier", 14), bg="#c8e6c9", borderwidth=2)
        self.operation_menu.pack(pady=10)

        self.calc_button = tk.Button(
            self.root, text="Calculate", command=self.calculate, 
            font=("Courier", 16), bg="#4caf50", fg="#ffffff", borderwidth=2
        )
        self.calc_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Courier", 16), bg="#e8f5e9")
        self.result_label.pack(pady=20)

    def calculate(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2

            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()