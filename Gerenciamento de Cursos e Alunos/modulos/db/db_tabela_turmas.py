# Objetivo: Criação da tabela TURMAS
#           CRUD da tabela TURMAS
# Autor...: André Vieira
# Data....: 2/6/24

import os
import sys
import sqlite3
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class CrudTabelaTurmas():
  pass

class CriarTabelaTurmas():
  
  local = f"(" + __qualname__ + " -> " + os.path.basename(__file__) + ")"  

  def criar(self, con):

    self.con = con

    try:
      with self.con:
        cur = self.con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS TURMAS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    curso TEXT,
                    data_inicio DATE,
                    FOREIGN KEY (curso) REFERENCES CURSOS (nome)
                    ON UPDATE CASCADE ON DELETE CASCADE)""")
    except sqlite3.Error as erro:
      print ("Erro ao criar tabela TURMAS: ", erro, self.local)
    else:
      print("Tabela TURMAS criada.")