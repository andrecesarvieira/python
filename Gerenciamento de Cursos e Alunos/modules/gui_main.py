# Objetivo: Gerenciar a GUI do aplicativo
# Autor...: André Vieira
# Data....: 4/6/24 -> desenvolvimento

import sys
import customtkinter
from PIL import Image

from modules.scr_padronizacao import cor
from modules.scr_padronizacao import fonte
from modules.db_criar import CriarTabelasDB
from modules.msg_notificacao import Notificacao
from modules.gui_tab_alunos import TabAlunos
from modules.gui_tab_cursos import TabCursos
from modules.gui_tab_turmas import TabTurmas

class Main():
    def __init__(self, root):
        self.root = root

        self.criar_janela()
        self.criar_frames()
        self.criar_widgets()
        Notificacao.criar(self.frm_rodape, ' - Sistema no ar. Bom trabalho!')
        self.banco_de_dados()

    def criar_janela(self):
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

    def criar_frames(self):
        # Criar frames
        self.frm_topo = customtkinter.CTkFrame(master=self.root,height=80,
                                               bg_color=cor(1), fg_color=cor(1))
        self.frm_corpo = customtkinter.CTkFrame(self.root,height=790)
        self.frm_rodape = customtkinter.CTkFrame(self.root,height=30)

        self.frm_topo.pack(fill='x', expand=False)
        self.frm_corpo.pack(fill='both', expand=True)
        self.frm_rodape.pack(fill='x', expand=False)

    def criar_widgets(self):
        # Definir icone e descrição no frame_logo
        img = customtkinter.CTkImage(Image.open(r'pics/img_alunos.png'), size=(50, 50))
        lbl_logo_img = customtkinter.CTkLabel(master=self.frm_topo, image=img, text='')
        lbl_logo_txt = customtkinter.CTkLabel(master=self.frm_topo, text='Escola de Desenvolvimento Python',
                                              font=fonte(1), text_color=cor(2))
        
        lbl_logo_img.place(x=460, y=15)
        lbl_logo_txt.place(x=530, y=18)

        # Criar das tabs (bootstrap) no frame_tabs        
        self.tab = customtkinter.CTkTabview(master=self.frm_corpo, command=self.tab_clique)
        self.tab_cursos = self.tab.add('Cursos')
        self.tab_turmas = self.tab.add('Turmas')
        self.tab_alunos = self.tab.add('Alunos')
        self.tab._segmented_button.configure(font=fonte(2), height=50)
        
        self.tab.pack(fill='both', expand=True)
                
        # Carrega tab Cursos ao inciar o aplicativo
        self.tab.set('Cursos')
        Main.tab_clique(self)

    def tab_clique(self):
        # Criação dos frames alunos nas abas
        tab = self.tab.get()

        match tab:
            case 'Cursos':
                TabCursos(self.tab_cursos)
            case 'Turmas':
                TabTurmas(self.tab_turmas)
            case 'Alunos':
                TabAlunos(self.tab_alunos)
    
    def banco_de_dados(self):
        res = CriarTabelasDB.criar()
        rc1, rc2, rc3, rc4 = res
        
        if any(i is not None for i in [rc1, rc2, rc3, rc4]):
            msg = ' - Problema com banco de dados. O programa será fechado.'
            Notificacao.criar(self.frm_rodape, msg)
            self.root.after(5000, self.encerrar_app)

    def encerrar_app(self):
        self.root.destroy()