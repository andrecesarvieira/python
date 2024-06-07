# Objetivo: Criação da tabela ALUNOS
#           CRUD da tabela ALUNOS
# Autor...: André Vieira
# Data....: 2/6/24

import os
import sqlite3

class CrudTabelaAlunos():
  local = f'(' + __qualname__ + ' -> ' + os.path.basename(__file__) + ')'

  def inserir(self, con, dados):
    try:
      with con:
        cur = con.cursor()
        query = """INSERT INTO ALUNOS (cpf, nome, email, telefone, sexo, foto,
                   data_nascimento, turma)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        cur.execute(query, dados)
    except sqlite3.Error as erro:
      print (f'Erro ao inserir na tabela ALUNOS: {erro}, {self.local}')

  def ler(self, con) -> list: 
    try:
      with con:
        tabela = []
        cur = con.cursor()
        cur.execute('SELECT * FROM ALUNOS')
        res = cur.fetchall()
        for i in res:
          tabela.append(i)
    except sqlite3.Error as erro:
      print (f'Erro ao ler a tabela ALUNOS: {erro}, {self.local}')
    else:
      return tabela
  
  def atualizar(self, con, dados):
    try:
      with con:
        cur = con.cursor()
        query = """UPDATE ALUNOS
                   SET nome=?, email=?, telefone=?, sexo=?, foto=?,
                       data_nascimento=?, turma=?
                   WHERE id=?"""
        cur.execute(query, dados)
    except sqlite3.Error as erro:
      print (f'Erro ao atualizar na tabela ALUNOS: {erro}, {self.local}')

  def deletar(self, con, id):
      try:
        with con:          
          cur = con.cursor()
          query = 'DELETE FROM ALUNOS WHERE id=?'
          cur.execute(query, (id,))
      except sqlite3.Error as erro:
          print(f'Erro ao deletar na tabela ALUNOS: {erro}, {self.local}')

class CriarTabelaAlunos():
  local = f'(' + __qualname__ + ' -> ' + os.path.basename(__file__) + ')'
  
  def criar(self, con):
    try:
      with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS ALUNOS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cpf TEXT,
                    nome TEXT,
                    email TEXT,
                    telefone TEXT,
                    sexo TEXT,
                    foto TEXT,
                    data_nascimento DATE,
                    turma TEXT,
                    FOREIGN KEY (turma) REFERENCES TURMAS (nome)
                    ON DELETE CASCADE)""")
    except sqlite3.Error as erro:
      print (f'Erro ao criar tabela ALUNOS: {erro}, {self.local}')
      return erro
    else:
      print('Tabela ALUNOS pronta.')
      return None