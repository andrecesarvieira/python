# Objetivo: Criação da tabela ALUNOS
#           CRUD da tabela ALUNOS
# Autor...: André Vieira
# Data....: 2/6/24

import os
import sys
import sqlite3
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Crud_Tabela_Alunos():

  local = "(" + __qualname__ + " -> " + os.path.basename(__file__) + ")"

  def ler_tudo(self, con) -> list: 
    
    self.con = con
    
    try:
      with self.con:
        tabela = []
        cur = self.con.cursor()
        cur.execute = "SELECT * FROM ALUNOS"
        res = cur.fetchall
        for i in res:
          tabela.append(i)
    except sqlite3.Error as erro:
      print ("Erro ao ler a tabela ALUNOS: ", erro, self.local)
    else:
      return tabela

  def inserir(self, con, dados):

    self.con = con

    try:
      with self.con:
        cur = self.con.cursor()
        query = "INSERT INTO ALUNOS (nome, duracao, preco) VALUES (?, ?, ?)"
        cur.execute(query, dados)
    except sqlite3.Error as erro:
      print ("Erro ao inserir na tabela ALUNOS: ", erro, self.local)
  
  def atualizar(self, con, dados):
    
    self.con = con
    
    try:
      with self.con:
        cur = self.con.cursor()
        query = "UPDATE ALUNOS SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.execute(query, dados)
    except sqlite3.Error as erro:
      print ("Erro ao atualizar na tabela ALUNOS: ", erro, self.local)

class Criar_Tabela_Alunos():

  local = "(" + __qualname__ + " -> " + os.path.basename(__file__) + ")"
  
  def criar(self, con):
    
    self.con = con

    try:
      with self.con:
        cur = self.con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS ALUNOS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cpf INTEGER,
                    nome TEXT,
                    email TEXT,
                    telefone TEXT,
                    sexo TEXT,
                    foto TEXT,
                    data_nascimento DATE,
                    turma TEXT,
                    FOREIGN KEY (turma) REFERENCES TURMAS (nome)
                    ON DELETE CASCADE)""")
        print("Tabela ALUNOS criada")
    except sqlite3.Error as erro:
      print ("Erro ao criar tabela ALUNOS: ", erro, self.local)