import re
import tkinter as tk
from tkinter import scrolledtext, ttk

class appCalcGUI:
    def __init__(self, root):
        self.root = root
        root.title("Calculadora de Área COBOL")
        root.resizable(False, False)
        self.criarWidgets()

    def criarWidgets(self):
        self.criarAreaTexto()
        self.criarBotoes()
        self.criarLabelResultado()
        self.criarArvoreCampos()

    def criarAreaTexto(self):
        self.area_texto = scrolledtext.ScrolledText(
            self.root, width=80, height=15, wrap=tk.WORD)
        self.area_texto.grid(row=0, column=0, columnspan=2,
                             padx=10, pady=10, sticky="nsew")

    def criarBotoes(self):
        frame_botoes = tk.Frame(self.root)
        frame_botoes.grid(row=1, column=0, columnspan=2, pady=5)
        self.botao_calcular = tk.Button(
            frame_botoes, text="Calcular Área", command=self.calcularArea)
        self.botao_calcular.grid(row=0, column=0, padx=5)
        self.botao_limpar = tk.Button(
            frame_botoes, text="Limpar", command=self.limparAreaTexto)
        self.botao_limpar.grid(row=0, column=1, padx=5)

    def criarLabelResultado(self):
        self.label_resultado = tk.Label(
            self.root, text="", font=("Helvetica", 12))
        self.label_resultado.grid(row=2, column=0, columnspan=2, pady=5)

    def criarArvoreCampos(self):
        self.frame_arvore = ttk.Frame(self.root)
        self.frame_arvore.grid(row=3, column=0, columnspan=2,
                               padx=10, pady=5, sticky="nsew")
        self.arvore = ttk.Treeview(self.frame_arvore, columns=(
            'Nome', 'Tipo', 'Tamanho', 'Ocorrências'), show='headings')
        self.arvore.heading('Nome', text='Nome do Campo')
        self.arvore.heading('Tipo', text='Tipo')
        self.arvore.heading('Tamanho', text='Tamanho')
        self.arvore.heading('Ocorrências', text='Ocorrências')
        self.barra_rolagem = ttk.Scrollbar(
            self.frame_arvore, orient="vertical", command=self.arvore.yview)
        self.arvore.configure(yscrollcommand=self.barra_rolagem.set)
        self.arvore.grid(row=0, column=0, sticky="nsew")
        self.barra_rolagem.grid(row=0, column=1, sticky="ns")
        self.frame_arvore.grid_rowconfigure(0, weight=1)
        self.frame_arvore.grid_columnconfigure(0, weight=1)

    def calcularArea(self):
        area_cobol = self.area_texto.get(1.0, tk.END)
        area_total, campos = Calculo.calcularAreaTotal(area_cobol)
        self.label_resultado.config(text=f"Área total do layout: {area_total}")
        self.exibirCampos(campos)

    def limparAreaTexto(self):
        self.area_texto.delete(1.0, tk.END)
        self.arvore.delete(*self.arvore.get_children())

    def exibirCampos(self, campos):
        self.arvore.delete(*self.arvore.get_children())
        for campo in campos:
            self.arvore.insert('', 'end', values=campo)


class Calculo:
    @staticmethod
    def calcularAreaTotal(area_cobol):
        total_area = 0
        campos = []
        linhas = area_cobol.split('\n')
        redefined_fields = set()
        in_redefines_block = False
        redefines_indentation = 0

        for linha in linhas:
            match_redefines = re.match(
                r'\s*(\d+)\s+(\S+)\s+REDEFINES\s+(\S+)\.', linha)
            if match_redefines:
                redefined_fields.add(match_redefines.group(3))
                in_redefines_block = True
                redefines_indentation = len(re.match(r'(\s*)', linha).group(1))
                continue

            if in_redefines_block:
                line_indentation = len(re.match(r'(\s*)', linha).group(1))
                if line_indentation <= redefines_indentation:
                    in_redefines_block = False
                else:
                    continue

            # Expressão regular dividida para melhor legibilidade
            expressao = (
                r'\s*(\d+)\s+(\S+)\s+PIC\s+([9X])'
                r'(?:\((\d+)\))?'
                r'(?:\s+(?:OCCURS|OC)\s+(\d+))?'
                r'(?:\s+DEPENDING\s+ON\s+(\S+))?'
                r'(?:\s+(BINARY|COMP(?:-2|-3|-4|-5)?))?'
            )

            match_field = re.match(expressao, linha)
            if match_field:
                name = match_field.group(2)
                field_type = match_field.group(3)
                size = int(match_field.group(4)) if match_field.group(4) else 1
                occurs = int(match_field.group(
                    5)) if match_field.group(5) else 1

                if match_field.group(7):
                    comp_type = match_field.group(7)
                    if comp_type == 'COMP':
                        size = (size + 1) // 2
                    elif comp_type == 'COMP-2':
                        size = size // 2
                    elif comp_type in ['COMP-3', 'COMP-4', 'COMP-5']:
                        size = (size // 2) + 1

                if name in redefined_fields:
                    continue

                total_area += size * occurs
                campos.append((name, field_type, size, occurs))

        return total_area, campos


def main():
    root = tk.Tk()
    appCalcGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
