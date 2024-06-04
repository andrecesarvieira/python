import tkinter as tk
from tkinter import ttk
import sv_ttk

class appGerenciaGUI:
  def __init__(self, root):
    self.root = root
    self.root.title("Gerenciamento de Cursos e Alunos")
    self.root.resizable(False, False)
    
    # Centralizando a janela conforme resolução do monitor
    largura = 1280
    altura = 720
    tela_largura = self.root.winfo_screenwidth()
    tela_altura = self.root.winfo_screenheight() - 80
    x_coordenada = int((tela_largura / 2) - (largura / 2))
    y_coordenada = int((tela_altura / 2) - (altura / 2))
    self.root.geometry(f"{largura}x{altura}+{x_coordenada}+{y_coordenada}")
    
    frame_logo = ttk.Frame(self.rootroot, height=52)
    frame_logo.grid(row==0, column=0)


    #Experimental
    style = ttk.Style(self.root)
    style.theme_use("xpnative")
    


def main():
  root = tk.Tk()
  appGerenciaGUI(root)
  sv_ttk.use_dark_theme()
  root.mainloop()

if __name__ == "__main__":
  main()