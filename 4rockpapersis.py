import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x300")
        self.root.configure(bg="#e8f5e9")

        self.user_score = 0
        self.computer_score = 0

        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(
            self.root, text="Choose Rock, Paper, or Scissors:", 
            font=("Courier", 14), bg="#e8f5e9"
        )
        self.label.pack(pady=10)

        self.choice_var = tk.StringVar(value="Rock")
        self.choice_menu = tk.OptionMenu(
            self.root, self.choice_var, "Rock", "Paper", "Scissors"
        )
        self.choice_menu.configure(font=("Courier", 14), bg="#c8e6c9", borderwidth=2)
        self.choice_menu.pack(pady=10)

        self.play_button = tk.Button(
            self.root, text="Play", command=self.play, 
            font=("Courier", 14), bg="#4caf50", fg="#ffffff", borderwidth=2
        )
        self.play_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Courier", 14), bg="#e8f5e9")
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(self.root, text="User: 0  Computer: 0", font=("Courier", 14), bg="#e8f5e9")
        self.score_label.pack(pady=10)

    def play(self):
        user_choice = self.choice_var.get()
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1

        self.result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
        self.score_label.config(text=f"User: {self.user_score}  Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()