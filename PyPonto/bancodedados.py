import os, sys, sqlite3

from PyQt6.QtWidgets import QMessageBox
from datetime import datetime
from calculos import Calculos

# Determina o caminho base dependendo do ambiente de execução
if getattr(sys, 'frozen', False):
    # Executando a partir do executável compilado
    base_path = os.path.dirname(sys.executable)
else:
    # Executando a partir do código fonte
    base_path = os.path.dirname(os.path.abspath(__file__))

# Define o nome do arquivo do banco de dados por mês
nome_db = f"{datetime.now().strftime('%Y%m')}_ponto.db"

# Define o caminho absoluto para o banco de dados
db_path = os.path.join(base_path, nome_db)

class BancoDeDados:
    calc = Calculos()

    # Abrir banco de dados
    conn = sqlite3.connect(db_path)

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ponto (
                data DATE PRIMARY KEY,
                entrada TEXT,
                almoco TEXT,
                retorno TEXT,
                saida TEXT,
                manha TEXT,
                tarde TEXT,
                horas TEXT
            );
        """)
        self.conn.commit()

    def ler_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM ponto ORDER BY data DESC")
        return cursor.fetchall()

    def ler_tabela_data(self, dia):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM ponto WHERE data = ?", (dia,))
        return cursor.fetchone()

    def atualizar_tabela(self, campo, registro):
        cursor = self.conn.cursor()

        match campo:
            case 1:
                cursor.execute("INSERT INTO ponto VALUES (?, ?, ?, ?, ?, ?, ?, ?)", registro)
            case 2:
                cursor.execute("UPDATE ponto SET entrada = ? WHERE data = ?", (registro[1], registro[0]))
            case 3:
                cursor.execute("UPDATE ponto SET almoco = ? WHERE data = ?", (registro[2], registro[0]))
            case 4:
                cursor.execute("UPDATE ponto SET retorno = ?, manha = ? WHERE data = ?", (registro[3], registro[5], registro[0]))
            case 5:
                cursor.execute("UPDATE ponto SET saida = ?, tarde = ?, horas = ? WHERE data = ?", (registro[4], registro[6], registro[7], registro[0]))

        self.conn.commit()
    
    def excluir_registro(self, chave):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM ponto WHERE data = ?", (chave,))
        try:
            self.conn.commit()
        except Exception as e:
            QMessageBox.warning(None, "Aviso", "Erro ao excluir o registro")
    
    def fechar_banco(self):
        self.conn.close()