# Objetivo: Script principal da aplicação Gerenciamento de Cursos e Alunos
# Autor...: André Vieira
# Data....: 3/6/24

import customtkinter

from modules.gui_main import Main

def main():
  root = customtkinter.CTk()
  Main(root)
  root.mainloop()

if __name__ == '__main__':
  main()