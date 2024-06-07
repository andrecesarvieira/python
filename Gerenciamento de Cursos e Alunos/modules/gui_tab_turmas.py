# Objetivo: Criação das guia alunos
# Autor...: André Vieira
# Data....: 5/6/24 -> desenvolvimento

import customtkinter
from modules.gui_tab_frames import Frames

class TabTurmas():
    def __init__(self, aba):
        self.aba = aba
        self.criar_frames()
        self.criar_widgets()

    def criar_frames(self):
        # Criar CTkFrames na guia alunos
        f = Frames.criar(self.aba)
        self.frame_menu, self.frame_corpo,self.frame_grade = f

    def criar_widgets(self):
        self.lbl = customtkinter.CTkEntry(master=self.frame_corpo)
        self.lbl.place(x=100, y=100)
