import os
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt6.QtCore import Qt, QDate
from datetime import datetime
from pyponto_tela import Ui_MainWindow
from bancodedados import BancoDeDados
from calculos import Calculos

# Caminho absoluto
if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

class MainWindow(QMainWindow):
    db = BancoDeDados()
    ca = Calculos()

    def __init__(self):
        def atribuir_botoes():
            self.ui.btnRegistrar.clicked.connect(self.registrar)
            self.ui.btnExcluir.clicked.connect(self.excluir)
            self.ui.btnInserir.clicked.connect(self.inserir)
            self.ui.btnExportar.clicked.connect(self.exportar)

        super().__init__()
                   
        # Declaração de variáveis
        self.registro = None
        self.campo = None
        self.lista = ["00/00/0000","00:00","00:00","00:00","00:00","00:00","00:00","00:00"]

        # UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Atribuir data do dia para a caixa de texto DATA
        self.ui.data.setDate(QDate.currentDate())

        # Atribuir funções aos cliques
        atribuir_botoes()

        # Banco de dados
        self.db.criar_tabela()
        self.popular_tabela()
    
    def popular_tabela(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

        self.registros = []
        self.registros = self.db.ler_tabela()
        
        if self.registros:
            self.ui.tableWidget.setRowCount(len(self.registros))
            self.ui.tableWidget.setColumnCount(len(self.registros[0]))
           
            for row_idx, registro in enumerate(self.registros):
                for col_idx, valor in enumerate(registro):
                    item = QTableWidgetItem(str(valor))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.ui.tableWidget.setItem(row_idx, col_idx, item)

    def registrar(self):
        # Verifica se já existe a chave do banco de dados
        self.dia = self.ui.data.date().currentDate().toString("yyyy/MM/dd")
        self.registro = self.db.ler_tabela_data(self.dia)

        if not self.registro:
            self.lista[0] = self.ui.data.date().currentDate().toString("yyyy/MM/dd")
            self.lista[1] = self.ui.entrada.time().currentTime().toString("HH:mm")
            self.db.atualizar_tabela(1, self.lista)
        else:
            self.lista = list(self.registro)
            if self.lista[1] == "00:00":
                self.lista[1] = self.ui.entrada.time().currentTime().toString("HH:mm")
                self.campo = 2
            elif self.lista[2] == "00:00":
                self.lista[2] = self.ui.almoco.time().currentTime().toString("HH:mm")
                self.campo = 3
            elif self.lista[3] == "00:00":
                self.lista[3] = self.ui.retorno.time().currentTime().toString("HH:mm")
                self.lista[5] = self.ca.calcular_duracao(self.lista[1], self.lista[2])
                self.campo = 4
            elif self.lista[4] == "00:00":
                self.lista[4] = self.ui.saida.time().currentTime().toString("HH:mm")
                self.lista[6] = self.ca.calcular_duracao(self.lista[3], self.lista[4])
                self.lista[7] = self.ca.somar_tempos(self.lista[5], self.lista[6])
                self.campo = 5
            else:
                return

        self.db.atualizar_tabela(self.campo, self.lista)
        self.popular_tabela()
    
    def inserir(self):
        self.dia = datetime.strptime(self.ui.data.text(), '%d/%m/%Y').strftime('%Y/%m/%d')
        self.registro = self.db.ler_tabela_data(self.dia)

        if not self.registro:
            self.lista[0] = self.dia
            self.lista[1] = self.ui.entrada.text()
            self.lista[2] = self.ui.almoco.text()
            self.lista[3] = self.ui.retorno.text()
            self.lista[4] = self.ui.saida.text()
            if self.lista[1] and self.lista [2] != "00:00":
                self.lista[5] = self.ca.calcular_duracao(self.lista[1], self.lista[2])
            if self.lista[3] and self.lista [4] != "00:00":
                self.lista[6] = self.ca.calcular_duracao(self.lista[3], self.lista[4])
            if self.lista[1] and self.lista [2] and self.lista[3] and self.lista [4] != "00:00":                
                self.lista[7] = self.ca.somar_tempos(self.lista[5], self.lista[6])
            self.db.atualizar_tabela(1, self.lista)
            self.popular_tabela()
        else:
            QMessageBox(
                QMessageBox.Icon.Information,
                "Atenção",
                "Já existe um registro para a data.",
                QMessageBox.StandardButton.Ok,
                self,
                flags=Qt.WindowType.WindowStaysOnTopHint
            ).exec()

    def excluir(self):
        self.selecao = self.ui.tableWidget.selectedItems()
        self.total_linhas = {item.row() for item in self.selecao}
        print(self.total_linhas)
        
        if len(self.total_linhas) != 1:
            QMessageBox(
                QMessageBox.Icon.Information,
                "Atenção",
                "Selecione um registro para excluir.",
                QMessageBox.StandardButton.Ok,
                self,
                flags=Qt.WindowType.WindowStaysOnTopHint
            ).exec()
            self.ui.tableWidget.clearSelection()
        else:
            self.chave = self.selecao[0].text()
            res = QMessageBox(
                    QMessageBox.Icon.Warning,
                    "Atenção",
                    f"Confirma a exclusão do registro de {self.chave}?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    self,
                    flags=Qt.WindowType.WindowStaysOnTopHint
                ).exec()            
            if res == QMessageBox.StandardButton.Yes:
                self.db.excluir_registro(self.chave)
                self.popular_tabela()

    def exportar(self):
        # Função auxiliar para pegar o texto da célula com segurança
        def getCellText(row, col):
            item = self.ui.tableWidget.item(row, col)
            return item.text() if item is not None else ""

        # Verifica se há itens selecionados
        itens_selecionados = self.ui.tableWidget.selectedItems()
        if not itens_selecionados:
            QMessageBox.information(self, "Atenção", "Selecione pelo menos um registro.")
            return

        # Identifica as linhas únicas selecionadas
        linhas_selecionadas = {item.row() for item in itens_selecionados}

        # Nome do arquivo: pontos_yyyymm.csv (ano e mês corrente)
        nome_arquivo = f"pontos_{datetime.now().strftime('%Y%m')}.csv"
        caminho_arquivo = os.path.join(base_path, nome_arquivo)

        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            for linha in sorted(linhas_selecionadas):
                # Usa a função auxiliar para recuperar o valor de cada coluna
                data_str = getCellText(linha, 0)   # formato: yyyy/MM/dd
                entrada  = getCellText(linha, 1)
                almoco   = getCellText(linha, 2)
                retorno  = getCellText(linha, 3)
                saida    = getCellText(linha, 4)
                manha    = getCellText(linha, 5)   # Duração manhã
                tarde    = getCellText(linha, 6)   # Duração tarde

                # Verifica se a data está preenchida antes de converter
                if data_str:
                    try:
                        dt = datetime.strptime(data_str, "%Y/%m/%d")
                        data_formatada = dt.strftime("%d/%b/%y")  # Ex.: 20/Mar/25
                    except Exception as e:
                        data_formatada = data_str
                else:
                    data_formatada = ""

                # Monta as duas linhas conforme o padrão informado:
                linha_tarde = (
                    f"{data_formatada}#|#APROVADO#|#{retorno}#|#{saida}#|#{tarde}"
                    "#|#00:00#|#0000#|#0000-0000#|#SIM#|#0000#|#ANALISE DE SISTEMAS#|#"
                )
                linha_manha = (
                    f"{data_formatada}#|#APROVADO#|#{entrada}#|#{almoco}#|#{manha}"
                    "#|#00:00#|#0000#|#0000-0000#|#SIM#|#0000#|#ANALISE DE SISTEMAS#|#"
                )

                # Escreve cada período em uma linha do arquivo
                f.write(linha_tarde + "\n")
                f.write(linha_manha + "\n")

        QMessageBox.information(self, "Exportação Concluída", f"Arquivo exportado com sucesso:\n{caminho_arquivo}")
        self.ui.tableWidget.clearSelection()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.aboutToQuit.connect(window.db.fechar_banco)
    window.show()
    sys.exit(app.exec())
