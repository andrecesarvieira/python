"""
Este módulo exibe elementos de tkinter
Autor: André Vieira
Data: 30/05/2024
"""
from tkinter import *
from tkinter import ttk


def criar_janela_principal():

    # Instancia para a classe Tk (janela principal)
    root = Tk()

    # Centralizando a janela no monitor
    root_altura = 300
    root_largura = 400

    tela_largura: int = root.winfo_screenwidth()
    tela_altura: int = root.winfo_screenheight()
    # Coordenadas do canto superior esquerdo
    x_coordenada = int((tela_largura/2) - (root_largura/2))
    y_coordenada = int((tela_altura/2) - (root_altura/2))
    root.geometry("{}x{}+{}+{}".format(root_largura,
                  root_altura, x_coordenada, y_coordenada))

    # Atribuindo valores padrões da janela
    root.title(string="Login")
    root.iconphoto(False, PhotoImage(file="logo.png"))
    root.resizable(height=False, width=False)
    root.configure(background="lightgray")

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)

    frame = criar_frame(root)
    frame.grid()

    root.mainloop()


def criar_frame(root):

    # Definindo grid para alocar os widgets
    frame = ttk.Frame(root)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Alocando widgets no grid
    ttk.Label(master=frame, text="Usuário:").grid(column=0, row=0, sticky=W)
    usuario = ttk.Entry(frame, width=30)
    usuario.grid(column=1, row=0, sticky=W)
    usuario.focus()

    ttk.Label(master=frame, text="Senha:").grid(column=0, row=1, sticky=W)
    senha = ttk.Entry(frame, width=30)
    senha.grid(column=1, row=1, sticky=W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


if __name__ == "__main__":
    criar_janela_principal()
