"""
Módulo para criação da estrutura de um App
Autor: André Vieira
Data: 30/05/2024
"""
import tkinter as tk
from tkinter import Label


def cria_janela():

    root = tk.Tk()
    root.title("App Hub")
    root.resizable(False, False)

    # Centralizando a janela conforme resolução do monitor
    largura = 1280
    altura = 720
    tela_largura: int = root.winfo_screenwidth()
    tela_altura: int = root.winfo_screenheight() - 80
    x_coordenada = int((tela_largura/2) - (largura/2))
    y_coordenada = int((tela_altura/2) - (altura/2))
    root.geometry(
        newGeometry=f"{largura}x{altura}+{x_coordenada}+{y_coordenada}")

    # Frame lateral
    menu_frame_cor = "#383838"

    global menu_frame
    menu_frame = tk.Frame(root, background=menu_frame_cor)
    menu_frame.pack(side=tk.LEFT, fill=tk.Y, padx=3, pady=3)
    menu_frame.pack_propagate(flag=False)
    menu_frame.configure(width=45)

    # Frame principal

    global main_frame
    main_frame = tk.Frame(root)
    main_frame.pack(side=tk.LEFT, fill="both", padx=3, pady=3)
    main_frame.pack_propagate(flag=False)
    main_frame.configure(width=1280)

    # Imagens
    toggle_icone = tk.PhotoImage(file="images/menu.png")
    agenda_icone = tk.PhotoImage(file="images/menu_agenda.png")
    cadastro_icone = tk.PhotoImage(file="images/menu_cadastro.png")

    # Botão Toggle
    botao_toggle = tk.Button(menu_frame, image=toggle_icone, background=menu_frame_cor,
                             border=0, activebackground=menu_frame_cor)
    botao_toggle.place(x=4, y=10)

    # Botão Agenda
    botao_agenda = tk.Button(menu_frame, image=agenda_icone, background=menu_frame_cor,
                             border=0, activebackground=menu_frame_cor,
                             command=lambda: botoes_acao(ind=botao_agenda_ind, pagina=agenda))
    botao_agenda.place(x=8, y=113, width=32, height=35)
    botao_agenda_ind = tk.Label(menu_frame, background="white")
    botao_agenda_ind.place(x=3, y=113, width=2, height=35)

    # Botão Cadastro
    botao_cadastro = tk.Button(menu_frame, image=cadastro_icone, background=menu_frame_cor,
                               border=0, activebackground=menu_frame_cor,
                               command=lambda: botoes_acao(ind=botao_cadastro_ind, pagina=cadastro))
    botao_cadastro.place(x=8, y=170, width=30, height=35)
    botao_cadastro_ind = tk.Label(menu_frame, background=menu_frame_cor)
    botao_cadastro_ind.place(x=3, y=170, width=2, height=35)

    agenda()
    root.mainloop()


def botoes_acao(ind, pagina):

    # Inicializa indicadores dos botões
    for widget in menu_frame.winfo_children():
        if isinstance(widget, Label):
            widget.config(background="#383838")

    ind.config(background="white")

    exclui_paginas()
    pagina()


def agenda():

    frame_agenda = tk.Frame(main_frame)

    lbl_texto = tk.Label(
        frame_agenda, text="Página Agenda\n\n1", font="Arial 30 bold")
    lbl_texto.pack()

    frame_agenda.pack()


def cadastro():

    frame_cadastro = tk.Frame(main_frame)

    lbl_texto = tk.Label(
        frame_cadastro, text="Página Cadastro\n\n2", font="Arial 30 bold")
    lbl_texto.pack()

    frame_cadastro.pack()


def exclui_paginas():

    for frame in main_frame.winfo_children():
        frame.destroy()


if __name__ == '__main__':
    cria_janela()
