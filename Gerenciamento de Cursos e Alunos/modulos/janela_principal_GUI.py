# Objetivo: Gerenciar a GUI do aplicativo
# Autor...: André Vieira
# Data....: 4/6/24 -> desenvolvimento

import tkinter as tk
#import sv_ttk -> à implementar

from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

from modulos.guia_aluno_GUI import GuiaAlunos
#from modulos.guia_cursos_criar import GuiaCursos -> à implementar
#from modulos.guia_turmas_criar import GuiaTurmas -> à implementar

class JanelaPrincipal():
  def __init__(self, root):
    self.root = root
    self.root.title("Gerenciamento de Cursos e Alunos")
    self.root.resizable(False, False)

    # Centralizar a janela conforme resolução do monitor
    LARGURA = 1280
    ALTURA = 720
    MENU_DO_WINDOWS = 80
    tela_largura = self.root.winfo_screenwidth()
    tela_altura = self.root.winfo_screenheight() - MENU_DO_WINDOWS
    x_coordenada = int((tela_largura / 2) - (LARGURA / 2))
    y_coordenada = int((tela_altura / 2) - (ALTURA / 2))
    self.root.geometry(f"{LARGURA}x{ALTURA}+{x_coordenada}+{y_coordenada}")

    # Definir tema -> à implementar
    #sv_ttk.set_theme("light")
    #root.tk.call('source', 'temas/forest-light.tcl')
    #ttk.Style().theme_use('forest-light')

    self.criar()

  def criar(self):  
    # Criar frames logo e menu
    frame_logo = ttk.Frame(self.root, width=1276, height=72, relief="raised")
    frame_logo.grid(row=0, column=0, columnspan=2, pady=2, padx=1, sticky="nsew")
    frame_menu = ttk.Frame(self.root, width=1276, height=60)
    frame_menu.grid(row=1, column=0, columnspan=2, pady=0, padx=1, sticky="nsew")

    # Definir cores e fonte
    COR_FONTE = "#0E2B4A"
    FONTE_LOGO = font.Font(family='JetBrains Mono ExtraBold', name='logo', size=18, weight='normal')

    # Decorar frame logo com icone e descrição
    o = Image.open(fp="imagens/img_alunos.png")
    r = o.resize(size=(40,40))
    img = ImageTk.PhotoImage(r)
    
    lbl_img = ttk.Label(frame_logo, image=img, width=40,
                            compound="left", anchor="nw")
    lbl_img.image = img
    lbl_img.place(x=350, y=15)
    lbl_txt = ttk.Label(frame_logo, text="Gerenciamento de Cursos e Alunos", width=32,
                            compound="center", anchor="center",
                            font=FONTE_LOGO,
                            foreground=COR_FONTE)
    lbl_txt.place(x=400, y=22)

    # Definir ttk styles para o bootstrap
    style = ttk.Style(self.root)
    style.theme_create(
        "padrao", parent="alt", settings={
        "TNotebook":     {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [20, 3],
                                        "font": ('JetBrains Mono Bold', 11),
                                        "borderwidth": (2)},
        "map":           {"foreground": [("selected", COR_FONTE)],
        "expand":        [("selected", [0, 0, 0, 0])] } } } )
    
    style.theme_use("padrao")

    # Criação das guias (bootstrap) no frame menu
    Guias = ttk.Notebook(frame_menu)
    guia_alunos = ttk.Frame(Guias)
    guia_cursos = ttk.Frame(Guias)
    guia_turmas = ttk.Frame(Guias)
    Guias.add(guia_alunos, text="Alunos")
    Guias.add(guia_cursos, text="Cursos")
    Guias.add(guia_turmas, text="Turmas")
    Guias.pack(expand = 1, fill ="both") 

    # Criação dos widgets alunos
    alunos = GuiaAlunos(guia_alunos, style)
    #cursos = CriarFramesAlunos(guia_cursos) -> à implementar
    #turmas = CriarFramesAlunos(guia_turmas) -> à implementar