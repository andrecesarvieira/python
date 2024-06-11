# Objetivo: Chama conexão e criação de tabelas
# Autor...: André Vieira
# Data....: 3/6/24

from modules.db_conexao import ConectarBancodeDados
from modules.db_pessoa import CriarTabela

class CriarTabelasDB:
  def criar() -> tuple:
    c = ConectarBancodeDados()
    conexao = c.conectar()    

    if conexao:
      pessoa = CriarTabela()
      rc1 = pessoa.criar(conexao)
      c.encerrar(conexao)
      conexao = None
          
    return conexao, rc1