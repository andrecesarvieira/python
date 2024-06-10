# Objetivo: Criação da tabela CURSOS
#           CRUD da tabela CURSOS
# Autor...: André Vieira
# Data....: 2/6/24

import os
import sqlite3

class CrudTabelaCursos:
  local = f'({__qualname__} -> {os.path.basename(__file__)})'

  def inserir(self, con, dados):
    try:
      with con:
        cur = con.cursor()
        query = """INSERT INTO CURSOS (nome, duracao, preco)
                   VALUES (?, ?, ?)"""
        cur.execute(query, dados)
    except sqlite3.Error as erro:
      print (f'Erro ao inserir na tabela CURSOS: {erro}, {self.local}')
      
  def ler(self, con) -> list: 
    try:
      with con: 
        tabela = []
        cur = con.cursor()
        cur.execute('SELECT * FROM CURSOS')
        res = cur.fetchall()
        for i in res:
          tabela.append(i)
    except sqlite3.Error as erro:
      print (f'Erro ao ler a tabela CURSOS: {erro}, {self.local}')
    else:
      return tabela
  
  def atualizar(self, con, dados):
    try:
      with con:
        cur = con.cursor()
        query = """UPDATE CURSOS
                   SET nome=?, duracao=?, preco=?
                   WHERE id=?"""
        cur.execute(query, dados)
    except sqlite3.Error as erro:
      print (f'Erro ao atualizar na tabela CURSOS: {erro}, {self.local}')

  def deletar(self, con, id):
      try:
        with con:          
          cur = con.cursor()
          query = 'DELETE FROM CURSOS WHERE id=?'
          cur.execute(query, (id,))
      except sqlite3.Error as erro:
          print(f'Erro ao deletar na tabela CURSOS: {erro}, {self.local}')

class CriarTabelaCursos:
  local = f'({__qualname__} -> {os.path.basename(__file__)})'

  def criar(self, con):
    try:
      with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS CURSOS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    duracao TEXT,
                    preco REAL
        )""")
    except sqlite3.Error as erro:
      print (f'Erro ao criar tabela CURSOS: {erro}, {self.local}')
      return erro
    else:
      print('Tabela CURSOS pronta.')
      return None