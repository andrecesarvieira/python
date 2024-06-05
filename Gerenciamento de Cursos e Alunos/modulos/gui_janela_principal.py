# Objetivo: Gerenciar a GUI do aplicativo
# Autor...: André Vieira
# Data....: 4/6/24 -> desenvolvimento

import tkinter as tk

from datetime import datetime
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

from modulos.gui_guia_aluno import AbaAlunos
# from modulos.guia_cursos_criar import GuiaCursos -> à implementar
# from modulos.guia_turmas_criar import GuiaTurmas -> à implementar

class JanelaPrincipal():
    def __init__(self, root):
        self.root = root
        self.root.title('Gerenciamento de Escola')
        self.root.resizable(False, False)

        # Centralizar o início da aplicação, considerando a resolução do sistema
        LARGURA = 1280
        ALTURA = 720
        MENU_DO_WINDOWS = 80
        tela_largura = self.root.winfo_screenwidth()
        tela_altura = self.root.winfo_screenheight() - MENU_DO_WINDOWS
        x_coordenada = int((tela_largura / 2) - (LARGURA / 2))
        y_coordenada = int((tela_altura / 2) - (ALTURA / 2))
        self.root.geometry(f'{LARGURA}x{ALTURA}+{x_coordenada}+{y_coordenada}')

        # Definir cores e fontes
        self.COR_FUNDO_LOGO = '#0E2B4A'
        self.COR_FONTE_LOGO = '#FFFFFF'
        self.FAM_FONTE_LOGO = font.Font(family='JetBrains Mono ExtraBold', name='logo', size=18, weight='normal')

        self.COR_FONTE_PADRAO = '#0E2B4A'
        self.FAM_FONTE_PADRAO = font.Font(family='Arial', name='padrao', size=8, weight='bold')

        self.criar_frames()
        self.criar_widgets()
    
    def criar_frames(self):
        self.style = ttk.Style(self.root)

        # Criar frames logo e menu -> em implementação (cor de fundo do frame_logo não está funcionando)
        self.style.configure('Logo.TFrame', background = self.COR_FUNDO_LOGO)
        self.frame_topo = ttk.Frame(self.root, width=1278, height=50, style='Logo.TFrame')
        self.frame_topo.config(borderwidth=2, relief='groove')
        self.frame_topo.grid(row=0, padx=1, sticky='nsew')

        self.frame_meio = ttk.Frame(self.root, width=1278, height=644)
        self.frame_meio.config(borderwidth=2, relief='groove')
        self.frame_meio.grid(row=1, padx=1, sticky='nsew')

        self.frame_rodape = ttk.Frame(self.root, width=1278, height=25)
        self.frame_rodape.config(borderwidth=2, relief='flat')
        self.frame_rodape.grid(row=2, padx=1, sticky='nsew')

    def criar_widgets(self):
        # Definir icone e descrição no frame_logo
        o = Image.open(fp='imagens/img_alunos.png')
        r = o.resize(size=(35, 35))
        img = ImageTk.PhotoImage(r)

        lbl_logo_img = ttk.Label(self.frame_topo, image=img, compound='left', anchor='nw',
                                 background=self.COR_FUNDO_LOGO)
        lbl_logo_img.image = img
        lbl_logo_img.place(x=340, y=4)
        lbl_logo_txt = ttk.Label(self.frame_topo, text='Escola de Desenvolvimento Python', width=32,
                                 compound='left', anchor='w', font=self.FAM_FONTE_LOGO,
                                 foreground=self.COR_FONTE_LOGO, background=self.COR_FUNDO_LOGO)
        lbl_logo_txt.place(x=400, y=6)

        # Criação das abas (bootstrap) no frame_abas
        #Abas = ttk.Notebook(self.frame_meio)
        #aba_alunos = ttk.Frame(Abas)
        #aba_cursos = ttk.Frame(Abas)
        #aba_turmas = ttk.Frame(Abas)
        #Abas.add(aba_alunos, text='Alunos')
        #Abas.add(aba_cursos, text='Cursos')
        #Abas.add(aba_turmas, text='Turmas')
        #Abas.pack(expand=1, fill='both')

        # Criar label de mensagem para o usuário no frame_msg
        o = Image.open(fp='imagens/notificacao.png')
        r = o.resize(size=(16, 14))
        img2 = ImageTk.PhotoImage(r)
        
        lbl_msg_img = ttk.Label(self.frame_rodape, image=img2, anchor='w')
        lbl_msg_img.image = img2
        lbl_msg_img.place(x=0, y=0)

        hora = datetime.now()
        lbl_msg_txt = ttk.Label(self.frame_rodape, text=hora.strftime('%H:%M:%S') + ' - Sistema funcionando corretamente',
                                anchor='w', font=self.FAM_FONTE_PADRAO)
        lbl_msg_txt.place(x=20, y=0)

        # Criação dos widgets alunos nas abas
        # alunos = AbaAlunos(aba_alunos, self.style)
        # cursos = CriarFramesAlunos(aba_cursos) -> à implementar
        # turmas = CriarFramesAlunos(aba_turmas) -> à implementar
