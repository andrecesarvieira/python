# Módulo para criação da estrutura de um AppHub
# Autor: André Vieira
# Data: 30/05/2024

import tkinter as tk
from tkinter import Label

class AppHub:
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Sistema de Controle")
        self.root.resizable(False, False)

        # Centralizando a janela conforme resolução do monitor
        largura = 1280
        altura = 720
        tela_largura = self.root.winfo_screenwidth()
        tela_altura = self.root.winfo_screenheight() - 80
        x_coordenada = int((tela_largura / 2) - (largura / 2))
        y_coordenada = int((tela_altura / 2) - (altura / 2))
        self.root.geometry(f"{largura}x{altura}+{x_coordenada}+{y_coordenada}")

        # Frame lateral
        self.menu_frame_cor = "#383838"

        self.menu_frame = tk.Frame(self.root, background=self.menu_frame_cor)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y, padx=3, pady=3)
        self.menu_frame.pack_propagate(False)
        self.menu_frame.configure(width=45)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(side=tk.LEFT, fill="both", padx=3, pady=3)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=1280)

        self.criar_widgets_menu()
        self.agenda()
        self.root.mainloop()

    def criar_widgets_menu(self):

        # Imagens
        self.toggle_png = tk.PhotoImage(file="images/menu.png")
        self.agenda_png = tk.PhotoImage(file="images/menu_agenda.png")
        self.cadastro_png = tk.PhotoImage(file="images/menu_cadastro.png")
        self.financeiro_png = tk.PhotoImage(file="images/menu_financeiro.png")
        self.pedidos_png = tk.PhotoImage(file="images/menu_pedidos.png")
        self.produtos_png = tk.PhotoImage(file="images/menu_produtos.png")
        self.config_png = tk.PhotoImage(file="images/menu_config.png")
        self.sair_png = tk.PhotoImage(file="images/menu_sair.png")

        # Botão Toggle

        botao_toggle = tk.Button(self.menu_frame, image=self.toggle_png, background=self.menu_frame_cor,
                                 border=0, activebackground=self.menu_frame_cor)
        botao_toggle.place(x=4, y=10)

        # Botão Agenda
        botao_agenda = tk.Button(self.menu_frame, image=self.agenda_png, background=self.menu_frame_cor,
                                 border=0, activebackground=self.menu_frame_cor,
                                 command=lambda: self.botoes_menu(ind=botao_agenda_ind, pagina=self.agenda))
        botao_agenda.place(x=8, y=113, width=32, height=35)
        botao_agenda_ind = tk.Label(self.menu_frame, background="white")
        botao_agenda_ind.place(x=3, y=113, width=2, height=35)

        # Botão Cadastro
        botao_cadastro = tk.Button(self.menu_frame, image=self.cadastro_png, background=self.menu_frame_cor,
                                   border=0, activebackground=self.menu_frame_cor,
                                   command=lambda: self.botoes_menu(ind=botao_cadastro_ind, pagina=self.cadastro))
        botao_cadastro.place(x=8, y=160, width=30, height=35)
        botao_cadastro_ind = tk.Label(self.menu_frame, background=self.menu_frame_cor)
        botao_cadastro_ind.place(x=3, y=160, width=2, height=35)

        # Botão Financeiro
        botao_financeiro = tk.Button(self.menu_frame, image=self.financeiro_png, background=self.menu_frame_cor,
                                     border=0, activebackground=self.menu_frame_cor,
                                     command=lambda: self.botoes_menu(ind=botao_financeiro_ind, pagina=self.financeiro))
        botao_financeiro.place(x=8, y=210, width=30, height=35)
        botao_financeiro_ind = tk.Label(self.menu_frame, background=self.menu_frame_cor)
        botao_financeiro_ind.place(x=3, y=210, width=2, height=35)

        # Botão Pedidos
        botao_pedidos = tk.Button(self.menu_frame, image=self.pedidos_png, background=self.menu_frame_cor,
                                  border=0, activebackground=self.menu_frame_cor,
                                  command=lambda: self.botoes_menu(ind=botao_pedidos_ind, pagina=self.pedidos))
        botao_pedidos.place(x=8, y=260, width=30, height=35)
        botao_pedidos_ind = tk.Label(self.menu_frame, background=self.menu_frame_cor)
        botao_pedidos_ind.place(x=3, y=260, width=2, height=35)

    def botoes_menu(self, ind, pagina):
        # Inicializa indicadores dos botões
        for widget in self.menu_frame.winfo_children():
            if isinstance(widget, Label):
                widget.config(background=self.menu_frame_cor)

        ind.config(background="white")

        self.exclui_paginas()
        pagina()

    def agenda(self):
        frame_agenda = tk.Frame(self.main_frame)

        lbl_texto = tk.Label(frame_agenda, text="Página Agenda\n\n1", font="Arial 30 bold")
        lbl_texto.pack()

        frame_agenda.pack()

    def cadastro(self):
        frame_cadastro = tk.Frame(self.main_frame)

        lbl_texto = tk.Label(frame_cadastro, text="Página Cadastro\n\n2", font="Arial 30 bold")
        lbl_texto.pack()

        frame_cadastro.pack()

    def financeiro(self):
        frame_financeiro = tk.Frame(self.main_frame)

        lbl_texto = tk.Label(frame_financeiro, text="Página Financeiro\n\n3", font="Arial 30 bold")
        lbl_texto.pack()

        frame_financeiro.pack()

    def pedidos(self):
        frame_pedidos = tk.Frame(self.main_frame)

        lbl_texto = tk.Label(frame_pedidos, text="Página Pedidos\n\n4", font="Arial 30 bold")
        lbl_texto.pack()

        frame_pedidos.pack()

    def exclui_paginas(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()


if __name__ == '__main__':
    app = AppHub()
