# Módulo para chamar a criação de todas as tabelas do banco de dados
# André Vieira
# 3/6/24

import os
import sys

import db.db_criar_tabela_alunos
import db.db_criar_tabela_cursos
import db.db_criar_tabela_turmas

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import db

if __name__ == '__main__':
  db.db_criar_tabela_alunos.Criar_Tabela_Alunos()
  db.db_criar_tabela_cursos.Criar_Tabela_Cursos()
  db.db_criar_tabela_turmas.Criar_Tabela_Turmas()