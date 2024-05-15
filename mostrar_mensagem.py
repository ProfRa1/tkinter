import tkinter as tk

def show_message():
    name = entry.get()
    if name:
        label.config(text=f"Olá, {name}!")
    else:
        label.config(text="Por favor, insira seu nome.")

# Criando a janela principal
root = tk.Tk()
root.title("Minha Interface Avançada")
root.geometry("300x200")

# Criando um rótulo
label = tk.Label(root, text="Digite seu nome:")
label.pack(pady=10)

# Criando um campo de entrada
entry = tk.Entry(root)
entry.pack(pady=5)

# Criando um botão
button = tk.Button(root, text="Clique Aqui", command=show_message)
button.pack(pady=5)

# Rótulo para exibir a mensagem
label = tk.Label(root, text="")
label.pack(pady=10)

# Iniciando o loop principal da aplicação
root.mainloop()
