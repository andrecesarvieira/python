# Objetivo: Criação das tabelas do banco de dados
# Autor...: André Vieira
# Data....: 3/6/24

import os
import sys
from db.db_conexao import Conectar_Banco_de_Dados
from db.db_tabela_alunos import Criar_Tabela_Alunos
from db.db_tabela_cursos import Criar_Tabela_Cursos
from db.db_tabela_turmas import Criar_Tabela_Turmas


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == '__main__':

  alunos = Criar_Tabela_Alunos()
  cursos = Criar_Tabela_Cursos()
  turmas = Criar_Tabela_Turmas()

  c = Conectar_Banco_de_Dados()
 
  c.conectar()
 
  alunos.criar(c.con)
  cursos.criar(c.con)
  turmas.criar(c.con)
 
  c.encerrar(c.con)