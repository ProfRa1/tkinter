import tkinter as tk
from tkinter import messagebox

# Configurações de estilo
BG_COLOR = "#F0F0F0"  # Cor de fundo
BUTTON_COLOR = "#E1E4E8"
TEXT_COLOR = "#333333"
FONT_NORMAL = ("Arial", 12)
FONT_BOLD = ("Arial", 12, "bold")

# Funções do aplicativo
def add_task():
    task = entry.get()
    if task:
        tasks_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "A tarefa não pode estar vazia!")

def remove_task():
    try:
        selected = tasks_list.curselection()
        tasks_list.delete(selected)
    except:
        messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para remover!")

def mark_completed(event):
    index = tasks_list.curselection()[0]
    current_text = tasks_list.get(index)
    if not current_text.startswith("Concluído: "):
        new_text = f"Concluído: {current_text}"
        tasks_list.delete(index)
        tasks_list.insert(index, new_text)
        tasks_list.itemconfig(index, {'bg':'light green'})

# Configuração da janela principal
root = tk.Tk()
root.title("Lista de Tarefas")
root.configure(bg=BG_COLOR)

# Widgets do aplicativo
entry = tk.Entry(root, font=FONT_NORMAL, bg="#FFFFFF")
add_button = tk.Button(root, text="Adicionar Tarefa", command=add_task, bg=BUTTON_COLOR, font=FONT_BOLD)
remove_button = tk.Button(root, text="Remover Tarefa Selecionada", command=remove_task, bg=BUTTON_COLOR, font=FONT_BOLD)
tasks_list = tk.Listbox(root, font=FONT_NORMAL, bg="#FFFFFF", fg=TEXT_COLOR)

# Associa o evento de duplo clique a mark_completed
tasks_list.bind('<Double-1>', mark_completed)

# Organizando os widgets na janela
entry.pack(padx=10, pady=5, fill=tk.X)
add_button.pack(padx=10, pady=5, fill=tk.X)
tasks_list.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
remove_button.pack(padx=10, pady=5, fill=tk.X)

# Iniciar o loop principal da GUI
root.mainloop()
