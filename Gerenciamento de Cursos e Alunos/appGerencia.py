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

    sv_ttk.toggle_theme()
    #Experimental
    self.style = sv_ttk.Style(self.root)
    self.style.configure("My.TFrame", background='#0059b3')

    frame_logo = sv_ttk.Frame(self.root, width=850, height=52, style="My.TFrame")
    frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky="nsew")


    


def main():
  root = tk.Tk()
  appGerenciaGUI(root)
  sv_ttk.use_light_theme()
  root.mainloop()

if __name__ == "__main__":
  main()