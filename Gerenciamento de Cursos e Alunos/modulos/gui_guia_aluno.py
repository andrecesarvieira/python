# Objetivo: Criação das guia alunos
# Autor...: André Vieira
# Data....: 5/6/24 -> desenvolvimento

from tkinter import ttk

class AbaAlunos():
  def __init__(self, guia_alunos, style):
    self.guia_alunos = guia_alunos
    self.style = style

    for widgets in self.guia_alunos.winfo_children():
      widgets.destroy()

    self.criar_frames()
    #self.criar_widgets()

  def criar_frames(self):
    
    #Para teste
    self.style.configure('Frame1.TFrame', background='red')
    self.style.configure('Frame2.TFrame', background='blue')
    self.style.configure('Frame3.TFrame', background='green')
    
    # Criar frames na guia alunos
    self.frame_menu = ttk.Frame(self.guia_alunos, width=1272, height=40, style='Frame1.TFrame',
                                relief="raised", border=0, borderwidth=0)
    self.frame_menu.grid(row=1, column=0, padx=3, pady=0, sticky='nsew')
    self.frame_corpo = ttk.Frame(self.guia_alunos, width=1272, height=280, style='Frame2.TFrame')
    self.frame_corpo.grid(row=2, column=0, padx=3, pady=0, sticky='nsew')
    self.frame_grade = ttk.Frame(self.guia_alunos, width=1272, height=280, style='Frame3.TFrame',
                                 relief='raised', border=0, borderwidth=0)
    self.frame_grade.grid(row=3, column=0, padx=3, pady=0, sticky='nsew')

  def criar_widgets(self):
    pass

