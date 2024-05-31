"""
Este módulo exibe elementos de tkinter
Autor: André Vieira
Data: 30/05/2024
"""

import tkinter as tk
from tkinter import ttk, PhotoImage


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # Centralizando a janela no monitor
        altura = 300
        largura = 400

        tela_largura: int = self.winfo_screenwidth()
        tela_altura: int = self.winfo_screenheight()
        # Coordenadas do canto superior esquerdo
        x_coordenada = int((tela_largura/2) - (largura/2))
        y_coordenada = int((tela_altura/2) - (altura/2))
        self.geometry("{}x{}+{}+{}".format(largura,
                                           altura, x_coordenada, y_coordenada))

        # Atribuindo valores padrões da janela
        self.title(string="Login")
        self.iconphoto(False, PhotoImage(file="logo.png"))
        self.resizable(height=False, width=False)
        self.config(background="lightgray")

        # Configurando a grade
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.criar_widgets()

    def criar_widgets(self):

        # Criação dos widgets
        usuario_label = ttk.Label(master=self, text="Usuário:")
        usuario_entry = ttk.Entry(self)
        senha_label = ttk.Label(master=self, text="Senha:")
        senha_entry = ttk.Entry(self)

        # Posicionamento dos widgets
        usuario_label.grid(column=1, row=1, padx=5, pady=5, sticky="E")
        usuario_entry.grid(column=2, row=1, padx=5, pady=5, sticky="W")
        senha_label.grid(column=1, row=2, padx=5, pady=5, sticky="E")
        senha_entry.grid(column=2, row=2, padx=5, pady=5, sticky="W")

        # Configurando espaçamento extra para centralizar os widgets
        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=4)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # Foco na caixa de texto do usuário
        usuario_entry.focus()


if __name__ == "__main__":
    app = App()
    app.mainloop()
