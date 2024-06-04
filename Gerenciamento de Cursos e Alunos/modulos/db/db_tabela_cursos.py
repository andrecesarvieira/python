# Objetivo: Criação da tabela CURSOS
#           CRUD da tabela CURSOS
# Autor...: André Vieira
# Data....: 2/6/24

import os
import sys
import sqlite3
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Crud_Tabela_Cursos():
  pass

class Criar_Tabela_Cursos():

  local = "(" + __qualname__ + " -> " + os.path.basename(__file__) + ")"  

  def criar(self, con):

    self.con = con

    try:
      with self.con:
        cur = self.con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS CURSOS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    duracao TEXT,
                    preco REAL
        )""")
    except sqlite3.Error as erro:
      print ("Erro ao criar tabela CURSOS: ", erro, self.local)
    else:
      print("Tabela CURSOS criada OK")