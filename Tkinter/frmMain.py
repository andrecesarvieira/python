"""
Este módulo exibe elementos de tkinter
Autor: André Vieira
Data: 30/05/2024
"""
from tkinter import *
from tkinter import ttk, TclError


def criar_frame(root):

    # Definindo grid para alocar os widgets
    frm_main = ttk.Frame(root)
    frm_main.columnconfigure(0, weight=1)
    frm_main.columnconfigure(0, weight=3)

    # Alocando widgets no grid
    ttk.Label(master=frm_main, text="Usuário:").grid(column=0, row=0, sticky=W)
    usuario = ttk.Entry(frm_main, width=30)
    usuario.focus()
    usuario.grid(column=1, row=0, sticky=W)

    ttk.Label(master=frm_main, text="Senha:").grid(column=0, row=1, sticky=W)
    usuario = ttk.Entry(frm_main, width=30)
    usuario.focus()
    usuario.grid(column=1, row=1, sticky=W)


def criar_janela_principal():

    # Instancia para a classe Tk (janela principal)
    root = Tk()

    # Atribuindo valores padrões da janela
    root.title(string="Login")
    root.config(background="LightGray")
    root.iconphoto(False, PhotoImage(file="logo.png"))
    root.resizable(height=False, width=False)

    # Remover os botões minimizar e maximizar (somente sistema Windows)
    try:
        root.attributes('-toolwindow', True)
    except TclError:
        print('Plataforma não suportada')

    root_altura = 300
    root_largura = 400

    # Centralizando a janela no monitor
    tela_largura: int = root.winfo_screenwidth()
    tela_altura: int = root.winfo_screenheight()
    # Coordenadas do canto superior esquerdo
    x_coordenada = int((tela_largura/2) - (root_largura/2))
    y_coordenada = int((tela_altura/2) - (root_altura/2))
    root.geometry("{}x{}+{}+{}".format(root_largura,
                  root_altura, x_coordenada, y_coordenada))

    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    root.mainloop()

    input_frame = criar_frame(root)
    input_frame.grid(column=0, row=0)


if __name__ == "__main__":
    criar_janela_principal()
