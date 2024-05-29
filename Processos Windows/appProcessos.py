import win32service
import win32serviceutil
import win32api
import subprocess
import tkinter as tk
from tkinter import messagebox, ttk
import ctypes
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    if not is_admin():
        try:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        except Exception as e:
            print(f"Erro ao tentar elevar o script: {e}")
        sys.exit(0)


def obter_configuracao(servico_nome):
    try:
        config_servico = win32service.QueryServiceConfig(win32service.OpenService(
            win32service.OpenSCManager(
                None, None, win32service.SC_MANAGER_ALL_ACCESS),
            servico_nome,
            win32service.SERVICE_QUERY_CONFIG
        ))
        tipo_inicio = config_servico[1]
        return tipo_inicio
    except Exception as e:
        # Apenas informativo
        print(f"Erro ao obter configuração do serviço {servico_nome}: {e}")
        return None


def obter_descricao(servico_nome):
    try:
        descricao_servico = win32service.QueryServiceConfig2(win32service.OpenService(
            win32service.OpenSCManager(
                None, None, win32service.SC_MANAGER_ALL_ACCESS),
            servico_nome,
            win32service.SERVICE_CONFIG_DESCRIPTION
        ), win32service.SERVICE_CONFIG_DESCRIPTION)
        descricao = descricao_servico
        return descricao if descricao else "Descrição não disponível"
    except win32api.error as e:
        if e.winerror == 15100:
            return "Descrição não disponível"
        # Apenas informativo
        print(f"Erro ao obter descrição do serviço {servico_nome}: {e}")
        return "Descrição não disponível"
    except Exception as e:
        # Apenas informativo
        print(f"Erro ao obter descrição do serviço {servico_nome}: {e}")
        return "Descrição não disponível"


def obter_status(servico_nome):
    status_servico = win32serviceutil.QueryServiceStatus(servico_nome)[1]
    status = {
        win32service.SERVICE_STOPPED: "Parado",
        win32service.SERVICE_START_PENDING: "Iniciando",
        win32service.SERVICE_STOP_PENDING: "Parando",
        win32service.SERVICE_RUNNING: "Executando",
        win32service.SERVICE_CONTINUE_PENDING: "Continuando",
        win32service.SERVICE_PAUSE_PENDING: "Pausando",
        win32service.SERVICE_PAUSED: "Pausado"
    }.get(status_servico, "Desconhecido")
    return status


def listar_servicos():
    try:
        servicos = win32service.EnumServicesStatus(
            win32service.OpenSCManager(None, None, win32service.SC_MANAGER_ALL_ACCESS))
    except win32api.error as e:
        if e.winerror == 5:
            messagebox.showerror(
                "Erro", "Acesso negado. Por favor, execute o script como administrador.")
        else:
            messagebox.showerror("Erro", e.strerror)
        return []

    tabela_servicos = []

    for servico in servicos:
        nome_servico = servico[0]
        nome_exibicao = servico[1] if servico[1] is not None else "Desconhecido"
        descricao = obter_descricao(nome_servico)
        status = obter_status(nome_servico)
        tipo_inicio = obter_configuracao(nome_servico)

        tipos_inicio = {
            win32service.SERVICE_AUTO_START: "Automático",
            win32service.SERVICE_BOOT_START: "Inicialização",
            win32service.SERVICE_DEMAND_START: "Manual",
            win32service.SERVICE_DISABLED: "Desativado",
            win32service.SERVICE_SYSTEM_START: "Sistema"
        }

        tipo_inicio_str = tipos_inicio.get(tipo_inicio, "Desconhecido")

        tabela_servicos.append({
            "nome": nome_servico,
            "nome_exibicao": nome_exibicao,
            "descricao": descricao,
            "status": status,
            "tipo_inicio": tipo_inicio_str
        })

    return tabela_servicos


def desabilitar_servico(servico):
    nome_servico = servico.get("nome", "")
    status_servico = servico.get("status", "")
    try:
        if status_servico == "Executando":
            win32serviceutil.StopService(nome_servico)
        comando = ["sc", "config", nome_servico, "start=demand"]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        if resultado.returncode != 0:
            print(
                f"Erro ao desabilitar o serviço {nome_servico}: {resultado.stderr}")
    except Exception as e:
        # Apenas informativo
        print(f"Erro ao desabilitar o serviço {nome_servico}: {str(e)}")


def iniciar_servico(servico):
    nome_servico = servico.get("nome", "")
    try:
        win32serviceutil.StartService(nome_servico)
    except Exception as e:
        # Apenas informativo
        print(f"Erro ao iniciar o serviço {nome_servico}: {str(e)}")


