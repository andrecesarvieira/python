# Objetivo: Criação das tabelas do banco de dados
# Autor...: André Vieira
# Data....: 3/6/24

import os
import sys
from modules.db_conexao import ConectarBancodeDados
from modules.db_alunos import CriarTabelaAlunos
from modules.db_cursos import CriarTabelaCursos
from modules.db_turmas import CriarTabelaTurmas

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class CriarTabelasDB():
  def __init__(self):
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
      print('Não foi possível criar as tabelas do banco de dados.')