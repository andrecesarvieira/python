# Objetivo: Script principal da aplicação Gerenciamento de Cursos e Alunos
# Autor...: André Vieira
# Data....: 3/6/24

import customtkinter

from modules.gui_main import Main
from modules.db_criar import CriarTabelasDB

def main():
  root = customtkinter.CTk()
  Main(root)
  root.mainloop()

if __name__ == '__main__':
  CriarTabelasDB()
  main()