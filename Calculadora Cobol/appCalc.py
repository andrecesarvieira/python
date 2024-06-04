import re
import tkinter as tk
from tkinter import scrolledtext, ttk
import sv_ttk

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
        frame_botoes = ttk.Frame(self.root)
        frame_botoes.grid(row=1, column=0, columnspan=2, pady=5)
        self.botao_calcular = ttk.Button(
            frame_botoes, text="Calcular Área", command=self.calcularArea)
        self.botao_calcular.grid(row=0, column=0, padx=5)
        self.botao_limpar = ttk.Button(
            frame_botoes, text="Limpar", command=self.limparAreaTexto)
        self.botao_limpar.grid(row=0, column=1, padx=5)
        self.botao_tema = ttk.Button(
            frame_botoes, text="Tema", command=self.mudarTema)
        self.botao_tema.grid(row=0, column=2, padx=5)

    def criarLabelResultado(self):
        self.label_resultado = ttk.Label(
            self.root, text="", font=("Helvetica", 10, "bold"))
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

    def mudarTema(self):
        if sv_ttk.get_theme() == "dark":
            sv_ttk.use_light_theme()
        else:
            sv_ttk.use_dark_theme()

class Calculo:
    @staticmethod
    def calcularAreaTotal(area_cobol):
        total_area = 0
        campos = []
        linhas = area_cobol.split('\n')
        redefinidos = set()
        redefinindo = False
        nivel_redefine = 0
        fatores_ocorrencia = [1] * 50  # Lista inicializada para 50 níveis de hierarquia

        for linha in linhas:
            match_redefine = re.match(
                r'\s*(\d+)\s+(\S+)\s+REDEFINES\s+(\S+)\.', linha)
            if match_redefine:
                redefinidos.add(match_redefine.group(3))
                redefinindo = True
                nivel_redefine = int(match_redefine.group(1))
                continue

            if redefinindo:
                nivel_linha = int(re.match(r'(\s*)', linha).group(1))
                if nivel_linha <= nivel_redefine:
                    redefinindo = False
                else:
                    continue

            expressao = (
                r'\s*(\d+)\s+(\S+)\s+PIC\s+([9XZS])'
                r'(?:\((\d+)\))?'
                r'(?:V9\((\d+)\))?'  # Captura campos com ponto decimal
                r'(?:\s+OCCURS\s+(\d+))?' # Captura ocorrências
                r'(?:\s+OC\s+(\d+))?' # Captura ocorrências abrev.
                r'(?:\s+(BINARY|COMP(?:-1|-2|-3|-4|-5)?))?'
            )
            
            match_campo = re.match(expressao, linha)
            if match_campo:
                nivel = int(match_campo.group(1))
                nome = match_campo.group(2)
                tipo = match_campo.group(3)
                tamanho = int(match_campo.group(4)) if match_campo.group(4) else 1
                decimal_size = int(match_campo.group(5)) if match_campo.group(5) else 0
                ocorrencias = int(match_campo.group(6)) if match_campo.group(6) else 1

                if tipo in ['9', 'S']:
                    tamanho += decimal_size

                fatores_ocorrencia[nivel] = ocorrencias

                if nome in redefinidos:
                    continue

                multiplicador = 1
                for i in range(1, nivel + 1):
                    multiplicador *= fatores_ocorrencia[i]

                total_area += tamanho * multiplicador
                campos.append((nome, tipo, tamanho, multiplicador))

        return total_area, campos

def main():
    root = tk.Tk()
    appCalcGUI(root)
    sv_ttk.use_light_theme()
    root.mainloop()

if __name__ == "__main__":
    main()
