import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        self.root.configure(bg="#5a7edc")
        
        self.tarefas = []

        self.create_widgets()

    def create_widgets(self):
        
        self.label = tk.Label(self.root, text="Digite uma nova tarefa:", bg='#5a7edc')
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, width=40, bg='#ffffff')
        self.entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Adicionar Tarefa", command=self.add_task, bg='#7DDBA5')
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, height=10, width=50, bg='#ece9d8')
        self.task_listbox.pack(pady=10)

        self.remove_button = tk.Button(self.root, text="Remover Tarefa", command=self.remove_task, bg='#f64935')
        self.remove_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tarefas.append(task)
            self.update_tasks_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Sem tarefa", "Digite uma tarefa para adicionar.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tarefas.pop(selected_task_index) 
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Nenhuma Tarefa Selecionada", "Selecione uma tarefa para remover.")

    def update_tasks_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tarefas:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
