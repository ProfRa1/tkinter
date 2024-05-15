import tkinter as tk

def add_task():
    # Função para adicionar uma nova tarefa à lista
    pass

def remove_task():
    # Função para remover a tarefa selecionada da lista
    pass

def mark_completed():
    # Função para marcar uma tarefa como concluída
    pass

# Criar a janela principal
root = tk.Tk()
root.title("Lista de Tarefas")

# Criar os widgets (entrada, botões, lista de tarefas)
entry = tk.Entry(root)
add_button = tk.Button(root, text="Adicionar Tarefa", command=add_task)
remove_button = tk.Button(root, text="Remover Tarefa Selecionada", command=remove_task)
tasks_list = tk.Listbox(root)
tasks_list.bind('<Double-1>', mark_completed)  # Associa o evento de duplo clique a mark_completed

# Organizar os widgets na janela
entry.pack()
add_button.pack()
tasks_list.pack()
remove_button.pack()

# Iniciar o loop principal da GUI
root.mainloop()
