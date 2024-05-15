import tkinter as tk

def calcular_inverso():
    try:
        num = int(entry.get())
        inverso = 1 / num
        result_label.config(text=f"O inverso de {num} é {inverso}")
    except ValueError:
        result_label.config(text="Isso não é um número válido.")
    except ZeroDivisionError:
        result_label.config(text="Zero não tem inverso.")
    except Exception as e:
        result_label.config(text=f"Algo deu errado: {e}")
    else:
        result_label.config(text="Tudo correu bem!")
    finally:
        print("Fim do programa.")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Inverso")

# Criação dos widgets
label = tk.Label(root, text="Digite um número:")
label.pack()

entry = tk.Entry(root)
entry.pack()

calc_button = tk.Button(root, text="Calcular", command=calcular_inverso)
calc_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Loop principal
root.mainloop()
