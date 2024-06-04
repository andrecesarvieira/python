# Objetivo: Criação das tabelas do banco de dados
#           CRUD da tabela TURMAS
# Autor...: André Vieira
# Data....: 3/6/24

import os
import sys
import db.db_tabela_alunos
import db.db_tabela_cursos
import db.db_tabela_turmas

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == '__main__':
  db.db_tabela_alunos.Criar_Tabela_Alunos()
  db.db_tabela_cursos.Criar_Tabela_Cursos()
  db.db_tabela_turmas.Criar_Tabela_Turmas()