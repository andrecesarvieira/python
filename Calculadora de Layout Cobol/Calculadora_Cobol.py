import tkinter as tk  # Importa a biblioteca tkinter para criar interfaces gráficas
from tkinter import scrolledtext, ttk  # Importa widgets específicos do tkinter
import re  # Importa o módulo re para trabalhar com expressões regulares

class CalculadoraLayoutCOBOL:
    def __init__(self, root):
        self.root = root  # Define o objeto root como a janela principal da interface
        root.title("Calculadora de Área COBOL")  # Define o título da janela
        root.resizable(False, False)  # Impede que a janela seja redimensionada

        self.criar_widgets()  # Chama o método para criar os widgets da interface

    def criar_widgets(self):
        self.criar_area_texto()  # Chama o método para criar a área de texto
        self.criar_botoes()  # Chama o método para criar os botões
        self.criar_label_resultado()  # Chama o método para criar o rótulo de resultado
        self.criar_arvore_campos()  # Chama o método para criar a árvore de campos

    def criar_area_texto(self):
        # Cria uma área de texto com barra de rolagem
        self.area_texto = scrolledtext.ScrolledText(self.root, width=80, height=15, wrap=tk.WORD)
        # Define a posição e o tamanho da área de texto na janela
        self.area_texto.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    def criar_botoes(self):
        # Cria um frame para conter os botões
        frame_botoes = tk.Frame(self.root)
        frame_botoes.grid(row=1, column=0, columnspan=2, pady=5)  # Define a posição do frame na janela
        # Cria um botão para calcular a área
        self.botao_calcular = tk.Button(frame_botoes, text="Calcular Área", command=self.calcular_area)
        self.botao_calcular.grid(row=0, column=0, padx=5)  # Define a posição do botão no frame
        # Cria um botão para limpar a área de texto
        self.botao_limpar = tk.Button(frame_botoes, text="Limpar", command=self.limpar_area_texto)
        self.botao_limpar.grid(row=0, column=1, padx=5)  # Define a posição do botão no frame

    def criar_label_resultado(self):
        # Cria um rótulo para exibir o resultado do cálculo
        self.label_resultado = tk.Label(self.root, text="", font=("Helvetica", 12))
        # Define a posição do rótulo na janela
        self.label_resultado.grid(row=2, column=0, columnspan=2, pady=5)

    def criar_arvore_campos(self):
        # Cria um frame para conter a árvore de campos
        self.frame_arvore = ttk.Frame(self.root)
        self.frame_arvore.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        # Cria a árvore de campos com colunas específicas
        self.arvore = ttk.Treeview(self.frame_arvore, columns=('Nome', 'Tipo', 'Tamanho', 'Ocorrências'), show='headings')
        # Define os cabeçalhos das colunas
        self.arvore.heading('Nome', text='Nome do Campo')
        self.arvore.heading('Tipo', text='Tipo')
        self.arvore.heading('Tamanho', text='Tamanho')
        self.arvore.heading('Ocorrências', text='Ocorrências')
        # Cria uma barra de rolagem vertical para a árvore de campos
        self.barra_rolagem = ttk.Scrollbar(self.frame_arvore, orient="vertical", command=self.arvore.yview)
        self.arvore.configure(yscrollcommand=self.barra_rolagem.set)
        # Define a posição da árvore de campos e da barra de rolagem no frame
        self.arvore.grid(row=0, column=0, sticky="nsew")
        self.barra_rolagem.grid(row=0, column=1, sticky="ns")
        # Configura a expansão automática do frame
        self.frame_arvore.grid_rowconfigure(0, weight=1)
        self.frame_arvore.grid_columnconfigure(0, weight=1)

    def calcular_area(self):
        # Obtém o código COBOL da área de texto
        codigo_cobol = self.area_texto.get(1.0, tk.END)
        # Calcula a área total e os campos a partir do código COBOL
        area_total, campos = self.calcular_area_total(codigo_cobol)
        # Atualiza o rótulo de resultado com a área total calculada
        self.label_resultado.config(text=f"Área total do layout: {area_total}")
        # Exibe os campos na árvore de campos
        self.exibir_campos(campos)

    def limpar_area_texto(self):
        # Limpa o conteúdo da área de texto
        self.area_texto.delete(1.0, tk.END)

    def calcular_area_total(self, codigo_cobol):
        total_area = 0  # Inicializa a área total como zero
        campos = []  # Lista para armazenar os campos encontrados no código COBOL
        linhas = codigo_cobol.split('\n')  # Divide o código COBOL em linhas

        redefined_fields = set()  # Conjunto para armazenar os nomes dos campos redefinidos
        in_redefines_block = False  # Flag para indicar se está dentro de um bloco de redefinições
        redefines_indentation = 0  # Variável para armazenar a indentação do bloco de redefinições

        # Itera sobre as linhas do código COBOL
        for line in linhas:
            # Verifica se a linha corresponde a uma redefinição de campo
            match_redefines = re.match(r'\s*(\d+)\s+(\S+)\s+REDEFINES\s+(\S+)\.', line)
            if match_redefines:
                # Obtém o nome do campo redefinido
                redefined_name = match_redefines.group(3)
                # Adiciona o nome do campo redefinido ao conjunto de campos redefinidos
                redefined_fields.add(redefined_name)
                # Indica que está dentro de um bloco de redefinições
                in_redefines_block = True
                # Obtém a indentação do bloco de redefinições
                redefines_indentation = len(re.match(r'(\s*)', line).group(1))
                continue  # Pula para a próxima iteração

            # Verifica se está dentro de um bloco de redefinições
            if in_redefines_block:
                # Obtém a indentação da linha atual
                line_indentation = len(re.match(r'(\s*)', line).group(1))
                # Verifica se a indentação da linha é menor ou igual à indentação do bloco de redefinições
                if line_indentation <= redefines_indentation:
                    # Indica que saiu do bloco de redefinições
                    in_redefines_block = False
                else:
                    continue  # Pula para a próxima iteração

            # Verifica se a linha corresponde a um campo
            match_field = re.match(r'\s*(\d+)\s+(\S+)\s+PIC\s+([9X])(?:\((\d+)\))?(?:\s+(?:OCCURS|OC)\s+(\d+))?(?:\s+DEPENDING\s+ON\s+(\S+))?(?:\s+(BINARY|COMP(?:-2|-3|-4|-5)?))?', line)
            if match_field:
                # Obtém o nome do campo
                name = match_field.group(2)
                # Obtém o tipo do campo
                field_type = match_field.group(3)
                # Obtém o tamanho do campo
                size = int(match_field.group(4)) if match_field.group(4) else 1
                # Obtém o número de ocorrências do campo
                occurs = int(match_field.group(5)) if match_field.group(5) else 1
                
                # Verifica se o campo é de tipo comp
                if match_field.group(7):
                    comp_type = match_field.group(7)
                    # Ajusta o tamanho do campo dependendo do tipo comp
                    if comp_type == 'COMP':
                        size = (size + 1) // 2  
                    elif comp_type == 'COMP-2':
                        size = size // 2  
                    elif comp_type in ['COMP-3', 'COMP-4', 'COMP-5']:
                        size = (size // 2) + 1  
                
                # Verifica se o campo está redefinido
                if name in redefined_fields:
                    continue  # Pula para a próxima iteração
                
                # Calcula a área total considerando o tamanho e o número de ocorrências do campo
                total_area += size * occurs
                # Adiciona o campo à lista de campos
                campos.append((name, field_type, size, occurs))
        
        # Retorna a área total calculada e a lista de campos
        return total_area, campos

    def exibir_campos(self, campos):
        # Limpa os campos existentes na árvore de campos
        self.arvore.delete(*self.arvore.get_children())
        # Insere cada campo na árvore de campos
        for campo in campos:
            self.arvore.insert('', 'end', values=campo)

def main():
    # Cria a janela principal
    root = tk.Tk()
    # Cria a aplicação da calculadora de layout COBOL
    app = CalculadoraLayoutCOBOL(root)
    # Inicia o loop de eventos da interface gráfica
    root.mainloop()

if __name__ == "__main__":
    main()
