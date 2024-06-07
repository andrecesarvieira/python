# Objetivo: Script principal da aplicação Gerenciamento de Cursos e Alunos
# Autor...: André Vieira
# Data....: 3/6/24

import customtkinter

from modulos.gui_janela_principal import JanelaPrincipal
from modulos.db_tabelas_criar import CriarTabelasDB

def main():
  root = customtkinter.CTk()
  JanelaPrincipal(root)
  root.mainloop()

if __name__ == '__main__':
  CriarTabelasDB()
  main()