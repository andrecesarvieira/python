# Objetivo: Criação das guia alunos
# Autor...: André Vieira
# Data....: 5/6/24 -> desenvolvimento

import customtkinter

class AbaAlunos():
    def __init__(self, aba):
        self.aba = aba

        for widgets in self.aba.winfo_children():
            widgets.destroy()

        self.criar_frames()
        # self.criar_widgets()

    def criar_frames(self):

        # Criar CTkFrames na guia alunos
        self.frame_menu = customtkinter.CTkFrame(self.aba, width=1200, height=40)
        self.frame_menu.pack(fill="both")
        
        self.frame_corpo = customtkinter.CTkFrame(self.aba, width=1200, height=290)
        self.frame_corpo.pack(fill="both")
        
        self.frame_grade = customtkinter.CTkFrame(self.aba, width=1200, height=285)
        self.frame_grade.pack(fill="both")

    def criar_widgets(self):
        pass
