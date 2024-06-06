# Objetivo: Criação das guia alunos
# Autor...: André Vieira
# Data....: 5/6/24 -> desenvolvimento

import customtkinter

class AbaAlunos():
    def __init__(self, aba):
        self.aba = aba
        self.criar_frames()
        self.criar_widgets()

    def criar_frames(self):

        # Criar CTkFrames na guia alunos
        self.frame_menu = customtkinter.CTkFrame(self.aba, height=40)
        self.frame_menu.pack(fill="x", expand=True)
        
        self.frame_corpo = customtkinter.CTkFrame(self.aba, height=290)
        self.frame_corpo.pack(fill="x", expand=True)
        
        self.frame_grade = customtkinter.CTkFrame(self.aba, height=260)
        self.frame_grade.pack(fill="x", expand=True)

    def criar_widgets(self):
        self.lbl = customtkinter.CTkEntry(master=self.frame_corpo)
        self.lbl.place(x=100, y=100)
