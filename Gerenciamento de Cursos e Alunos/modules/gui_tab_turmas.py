# Objetivo: Criação das guia alunos
# Autor...: André Vieira
# Data....: 5/6/24 -> desenvolvimento

import customtkinter
from modules.gui_tab_frames import Frames

class TabTurmas():
    def __init__(self, tab):
        self.tab = tab
        self.criar_frames()
        self.criar_widgets()

    def criar_frames(self):
        # Criar frames na tab alunos
        self.frm = Frames.criar(self.tab)

    def criar_widgets(self):
        # Criar widgets apenas de retornou frame criado
        if self.frm != None:
            self.lbl = customtkinter.CTkEntry(master=self.frm)
            self.lbl.place(x=100, y=100)
