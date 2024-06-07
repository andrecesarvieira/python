# Objetivo: Criação da tabela TURMAS
#           CRUD da tabela TURMAS
# Autor...: André Vieira
# Data....: 2/6/24

import os
import sqlite3

class CrudTabelaTurmas():
  local = f'(' + __qualname__ + ' -> ' + os.path.basename(__file__) + ')'

  def inserir(self, con, dados):
    try:
      with con:
        cur = con.cursor()
        query = """INSERT INTO TURMAS (nome, curso, data_inicio)
                   VALUES (?, ?, ?)"""
        cur.execute(query, dados)
    except sqlite3.Error as erro:
      print (f'Erro ao inserir na tabela TURMAS: {erro}, {self.local}')

  def ler(self, con) -> list: 
    try:
      with con:
        tabela = []
        cur = con.cursor()
        cur.execute('SELECT * FROM TURMAS')
        res = cur.fetchall()
        for i in res:
          tabela.append(i)
    except sqlite3.Error as erro:
      print (f'Erro ao ler a tabela TURMAS: {erro}, {self.local}')
    else:
      return tabela
  
  def atualizar(self, con, dados):
    try:
      with con:
        cur = con.cursor()
        query = """UPDATE TURMAS
                   SET nome=?, curso=?, data_inicio=?
                   WHERE id=?"""
        cur.execute(query, dados)
    except sqlite3.Error as erro:
      print (f'Erro ao atualizar na tabela TURMAS: {erro}, {self.local}')

  def deletar(self, con, id):
      try:
        with con:          
          cur = con.cursor()
          query = 'DELETE FROM TURMAS WHERE id=?'
          cur.execute(query, (id,))
      except sqlite3.Error as erro:
          print(f'Erro ao deletar na tabela TURMAS: {erro}, {self.local}')

class CriarTabelaTurmas():
  local = f'(' + __qualname__ + ' -> ' + os.path.basename(__file__) + ')'  

  def criar(self, con):
    try:
      with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS TURMAS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    curso TEXT,
                    data_inicio DATE,
                    FOREIGN KEY (curso) REFERENCES CURSOS (nome)
                    ON UPDATE CASCADE ON DELETE CASCADE)""")
    except sqlite3.Error as erro:
      print (f'Erro ao criar tabela TURMAS: {erro}, {self.local}')
      return erro
    else:
      print('Tabela TURMAS pronta.')
      return None