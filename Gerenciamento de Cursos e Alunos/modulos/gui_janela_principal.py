# Objetivo: Gerenciar a GUI do aplicativo
# Autor...: André Vieira
# Data....: 4/6/24 -> desenvolvimento

import customtkinter
from PIL import Image

from modulos.scr_padronizacao import cor
from modulos.scr_padronizacao import fonte
from modulos.msg_notificacao import Notificacao
from modulos.gui_aba_alunos import AbaAlunos
from modulos.gui_aba_cursos import AbaCursos
from modulos.gui_aba_turmas import AbaTurmas

class JanelaPrincipal():
    def __init__(self, root):
        self.root = root
        self.root.title('Gerenciamento de Escola')
        self.root.resizable(False, False)

        # Centralizar o início da aplicação, considerando a resolução do sistema
        LARGURA = 1600
        ALTURA = 900
        MENU_DO_WINDOWS = 80
        tela_largura = self.root.winfo_screenwidth()
        tela_altura = self.root.winfo_screenheight() - MENU_DO_WINDOWS
        x_coordenada = int((tela_largura / 2) - (LARGURA / 2))
        y_coordenada = int((tela_altura / 2) - (ALTURA / 2))
        self.root.geometry(f'{LARGURA}x{ALTURA}+{x_coordenada}+{y_coordenada}')

        # Definir tema de acordo com as configurações do sistema operacional
        customtkinter.set_appearance_mode('System')
        customtkinter.set_default_color_theme('dark-blue')

        self.criar_frames()
        self.criar_widgets()
        Notificacao.criar(self.frame_rodape, ' - Sistema no ar. Bom trabalho!')
    
    def criar_frames(self):
        # Criar frames logo e menu
        self.frame_topo = customtkinter.CTkFrame(master=self.root,height=80,
                                                 bg_color=cor(1), fg_color=cor(1))
        self.frame_topo.pack(fill='x', expand=True)

        self.frame_meio = customtkinter.CTkFrame(self.root,height=780)
        self.frame_meio.pack(fill='x', expand=True)
        
        self.frame_rodape = customtkinter.CTkFrame(self.root,height=40)
        self.frame_rodape.pack(fill='x', expand=True)

    def criar_widgets(self):
        # Definir icone e descrição no frame_logo
        img = customtkinter.CTkImage(Image.open(r'imagens/img_alunos.png'), size=(50, 50))
        lbl_logo_img = customtkinter.CTkLabel(master=self.frame_topo, image=img, text='')
        lbl_logo_img.place(x=430, y=15)
        lbl_logo_txt = customtkinter.CTkLabel(master=self.frame_topo, text='Escola de Desenvolvimento Python',
                                              font=fonte(1), text_color=cor(2))
        lbl_logo_txt.place(x=500, y=18)

        # Criação das abas (bootstrap) no frame_abas        
        abas = customtkinter.CTkTabview(master=self.frame_meio)
        abas._segmented_button.configure(font=fonte(2))
        abas.pack(fill='both', expand=True)

        aba_alunos = abas.add('Alunos')
        aba_cursos = abas.add('Cursos')
        aba_turmas = abas.add('Turmas')
        
        abas.set('Alunos')

        # Criação dos frames alunos nas abas
        alunos = AbaAlunos(aba_alunos)
        cursos = AbaCursos(aba_cursos)
        turmas = AbaTurmas(aba_turmas)
