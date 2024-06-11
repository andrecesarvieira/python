# Objetivo: Gerenciar a GUI do aplicativo
# Autor...: André Vieira
# Data....: 4/6/24 -> desenvolvimento

import customtkinter

from PIL import Image
from custom_hovertip import CustomTooltipLabel

from modules.db_criar import CriarTabelasDB as DB
from modules.msg_notificacao import Notificacao as Nt
from modules.scr_padronizacao import fonte
from modules.gui_tab_alunos import TabAlunos
from modules.gui_tab_cursos import TabCursos
from modules.gui_tab_turmas import TabTurmas

class MainGui:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title('UI Moderna Tkinter')
        self.root.resizable(False, False)

        self.centralizar_janela()
        self.frame_topo()
        self.frame_principal()
        self.frame_rodape()
        self.frame_menu_compactado()
        self.banco_de_dados()

        self.root.mainloop()

    def sair_app(self):
        self.root.destroy()    

    def modo_aparencia(self):
        # Configurações para mudar modo aparência
        tema = customtkinter.get_appearance_mode()
        if tema == 'Dark':
            customtkinter.set_appearance_mode('light')
        else:
            customtkinter.set_appearance_mode('dark')

    def centralizar_janela(self):
        # Centralizar o início da aplicação, considerando a resolução do sistema
        LARGURA = 1600
        ALTURA = 900
        MENU_DO_WINDOWS = 80
        tela_largura = self.root.winfo_screenwidth()
        tela_altura = self.root.winfo_screenheight() - MENU_DO_WINDOWS
        x_coordenada = int((tela_largura / 2) - (LARGURA / 2))
        y_coordenada = int((tela_altura / 2) - (ALTURA / 2))
        self.root.geometry(f'{LARGURA}x{ALTURA}+{x_coordenada}+{y_coordenada}')

    def frame_topo(self):
        # Criar frame de pesquisa no topo
        self.frm_topo = customtkinter.CTkFrame(self.root, height=60, border_width=1, corner_radius=0)
        self.frm_topo.pack(side='top', expand=False, fill='x')
        
        self.widgets_frame_topo()

    def widgets_frame_topo(self):
        def entry_foco():
            self.entry_search.focus()

        lbl_search = customtkinter.CTkLabel(self.frm_topo, height=55, text='Desenvolvimento em Pyhton e CustomTkinter',
                                            font=fonte(1))
        lbl_search.place(x=90, y=4.3)

        lbl_search = customtkinter.CTkLabel(self.frm_topo, text='Pesquisar:', font=fonte(2))
        lbl_search.place(x=1115, y=16)

        self.entry_search = customtkinter.CTkEntry(self.frm_topo, width=400, font=('Arial', 13, 'normal'),
                                                    corner_radius=5, placeholder_text='Tecle "Alt + P" para pesquisar')
        self.entry_search.place(x=1185, y=15)

        # Tecla ESCAPE fecha o menu expandido
        self.root.bind('<Alt-p>', lambda event: entry_foco())
        self.root.bind('<Alt-P>', lambda event: entry_foco())

    def frame_principal(self):
        # Criar frame principal
        self.frm_main = customtkinter.CTkFrame(self.root, border_width=0, corner_radius=0)
        self.frm_main.pack(expand=True, fill='both')
        
        self.widgets_frame_principal()

    def widgets_frame_principal(self):
        lbl_main = customtkinter.CTkLabel(self.frm_main, text='UI Moderna CustomTkinter', font=('Arial', 120))
        lbl_main.pack(expand=True)

    def frame_rodape(self):
        self.frm_rodape = customtkinter.CTkFrame(self.root, border_width=0, corner_radius=0, height=30)
        self.frm_rodape.pack(side='bottom', expand=False, fill='x')

    def frame_menu_compactado(self):
        self.frm_hub1 = customtkinter.CTkFrame(self.root, fg_color='gray', height=900, width=60,
                                            border_width=0, corner_radius=0)
        self.frm_hub1.place(x=0, y=0)

        self.widgets_comuns(self.frm_hub1)

    def frame_menu_expandido(self):
        # Frame do menu expandido
        self.frm_hub2 = customtkinter.CTkFrame(self.root, fg_color='gray', height=900, width=250,
                                        border_width=0, corner_radius=0)
        self.frm_hub2.place(x=0, y=0)
       
        self.widgets_menu_expandido()
        self.widgets_comuns(self.frm_hub2)

    def widgets_menu_expandido(self):
        def destruir():
            self.frm_hub2.destroy()

        # Botão fechar -> compactar menu
        img = customtkinter.CTkImage(Image.open('pics//fechar.png'), size=(40, 40))
        btn_hub = customtkinter.CTkButton(self.frm_hub2, image=img, width=50, text='',
                                                border_width=0, corner_radius=0, command=destruir,
                                                fg_color='transparent', hover_color='gray')
        btn_hub.place(x=5, y=5)    
        CustomTooltipLabel(anchor_widget=btn_hub, text='Pressione ESC para fechar', border=1, background='lightgray',
                           width=25, font=('Arial', 9, 'bold'))

        # Label do botão mudar aparência
        lbl_sair = customtkinter.CTkLabel(self.frm_hub2, text = 'Tema claro/escuro', font=fonte(4),
                                        text_color='#1C1C1C')
        lbl_sair.place(x=60, y=797)
        
        # Label do botão Sair
        lbl_sair = customtkinter.CTkLabel(self.frm_hub2, text = 'Sair do programa', font=fonte(4),
                                        text_color='#1C1C1C')
        lbl_sair.place(x=60, y=854)

        # Tecla ESCAPE fecha o menu expandido
        self.root.bind('<Escape>', lambda event: destruir())

    def widgets_comuns(self, frame):
        self.frame = frame

        # Botão abrir -> expandir menu
        img = customtkinter.CTkImage(Image.open('pics//abrir.png'), size=(40, 40))
        btn_hub = customtkinter.CTkButton(self.frm_hub1, image=img, width=50, text='',
                                                border_width=0, corner_radius=0, command=self.frame_menu_expandido,
                                                fg_color='transparent', hover_color='gray')
        btn_hub.place(x=5, y=5)

        # Criar botão trocar modo de aparência
        self.img_modo = customtkinter.CTkImage(light_image=Image.open('pics//mudar_escuro.png'),
                                            dark_image=Image.open('pics//mudar_claro.png'), size=(40, 40))
        self.btn_modo = customtkinter.CTkButton(self.frame, image=self.img_modo, width=50, text='',
                                            border_width=0, corner_radius=0, command=self.modo_aparencia,
                                            fg_color='transparent', hover_color='gray')
        self.btn_modo.place(x=5, y=787)

        # Botão sair do programa
        img_sair = customtkinter.CTkImage(Image.open('pics//sair.png'), size=(40, 40))
        btn_sair = customtkinter.CTkButton(self.frame, image=img_sair, width=50, text='',
                                                border_width=0, corner_radius=0, command=self.sair_app,
                                                fg_color='transparent', hover_color='gray')
        btn_sair.place(x=5, y=845)
    
    def banco_de_dados(self):
        res = DB.criar()
        rc1, rc2, rc3, rc4 = res
        
        # Essa expressão funciona porque o Python avalia None como False e qualquer valor diferente de None como True.
        # Portanto, any() retornará True se pelo menos um dos valores não for None.
        if any([rc1, rc2, rc3, rc4]):
            msg = 'Problema com banco de dados. O programa será fechado.'
            Nt.criar(self.frm_rodape, msg)
            self.root.after(5000, self.sair_app)
        else:
            Nt.criar(self.frm_rodape, 'Sistema no ar. Bom trabalho!')        