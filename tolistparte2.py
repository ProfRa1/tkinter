import tkinter as tk

def add_task():
    task = entry.get()
    if task:  # Verifica se a tarefa não está vazia
        tasks_list.insert(tk.END, task)
        entry.delete(0, tk.END)  # Limpa o campo de entrada após adicionar
    else:
        tk.messagebox.showwarning("Aviso", "A tarefa não pode estar vazia!")  # Mostra um aviso se a entrada estiver vazia

def remove_task():
    try:
        selected = tasks_list.curselection()  # Obtém o índice da tarefa selecionada
        tasks_list.delete(selected)  # Remove a tarefa selecionada da lista
    except:
        tk.messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para remover!")  # Mostra um aviso se nenhuma tarefa for selecionada

def mark_completed(event):
    # Obtém o índice do item que foi clicado duas vezes
    index = tasks_list.curselection()[0]
    # Obtém o texto atual do item e adiciona o prefixo "Concluído: "
    current_text = tasks_list.get(index)
    # Verifica se a tarefa já está marcada como concluída para evitar sobreposição
    if not current_text.startswith("Concluído: "):
        new_text = f"Concluído: {current_text}"
        # Atualiza o item na lista com o novo texto
        tasks_list.delete(index)
        tasks_list.insert(index, new_text)
        # Muda a cor do item para verde para indicar que está concluído
        tasks_list.itemconfig(index, {'bg':'light green'})

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
