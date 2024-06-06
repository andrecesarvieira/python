# Objetivo: Gerenciar a GUI do aplicativo
# Autor...: André Vieira
# Data....: 4/6/24 -> desenvolvimento

import customtkinter
from PIL import Image

from modulos.scr_padronizacao import cor
from modulos.scr_padronizacao import fonte
from modulos.msg_notificacao import Notificar
from modulos.gui_aba_aluno import AbaAlunos
# from modulos.guia_cursos_criar import GuiaCursos -> à implementar
# from modulos.guia_turmas_criar import GuiaTurmas -> à implementar

class JanelaPrincipal():
    def __init__(self, root):
        self.root = root
        self.root.title('Gerenciamento de Escola')
        #self.root.resizable(False, False)

        # Centralizar o início da aplicação, considerando a resolução do sistema
        LARGURA = 1280
        ALTURA = 720
        MENU_DO_WINDOWS = 80
        tela_largura = self.root.winfo_screenwidth()
        tela_altura = self.root.winfo_screenheight() - MENU_DO_WINDOWS
        x_coordenada = int((tela_largura / 2) - (LARGURA / 2))
        y_coordenada = int((tela_altura / 2) - (ALTURA / 2))
        self.root.geometry(f'{LARGURA}x{ALTURA}+{x_coordenada}+{y_coordenada}')

        # Definir tema de acordo com as configurações do sistema operacional
        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('dark-blue')

        self.criar_frames()
        self.criar_widgets()
        Notificar(self.frame_rodape, ' - Sistema no ar. Bom trabalho!')
    
    def criar_frames(self):
        # Criar frames logo e menu
        self.frame_topo = customtkinter.CTkFrame(master=self.root,height=50,
                                                 bg_color=cor(1), fg_color=cor(1))
        self.frame_topo.pack(fill='both')

        self.frame_meio = customtkinter.CTkFrame(self.root,height=644)
        self.frame_meio.pack(fill='both')
        
        self.frame_rodape = customtkinter.CTkFrame(self.root,height=26)
        self.frame_rodape.pack(fill='both')

    def criar_widgets(self):
        # Definir icone e descrição no frame_logo
        img = customtkinter.CTkImage(Image.open(r'imagens/img_alunos.png'), size=(35, 35))
        lbl_logo_img = customtkinter.CTkLabel(master=self.frame_topo, image=img, text='')
        lbl_logo_img.place(x=350, y=8)
        lbl_logo_txt = customtkinter.CTkLabel(master=self.frame_topo, text='Escola de Desenvolvimento Python',
                                              font=fonte(1), text_color=cor(2))
        lbl_logo_txt.place(x=400, y=8)

        # Criação das abas (bootstrap) no frame_abas        
        abas = customtkinter.CTkTabview(master=self.frame_meio)
        abas._segmented_button.configure(font=fonte(2))
        aba_aluno = abas.add('Alunos')
        aba_cursos = abas.add('Cursos')
        aba_turmas = abas.add('Turmas')
        abas.pack(expand=1, fill='both')

        # Criação dos widgets alunos nas abas
        #alunos = AbaAlunos(aba_aluno)
        #cursos = AbaAlunos(abas('Cursos'))
        #turmas = AbaAlunos(abas('Turmas'))
