import tkinter as tk
from datetime import datetime

# Função para atualizar o cronômetro
def update_time():
    if running:
        global timer
        # Atualiza o tempo
        timer[2] += 1
        if timer[2] >= 100:
            timer[2] = 0
            timer[1] += 1
        if timer[1] >= 60:
            timer[1] = 0
            timer[0] += 1
        # Formata o tempo para o formato hh:mm:ss:cs (horas, minutos, segundos, centésimos de segundo)
        time_string = f'{timer[0]:02d}:{timer[1]:02d}:{timer[2]:02d}'
        # Atualiza o texto do cronômetro
        label.config(text=time_string)
        # Agenda a função para ser chamada novamente após 10ms (1 centésimo de segundo)
        root.after(10, update_time)

# Função para iniciar o cronômetro
def start():
    global running
    running = True
    update_time()

# Função para pausar o cronômetro
def pause():
    global running
    running = False

# Função para reiniciar o cronômetro
def reset():
    global timer
    timer = [0, 0, 0]
    label.config(text='00:00:00')
    pause()

# Configuração da janela Tkinter
root = tk.Tk()
root.title("Cronômetro")

# Inicializa variáveis
running = False
timer = [0, 0, 0]  # Horas, Minutos, Segundos

# Criação dos widgets
label = tk.Label(root, text='00:00:00', font=('Helvetica', 40))
label.pack()

start_button = tk.Button(root, text='Iniciar', command=start)
start_button.pack(side=tk.LEFT)

pause_button = tk.Button(root, text='Pausar', command=pause)
pause_button.pack(side=tk.LEFT)

reset_button = tk.Button(root, text='Reiniciar', command=reset)
reset_button.pack(side=tk.LEFT)

# Inicia o loop principal da GUI
root.mainloop()
