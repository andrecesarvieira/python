import tkinter as tk
from tkinter import filedialog, ttk, messagebox

class GeradorComandosDesinstalacaoWinget:
    def __init__(self, raiz):
        self.raiz = raiz
        raiz.title("Gerador de Script Desinstalador Winget")
        raiz.geometry("1280x720")

        # Botão para carregar arquivo
        self.botao_carregar = tk.Button(raiz, text="Carregar Arquivo TXT", command=self.carregar_arquivo)
        self.botao_carregar.pack(pady=10)

        # Frame para o Treeview e a Scrollbar
        self.tree_frame = tk.Frame(raiz)
        self.tree_frame.pack(expand=True, fill='both')

        # Configuração do Treeview
        self.tree = ttk.Treeview(self.tree_frame, columns=("Nome", "ID"), show="headings")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("ID", text="ID")
        self.tree.column("Nome", width=200)
        self.tree.column("ID", width=200)
        self.tree.pack(side=tk.LEFT, expand=True, fill='both')

        # Scrollbar para o Treeview
        self.scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Botão para excluir linha selecionada
        self.botao_excluir = tk.Button(raiz, text="Remover da Lista", command=self.excluir_selecionado)
        self.botao_excluir.pack(pady=10)

        # Botão para gerar script PowerShell
        self.botao_gerar_script = tk.Button(raiz, text="Gerar Script PowerShell", command=self.gerar_script_powershell)
        self.botao_gerar_script.pack(pady=10)

    def carregar_arquivo(self):
        caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt")])
        if caminho_arquivo:
            self.processar_arquivo(caminho_arquivo)

    def processar_arquivo(self, caminho_arquivo):
        # Limpa o Treeview antes de adicionar novos itens
        for i in self.tree.get_children():
            self.tree.delete(i)

        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        colunas = ["Nome", "ID", "Versão", "Disponível", "Origem"]
        posicoes_colunas = self.identificar_posicoes_colunas(linhas[0], colunas)

        for linha in linhas[2:]:
            inicio_nome, fim_nome = posicoes_colunas[0]
            inicio_id, fim_id = posicoes_colunas[1]
            nome = linha[inicio_nome:fim_nome].strip()
            valor_id = linha[inicio_id:fim_id].strip()
            self.tree.insert("", tk.END, values=(nome, valor_id))

    def identificar_posicoes_colunas(self, linha_cabecalho, colunas):
        posicoes = []
        for coluna in colunas:
            inicio = linha_cabecalho.find(coluna)
            fim = len(linha_cabecalho) if colunas.index(coluna) == len(colunas) - 1 else linha_cabecalho.find(colunas[colunas.index(coluna) + 1], inicio)
            posicoes.append((inicio, fim))
        return posicoes

    def excluir_selecionado(self):
        selecionados = self.tree.selection()
        if selecionados:
            for item_selecionado in selecionados:
                self.tree.delete(item_selecionado)
        else:
            messagebox.showwarning("Aviso", "Selecione pelo menos um item para excluir.")

    def gerar_script_powershell(self):
        local_arquivo = filedialog.asksaveasfilename(
            defaultextension=".ps1",
            filetypes=[("PowerShell Scripts", "*.ps1")],
            initialfile="ExcluirLista.ps1"  # Sugerir nome padrão para o arquivo
        )
        if not local_arquivo:
            return  # O usuário cancelou a operação de salvar o arquivo
        
        with open(local_arquivo, "w") as arquivo_ps:
            for item in self.tree.get_children():
                id = self.tree.item(item, 'values')[1]  # Obtém o ID
                comando = f"winget uninstall --id {id}\n"
                arquivo_ps.write(comando)
        
        # Mensagem informativa sobre como executar o script
        messagebox.showinfo("Script Gerado com Sucesso", "Abrir um terminal Power Shell como Administrador e executar o seguinte comando para liberar a execução de scripts: \"Set-ExecutionPolicy Unrestricted\".\nApós, executar o script gerado pelo prompt.")

if __name__ == "__main__":
    raiz = tk.Tk()
    app = GeradorComandosDesinstalacaoWinget(raiz)
    raiz.mainloop()
