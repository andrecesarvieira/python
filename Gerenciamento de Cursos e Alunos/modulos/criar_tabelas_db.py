# Objetivo: Criação das tabelas do banco de dados
# Autor...: André Vieira
# Data....: 3/6/24

import os
import sys
from db.db_conexao import ConectarBancodeDados
from db.db_tabela_alunos import CriarTabelaAlunos
from db.db_tabela_cursos import CriarTabelaCursos
from db.db_tabela_turmas import CriarTabelaTurmas

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
  c = ConectarBancodeDados()
  conexao = c.conectar()
  
  if conexao:
    alunos = CriarTabelaAlunos()
    cursos = CriarTabelaCursos()
    turmas = CriarTabelaTurmas()
    alunos.criar(conexao)
    cursos.criar(conexao)
    turmas.criar(conexao)
    c.encerrar(conexao)
  else:
    print("Não foi possível criar as tabelas do banco de dados.")

if __name__ == "__main__":
  main()