import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")
        self.root.configure(bg="#e8f5e9")

        self.setup_ui()

    def setup_ui(self):
        self.frame = tk.Frame(self.root, bg="#e8f5e9")
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(
            self.frame, width=50, height=10, bd=0, selectmode=tk.SINGLE,
            font=("Courier", 12), bg="#ffffff", fg="#000000",
            selectbackground="#a5d6a7", selectforeground="#000000"
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(self.root, width=50, font=("Courier", 12))
        self.entry.pack(pady=10)

        self.add_button = tk.Button(
            self.root, text="Add Task", command=self.add_task, 
            bg="#4caf50", fg="#ffffff", font=("Courier", 12), bd=0, 
            activebackground="#388e3c"
        )
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(
            self.root, text="Delete Task", command=self.delete_task, 
            bg="#d32f2f", fg="#ffffff", font=("Courier", 12), bd=0, 
            activebackground="#c62828"
        )
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(
            self.root, text="Clear All Tasks", command=self.clear_tasks, 
            bg="#ffa000", fg="#ffffff", font=("Courier", 12), bd=0, 
            activebackground="#ff8f00"
        )
        self.clear_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            self.listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def clear_tasks(self):
        self.listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()