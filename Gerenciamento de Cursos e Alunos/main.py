# Objetivo: Script principal da aplicação Gerenciamento de Cursos e Alunos
# Autor...: André Vieira
# Data....: 3/6/24

import tkinter as tk

from tkinter import ttk
from tkinter import font
from modulos.gui_janela_principal import JanelaPrincipal
from modulos.db_tabelas_criar import CriarTabelasDB

def main():
  root = tk.Tk()
  JanelaPrincipal(root)
  root.mainloop()

if __name__ == '__main__':
  CriarTabelasDB()
  main()