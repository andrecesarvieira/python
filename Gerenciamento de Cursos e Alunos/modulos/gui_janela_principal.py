# Objetivo: Gerenciar a GUI do aplicativo
# Autor...: André Vieira
# Data....: 4/6/24 -> desenvolvimento

import tkinter as tk

from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

from modulos.gui_guia_aluno import AbaAlunos
#from modulos.guia_cursos_criar import GuiaCursos -> à implementar
#from modulos.guia_turmas_criar import GuiaTurmas -> à implementar

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

    self.criar_frames()
    self.criar_widgets()

  def criar_frames(self):
    self.style = ttk.Style(self.root)  
    
    # Criar frames logo e menu -> em implementação (cor de fundo do frame_logo não está funcionando)
    self.style.configure('custom.TFrame', background='green', relief='sunken')    
    self.frame_topo = ttk.Frame(self.root, width=1280, height=60, relief='raised',style='custom.TFrame')
    self.frame_topo.config(borderwidth=1)
    self.frame_topo.grid(row=0, column=0, columnspan=1, pady=2, padx=1, sticky='nsew')
    
    self.frame_meio = ttk.Frame(self.root, width=1280, height=640, style='custom.TFrame')
    self.frame_meio.grid(row=2, column=0, columnspan=1, pady=0, padx=1, sticky='nsew')
    
    self.frame_rodape = ttk.Frame(self.root, width=1276, height=20, style='Teste.TFrame', relief='flat')
    self.frame_rodape.grid(row=3, column=0, columnspan=1, pady=0, padx=1, sticky='s')

  def criar_widgets(self):
    # Definir cores e fonte
    COR_FONTE = '#0E2B4A'
    FONTE_LOGO = font.Font(family='JetBrains Mono ExtraBold', name='logo', size=18, weight='normal')

    # Definir icone e descrição no frame_logo
    o = Image.open(fp='imagens/img_alunos.png')
    r = o.resize(size=(40,40))
    img = ImageTk.PhotoImage(r)
    
    lbl_logo_img = ttk.Label(self.frame_topo, image=img, width=60,
                            compound='left', anchor='nw')
    lbl_logo_img.image = img
    lbl_logo_img.place(x=340, y=7)
    lbl_logo_txt = ttk.Label(self.frame_topo, text='Escola de Desenvolvimento Python', width=60,
                            compound='left', anchor='w',
                            font=FONTE_LOGO, foreground=COR_FONTE)
    lbl_logo_txt.place(x=400, y=12)

    # Definir tema styles para as abas (bootstrap)
    self.style.theme_create(
        'padrao', parent='alt', settings={
        'TNotebook':     {'configure': {'tabmargins': [2, 5, 2, 0],
                                        'borderwidth': (0)} },
        'TNotebook.Tab': {'configure': {'padding': [20, 3],
                                        'font': ('JetBrains Mono Bold', 11),
                                        'borderwidth': (2)},
        'map':           {'foreground': [('selected', COR_FONTE)],
        'expand':        [('selected', [0, 0, 0, 0])] } } } )
    
    self.style.theme_use('padrao')
    
    # Criação das abas (bootstrap) no frame_abas
    Abas = ttk.Notebook(self.frame_meio)
    aba_alunos = ttk.Frame(Abas)
    aba_cursos = ttk.Frame(Abas)
    aba_turmas = ttk.Frame(Abas)
    Abas.add(aba_alunos, text='Alunos')
    Abas.add(aba_cursos, text='Cursos')
    Abas.add(aba_turmas, text='Turmas')
    Abas.pack(expand = 1, fill ='both') 

    # Criar label de mensagem para o usuário no frame_msg
    lbl_msg_txt = ttk.Label(self.frame_rodape, width=40,anchor='w', text="Sem mensagens.")
    lbl_msg_txt.place(x=0, y=0)

    # Criação dos widgets alunos nas abas
    alunos = AbaAlunos(aba_alunos, self.style)
    #cursos = CriarFramesAlunos(aba_cursos) -> à implementar
    #turmas = CriarFramesAlunos(aba_turmas) -> à implementar