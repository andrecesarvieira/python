import tkinter as tk
from tkinter import scrolledtext, ttk
from backend.mainBackEnd import calcularAreaTotal

class CalculadoraLayoutCOBOL:
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
        self.area_texto = scrolledtext.ScrolledText(self.root, width=80, height=15, wrap=tk.WORD)
        self.area_texto.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    def criarBotoes(self):
        frame_botoes = tk.Frame(self.root)
        frame_botoes.grid(row=1, column=0, columnspan=2, pady=5)
        self.botao_calcular = tk.Button(frame_botoes, text="Calcular Área", command=self.calcularArea)
        self.botao_calcular.grid(row=0, column=0, padx=5)
        self.botao_limpar = tk.Button(frame_botoes, text="Limpar", command=self.limparAreaTexto)
        self.botao_limpar.grid(row=0, column=1, padx=5)

    def criarLabelResultado(self):
        self.label_resultado = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.label_resultado.grid(row=2, column=0, columnspan=2, pady=5)

    def criarArvoreCampos(self):
        self.frame_arvore = ttk.Frame(self.root)
        self.frame_arvore.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        self.arvore = ttk.Treeview(self.frame_arvore, columns=('Nome', 'Tipo', 'Tamanho', 'Ocorrências'), show='headings')
        self.arvore.heading('Nome', text='Nome do Campo')
        self.arvore.heading('Tipo', text='Tipo')
        self.arvore.heading('Tamanho', text='Tamanho')
        self.arvore.heading('Ocorrências', text='Ocorrências')
        self.barra_rolagem = ttk.Scrollbar(self.frame_arvore, orient="vertical", command=self.arvore.yview)
        self.arvore.configure(yscrollcommand=self.barra_rolagem.set)
        self.arvore.grid(row=0, column=0, sticky="nsew")
        self.barra_rolagem.grid(row=0, column=1, sticky="ns")
        self.frame_arvore.grid_rowconfigure(0, weight=1)
        self.frame_arvore.grid_columnconfigure(0, weight=1)

    def calcularArea(self):
        area_cobol = self.area_texto.get(1.0, tk.END)
        area_total, campos = calcularAreaTotal(area_cobol)
        self.label_resultado.config(text=f"Área total do layout: {area_total}")
        self.exibirCampos(campos)

    def limparAreaTexto(self):
        self.area_texto.delete(1.0, tk.END)
        self.arvore.delete(*self.arvore.get_children())

    def exibirCampos(self, campos):
        self.arvore.delete(*self.arvore.get_children())
        for campo in campos:
            self.arvore.insert('', 'end', values=campo)
