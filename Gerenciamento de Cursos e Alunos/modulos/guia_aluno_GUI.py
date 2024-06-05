# Objetivo: Criação das guia alunos
# Autor...: André Vieira
# Data....: 5/6/24 -> desenvolvimento

from tkinter import ttk

class GuiaAlunos():
  def __init__(self, guia_alunos, style):
    self.guia_alunos = guia_alunos
    self.style = style

    self.criar_frames()
    self.criar_widgets()

  def criar_frames(self):
    
    #Para teste
    self.style.configure('Frame1.TFrame', background='red')
    self.style.configure('Frame2.TFrame', background='blue')
    self.style.configure('Frame3.TFrame', background='green')
    
    # Criar frames na guia alunos
    self.frame_detalhes = ttk.Frame(self.guia_alunos, width=750, height=301, style='Frame1.TFrame')
    self.frame_detalhes.grid(row=2, column=0, columnspan=1, pady=2, padx=1, sticky="nsew")
    self.frame_crud = ttk.Frame(self.guia_alunos, width=100, height=298, style='Frame2.TFrame')
    self.frame_crud.grid(row=2, column=1, columnspan=1, pady=2, padx=1, sticky="nsew")
    self.frame_grade = ttk.Frame(self.guia_alunos, width=1276, height=301, style='Frame3.TFrame',
                                 relief="flat", border=0, borderwidth=0)
    self.frame_grade.grid(row=3, column=0, columnspan=2,pady=0, padx=1, sticky="nsew")

  def criar_widgets(self):
    # Destruir
    for widgets in self.frame_detalhes.winfo_children():
      widgets.destroy()
