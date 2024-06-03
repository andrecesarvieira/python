import os, sqlite3

class DB_Crud():
    
  # Origem da mensagem
  global arquivo, classe, origem
  classe = __qualname__
  arquivo = os.path.basename(__file__)
  origem = "(" + classe + " -> " + arquivo + ")"

  def __init__():

    global con
    try:
      con = sqlite3.connect("db/banco_de_dados.db")
      print("Conexão com banco de dados OK")
    except sqlite3 as erro:
      print("Erro de conexão com banco de dados: ", erro, origem)  

  def ler_tudo(nome_da_tabela) -> list: 

    try:
      with con:
        tabela = []
        cur = con.cursor()
        cur.execute = "SELECT * FROM " + tabela
        res = cur.fetchall
        for i in res:
          tabela.append(i)
    except sqlite3.Error as erro:
      print ("Erro ao ler a tabela " + nome_da_tabela + ": ", erro, origem)
      return tabela

  def inserir(nome_da_tabela, dados):

 # Tabela de Cursos
    try:
      with con:
        cur = con.cursor()
        query = "INSERT INTO " + nome_da_tabela + "(nome, duracao, preco) \
                 VALUES (?, ?, ?)"
        cur.execute(query, dados)
    except sqlite3.Error as erro:
      print ("Erro ao inserir na tabela " + nome_da_tabela + ": ", erro, origem)

if __name__ == '__main__':
    iniciar = DB_Crud()