# tkinter é uma biblioteca que acompanha nativamente o python, muito utilizada para criação de interfaces e janelas
# https://www.pythontutorial.net/tkinter/tkinter-ttk/
# https://docs.python.org/3/library/tkinter.html

import tkinter as tk

# Instanciando a janela
root = tk.Tk()

# adicionando um titulo a janela
root.title('Download YouTube')

# Definindo as dimenções da tela (window.geometry('WIDTHxHEIGHT+X+Y'))
root.geometry('600x500+50+50')

# Deixando as dimensções fixas
root.resizable(False, False)

# widget
message = tk.Label(root, text="Hello, World!")
message.pack()

# Mantendo a janela aberta
root.mainloop()
