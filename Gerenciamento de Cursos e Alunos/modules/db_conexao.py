# Objetivo: Conectar ao banco de dados
# Autor...: André Vieira
# Data....: 3/6/24

import os
import sqlite3

class ConectarBancodeDados:
  local = f'(' + __qualname__ + ' -> ' + os.path.basename(__file__) + ')'

  def __init__(self):
    self.arquivo = os.path.join('db', 'banco_de_dados.db')
    self.con = None
  
  def conectar(self) -> str:
    try:
      self.con = sqlite3.connect(self.arquivo)
    except sqlite3 as erro:
      print('Erro de conexão com banco de dados: ', erro, self.local)
      return erro
    else:
      print('Conexão com banco de dados realizada.')
      return self.con

  def encerrar(self, con):
    try:
      con.close()
    except sqlite3.Error as erro:
      print ('Erro ao tentar fechar o banco de dados', erro, self.local)
      return erro
    else:
      print ('Conexão com banco de dados encerrada.')
      return None