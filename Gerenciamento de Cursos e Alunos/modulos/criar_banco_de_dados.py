# Objetivo: Criação das tabelas do banco de dados
#           CRUD da tabela TURMAS
# Autor...: André Vieira
# Data....: 3/6/24

import os
import sys
from db.db_tabela_alunos import Criar_Tabela_Alunos
from db.db_tabela_cursos import Criar_Tabela_Cursos
from db.db_tabela_turmas import Criar_Tabela_Turmas

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == '__main__':
  # Tabela Alunos
  alunos = Conectar_Banco_de_Dados()

  #db.db_tabela_cursos.Criar_Tabela_Cursos()
  #db.db_tabela_turmas.Criar_Tabela_Turmas()