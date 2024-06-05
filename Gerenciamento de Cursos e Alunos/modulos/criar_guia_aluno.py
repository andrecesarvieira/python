# Objetivo: Criação das guia alunos
# Autor...: André Vieira
# Data....: 5/6/24 -> desenvolvimento

from tkinter import ttk

class GuiaAlunos():
  def __init__(self, guia_alunos):
    self.guia_alunos = guia_alunos
    self.criar_frames_alunos()
    self.criar_widgets_alunos()

  def criar_frames_alunos(self):
    # Criar frames na guia alunos
    self.frame_detalhes = ttk.Frame(self.guia_alunos, width=750, height=298, style="Padrao.TFrame")
    self.frame_detalhes.grid(row=2, column=0, columnspan=1, pady=2, padx=2, sticky="nsew")
    self.frame_crud = ttk.Frame(self.guia_alunos, width=100, height=298, style="Padrao.TFrame")
    self.frame_crud.grid(row=2, column=1, columnspan=1, pady=2, padx=2, sticky="nsew")
    self.frame_grade = ttk.Frame(self.guia_alunos, width=1276, height=304, style="Padrao.TFrame")
    self.frame_grade.grid(row=3, column=0, columnspan=2,pady=0, padx=2, sticky="nsew")

  def criar_widgets_alunos(self):
    # Destruir
    for widgets in self.frame_detalhes.winfo_children():
      widgets.destroy()
