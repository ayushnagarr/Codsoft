import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x200")
        self.root.configure(bg="#e8f5e9")

        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(
            self.root, text="Enter desired password length:", 
            font=("Courier", 14), bg="#e8f5e9"
        )
        self.label.pack(pady=10)

        self.length_entry = tk.Entry(self.root, font=("Courier", 14), width=10)
        self.length_entry.pack(pady=10)

        self.generate_button = tk.Button(
            self.root, text="Generate Password", command=self.generate_password, 
            font=("Courier", 14), bg="#4caf50", fg="#ffffff", borderwidth=2
        )
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(self.root, text="", font=("Courier", 14), bg="#e8f5e9")
        self.password_label.pack(pady=20)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(length))
            self.password_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for the length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
    