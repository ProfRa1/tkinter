import tkinter as tk

def convert_to_hours():
    try:
        time = float(entry.get())
        if radio_var.get() == 1:  # Se a opção selecionada for minutos
            hours = time / 60
        else:  # Se a opção selecionada for segundos
            hours = time / 3600
        result_label.config(text=f"{time} {'minutos' if radio_var.get() == 1 else 'segundos'} = {hours:.2f} horas")
    except ValueError:
        result_label.config(text="Por favor, insira um número válido.")

# Criando a janela principal
root = tk.Tk()
root.title("Conversor de Tempo")
root.geometry("300x200")

# Rótulo e campo de entrada
entry_label = tk.Label(root, text="Tempo:")
entry_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

# Radio buttons para escolher a unidade de tempo
radio_var = tk.IntVar()
minutes_radio = tk.Radiobutton(root, text="Minutos", variable=radio_var, value=1)
minutes_radio.pack()
seconds_radio = tk.Radiobutton(root, text="Segundos", variable=radio_var, value=2)
seconds_radio.pack()

# Botão para conversão
to_hours_button = tk.Button(root, text="Converter para Horas", command=convert_to_hours)
to_hours_button.pack(pady=5)

# Rótulo para exibir o resultado
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Iniciando o loop principal da aplicação
root.mainloop()




