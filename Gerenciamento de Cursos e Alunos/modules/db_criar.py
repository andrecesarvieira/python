# Objetivo: Chama conexão e criação de tabelas
# Autor...: André Vieira
# Data....: 3/6/24

from modules.msg_notificacao import Notificacao
from modules.db_conexao import ConectarBancodeDados
from modules.db_alunos import CriarTabelaAlunos
from modules.db_cursos import CriarTabelaCursos
from modules.db_turmas import CriarTabelaTurmas

class CriarTabelasDB():
  def criar() -> tuple:
    c = ConectarBancodeDados()
    conexao = c.conectar()    

    if conexao:
      alunos = CriarTabelaAlunos()
      cursos = CriarTabelaCursos()
      turmas = CriarTabelaTurmas()
      rc1 = alunos.criar(conexao)
      rc2 = cursos.criar(conexao)
      rc3 = turmas.criar(conexao)
      c.encerrar(conexao)
      conexao = None
    else:
      conexao = False
    
    return conexao, rc1, rc2, rc3