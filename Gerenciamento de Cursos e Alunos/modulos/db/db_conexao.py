# Objetivo: Conectar ao banco de dados
# Autor...: André Vieira
# Data....: 3/6/24

import os
import sys
import sqlite3
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Conectar_Banco_de_Dados():
  
  local = "(" + __qualname__ + " -> " + os.path.basename(__file__) + ")"
  
  def conectar(self) -> str:
    
    self.db_arquivo = "db/banco_de_dados.db"
    self.con = None

    try:
      self.con = sqlite3.connect(self.db_arquivo)
    except sqlite3 as erro:
      print("Erro de conexão com banco de dados: ", erro, self.local) 
    else:
      print("Conexão com banco de dados realizada")
      return self.con

  def encerrar(self, con):
    
    self.con = con
    
    try:
      self.con.close()
    except sqlite3.Error as erro:
      print ("Erro ao tentar fechar o banco de dados", erro, self.local)
    else:
      print ("Conexão com banco de dados encerrada")