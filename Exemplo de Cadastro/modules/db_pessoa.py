# Objetivo: Criação da tabela
#           CRUD
# Autor...: André Vieira
# Data....: 2/6/24

import os
import sqlite3

class CrudTabela:
  local = f'({__qualname__} -> {os.path.basename(__file__)})'

  def inserir(self, con, dados):
    try:
      with con:
        cur = con.cursor()
        query = """INSERT INTO PESSOA (cpf, nome, email, celular, sexo, foto,
                   data_nascimento)
                   VALUES (?, ?, ?, ?, ?, ?, ?)"""
        cur.execute(query, dados)
    except sqlite3.Error as erro:
      print (f'Erro ao inserir na tabela PESSOA: {erro}, {self.local}')
      return erro      

  def ler(self, con) -> list: 
    try:
      with con:
        tabela = []
        cur = con.cursor()
        cur.execute('SELECT * FROM PESSOA')
        res = cur.fetchall()
        for i in res:
          tabela.append(i)
    except sqlite3.Error as erro:
      print (f'Erro ao ler a tabela PESSOA: {erro}, {self.local}')
      return erro
    else:
      return tabela
  
  def atualizar(self, con, dados):
    try:
      with con:
        cur = con.cursor()
        query = """UPDATE PESSOA
                   SET cpf=?, nome=?, email=?, celular=?, sexo=?, foto=?,
                       data_nascimento=?
                   WHERE id=?"""
        cur.execute(query, dados)
    except sqlite3.Error as erro:
      print (f'Erro ao atualizar na tabela PESSOA: {erro}, {self.local}')
      return erro      

  def deletar(self, con, id):
      try:
        with con:          
          cur = con.cursor()
          query = 'DELETE FROM PESSOA WHERE id=?'
          cur.execute(query, (id,))
      except sqlite3.Error as erro:
          print(f'Erro ao deletar na tabela PESSOA: {erro}, {self.local}')
          return erro

class CriarTabela:
  local = f'({__qualname__} -> {os.path.basename(__file__)})'
  
  def criar(self, con):
    try:
      with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS PESSOA(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cpf TEXT,
                    nome TEXT,
                    email TEXT,
                    celular TEXT,
                    sexo TEXT,
                    foto TEXT,
                    data_nascimento DATE) """)
    except sqlite3.Error as erro:
      print (f'Erro ao criar tabela PESSOA: {erro}, {self.local}')
      return erro
    else:
      print('Tabela PESSOA pronta.')
      return None