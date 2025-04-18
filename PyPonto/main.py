import os
import platform
import subprocess
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
        self.lista = ["00/00/0000", "00:00", "00:00", "00:00", "00:00", "00:00", "00:00", "00:00"]

        # UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Atribuir data do dia para a caixa de texto DATA
        self.ui.data.setDate(QDate.currentDate())

        # Atribuir funções aos botões
        atribuir_botoes()

        # Banco de dados
        self.db.criar_tabela()
        self.popular_tabela()

    def popular_tabela(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

        registros = []
        registros = self.db.ler_tabela()

        if registros:
            self.ui.tableWidget.setRowCount(len(registros))
            self.ui.tableWidget.setColumnCount(len(registros[0]))

            for row_idx, registro in enumerate(registros):
                for col_idx, valor in enumerate(registro):
                    item = QTableWidgetItem(str(valor))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.ui.tableWidget.setItem(row_idx, col_idx, item)

    def registrar(self):
        # Verifica se já existe a chave do banco de dados
        dia = self.ui.data.date().currentDate().toString("yyyy/MM/dd")
        registro = self.db.ler_tabela_data(dia)

        self.campo = None
        if not registro:
            self.lista[0] = self.ui.data.date().currentDate().toString("yyyy/MM/dd")
            self.lista[1] = self.ui.entrada.time().currentTime().toString("HH:mm")
            self.campo = 1
            self.db.atualizar_tabela(self.campo, self.lista)
            self.popular_tabela()
            return
        else:
            self.lista = list(registro)
            if self.lista[1] == "00:00":
                self.lista[1] = self.ui.entrada.time().currentTime().toString("HH:mm")
                self.campo = 2
            elif self.lista[2] == "00:00":
                self.lista[2] = self.ui.almoco.time().currentTime().toString("HH:mm")
                res = datetime.strptime(self.ca.calcular_duracao(self.lista[1], self.lista[2]), "%H:%M")
                self.lista[5] = res.strftime("%H:%M")
                self.campo = 3
            elif self.lista[3] == "00:00":
                self.lista[3] = self.ui.retorno.time().currentTime().toString("HH:mm")
                self.campo = 4
            elif self.lista[4] == "00:00":
                self.lista[4] = self.ui.saida.time().currentTime().toString("HH:mm")
                res = datetime.strptime(self.ca.calcular_duracao(self.lista[3], self.lista[4]), "%H:%M")
                self.lista[6] = res.strftime("%H:%M")
                res = self.ca.somar_tempos(self.lista[5], self.lista[6])
                res_conv = datetime.strptime(res, "%H:%M")
                self.lista[7] = res_conv.strftime("%H:%M")
                self.campo = 5
            else:
                return

        self.db.atualizar_tabela(self.campo, self.lista)
        self.popular_tabela()

    def inserir(self):
        self.dia = datetime.strptime(self.ui.data.text(), '%d/%m/%Y').strftime('%Y/%m/%d')
        registro = self.db.ler_tabela_data(self.dia)

        if not registro:
            self.lista[0] = self.dia
            self.lista[1] = self.ui.entrada.text()
            self.lista[2] = self.ui.almoco.text()
            self.lista[3] = self.ui.retorno.text()
            self.lista[4] = self.ui.saida.text()
            if self.lista[1] and self.lista[2] != "00:00":
                res = datetime.strptime(self.ca.calcular_duracao(self.lista[1], self.lista[2]), "%H:%M")
                self.lista[5] = res.strftime("%H:%M")
            if self.lista[3] and self.lista[4] != "00:00":
                res = datetime.strptime(self.ca.calcular_duracao(self.lista[3], self.lista[4]), "%H:%M")
                self.lista[6] = res.strftime("%H:%M")
            if self.lista[1] and self.lista[2] and self.lista[3] and self.lista[4] != "00:00":
                res = self.ca.somar_tempos(self.lista[5], self.lista[6])
                res_conv = datetime.strptime(res, "%H:%M")
                self.lista[7] = res_conv.strftime("%H:%M")
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
        selecao = self.ui.tableWidget.selectedItems()
        total_linhas = {item.row() for item in selecao}

        if len(total_linhas) != 1:
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
            chave = selecao[0].text()
            res = QMessageBox(
                QMessageBox.Icon.Warning,
                "Atenção",
                f"Confirma a exclusão do registro de {chave}?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                self,
                flags=Qt.WindowType.WindowStaysOnTopHint).exec()
            if res == QMessageBox.StandardButton.Yes:
                self.db.excluir_registro(chave)
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
                data_str = getCellText(linha, 0)  # data
                entrada = getCellText(linha, 1)  # entrada
                almoco = getCellText(linha, 2)  # almoço
                retorno = getCellText(linha, 3)  # retorno
                saida = getCellText(linha, 4)  # saide
                manha = getCellText(linha, 5)  # manhã
                tarde = getCellText(linha, 6)  # tarde

                # Verifica se a data está preenchida antes de converter
                if data_str:
                    try:
                        dt = datetime.strptime(data_str, "%Y/%m/%d")
                        data_str = dt.strftime("%d/%b/%y")
                        dia, mes, ano = data_str.split('/')
                        mes = mes.capitalize()
                        data_formatada = f"{dia}/{mes}/{ano}"
                    except Exception:
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


def dark_mode():
    try:
        resultado = subprocess.run(
            ["gsettings", "get", "org.gnome.desktop.interface", "color-scheme"],
            capture_output=True, text=True
        )
        return "prefer-dark" in resultado.stdout
    except Exception:
        return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Verifica qual modo de cor o Gnome está
    if platform.system() == "Linux" and dark_mode():
        try:
            import qdarkstyle
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6())
        except ImportError:
            print("Instale o qdarkstyle: pip install qdarkstyle")
    else:
        app.setStyle("Fusion")
    window = MainWindow()
    app.aboutToQuit.connect(window.db.fechar_banco)
    window.show()
    sys.exit(app.exec())