def parar_servico(servico):
    nome_servico = servico.get("nome", "")
    try:
        win32serviceutil.StopService(nome_servico)
    except Exception as e:
        # Apenas informativo
        print(f"Erro ao parar o serviço {nome_servico}: {str(e)}")


def atualizar_lista(tree, filtro=""):
    for item in tree.get_children():
        tree.delete(item)
    servicos = listar_servicos()
    for servico in servicos:
        if (filtro.lower() in (servico['nome'] or "").lower() or
            filtro.lower() in (servico['nome_exibicao'] or "").lower() or
            filtro.lower() in (servico['descricao'] or "").lower() or
            filtro.lower() in (servico['status'] or "").lower() or
                filtro.lower() in (servico['tipo_inicio'] or "").lower()):
            tree.insert("", "end", values=(
                servico['nome'],
                servico['nome_exibicao'],
                servico['descricao'],
                servico['status'],
                servico['tipo_inicio']
            ))


def criar_gui():
    root = tk.Tk()
    root.title("Gerenciador de Serviços")
    root.geometry("1200x600")

    search_frame = tk.Frame(root)
    search_frame.pack(fill=tk.X)

    search_label = tk.Label(search_frame, text="Pesquisar:")
    search_label.pack(side=tk.LEFT, padx=5, pady=5)

    search_entry = tk.Entry(search_frame)
    search_entry.pack(fill=tk.X, padx=5, expand=True)

    # Adiciona o foco ao campo de entrada de pesquisa
    search_entry.focus_set()

    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    columns = ["Nome", "Nome de Exibição",
               "Descrição", "Status", "Tipo de Início"]
    tree = ttk.Treeview(frame, columns=columns, show="headings")
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Definindo as larguras das colunas
    tree.column("Nome", width=150)
    tree.column("Nome de Exibição", width=200)
    tree.column("Descrição", width=400)
    tree.column("Status", width=100)
    tree.column("Tipo de Início", width=100)

    for col in columns:
        tree.heading(
            col, text=col, command=lambda _col=col: sort_by(tree, _col, False))
        tree.column(col, stretch=True)

    scrollbar_v = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_v.set)
    scrollbar_v.pack(side=tk.RIGHT, fill=tk.Y)

    atualizar_lista(tree)

    selected_servico = {}

    btn_frame = tk.Frame(root)
    btn_frame.pack(fill=tk.X, pady=10)

    btn_iniciar = tk.Button(btn_frame, text="Iniciar Serviço", state=tk.DISABLED, command=lambda: [
                            iniciar_servico(selected_servico), atualizar_lista(tree, search_entry.get())])
    btn_iniciar.pack(side=tk.LEFT, padx=5)

    btn_parar = tk.Button(btn_frame, text="Parar Serviço", state=tk.DISABLED, command=lambda: [
                          parar_servico(selected_servico), atualizar_lista(tree, search_entry.get())])
    btn_parar.pack(side=tk.LEFT, padx=5)

    btn_desabilitar = tk.Button(btn_frame, text="Desabilitar Serviço", state=tk.DISABLED, command=lambda: [
                                desabilitar_servico(selected_servico), atualizar_lista(tree, search_entry.get())])
    btn_desabilitar.pack(side=tk.LEFT, padx=5)

    def on_select(event):
        selected = tree.selection()
        if selected:
            btn_iniciar.config(state=tk.NORMAL)
            btn_parar.config(state=tk.NORMAL)
            btn_desabilitar.config(state=tk.NORMAL)
            item = tree.item(selected[0])
            nonlocal selected_servico
            selected_servico = {
                "nome": item['values'][0],
                "nome_exibicao": item['values'][1],
                "descricao": item['values'][2],
                "status": item['values'][3],
                "tipo_inicio": item['values'][4]
            }
        else:
            btn_iniciar.config(state=tk.DISABLED)
            btn_parar.config(state=tk.DISABLED)
            btn_desabilitar.config(state=tk.DISABLED)

    tree.bind('<<TreeviewSelect>>', on_select)

    def sort_by(tree, col, descending):
        data = [(tree.set(child, col), child)
                for child in tree.get_children('')]
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            tree.move(item[1], '', indx)
        tree.heading(col, command=lambda: sort_by(tree, col, not descending))

    def on_key_release(event):
        atualizar_lista(tree, search_entry.get())

    search_entry.bind("<KeyRelease>", on_key_release)

    root.mainloop()


if __name__ == "__main__":
    run_as_admin()
    criar_gui()
