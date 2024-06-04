import tkinter as tk
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk

class appGerenciaGUI:
  def __init__(self, root):
    self.root = root
    self.root.title("Gerenciamento de Cursos e Alunos")
    self.root.resizable(False, False)
    #self.root.tk.call('source', 'temas/forest-light.tcl')
    #ttk.Style().theme_use('forest-light')

    # Centralizando a janela conforme resolução do monitor
    largura = 1280
    altura = 720
    tela_largura = self.root.winfo_screenwidth()
    tela_altura = self.root.winfo_screenheight() - 80
    x_coordenada = int((tela_largura / 2) - (largura / 2))
    y_coordenada = int((tela_altura / 2) - (altura / 2))
    self.root.geometry(f"{largura}x{altura}+{x_coordenada}+{y_coordenada}")

    # Definindo style dos frames
    self.cor_fundo_logo = "#D3D3D3"
    self.cor_fonte_logo = "#0E2B4A"
    self.cor_fundo_padrao = "#091E35"

    self.fonte = font.Font(family='JetBrains Mono ExtraBold', name='logo', size=18, weight='normal')
    
    self.style = ttk.Style(self.root)
    self.style.configure("Logo.TFrame", background=self.cor_fundo_logo, font=self.fonte)
    self.style.configure("Padrao.TFrame", background=self.cor_fundo_padrao, font=self.fonte)
    
    # Criação dos frames
    self.frame_logo = ttk.Frame(self.root, width=1276, height=48, style="Logo.TFrame")
    self.frame_logo.grid(row=0, column=0, columnspan=2, pady=2, padx=2, sticky="nsew")
    self.frame_menu = ttk.Frame(self.root, width=1276, height=60, style="Padrao.TFrame")
    self.frame_menu.grid(row=1, column=0, columnspan=2, pady=0, padx=2, sticky="nsew")
    self.frame_detalhes = ttk.Frame(self.root, width=700, height=298, style="Padrao.TFrame")
    self.frame_detalhes.grid(row=2, column=0, columnspan=1, pady=2, padx=2, sticky="nsew")
    self.frame_crud = ttk.Frame(self.root, width=572, height=298, style="Padrao.TFrame")
    self.frame_crud.grid(row=2, column=1, columnspan=1, pady=2, padx=2, sticky="nsew")
    self.frame_grade = ttk.Frame(self.root, width=1276, height=304, style="Padrao.TFrame")
    self.frame_grade.grid(row=3, column=0, columnspan=2,pady=0, padx=2, sticky="nsew")

    # Criação dos widgets
    self.criar_widgets_frame_logo()

  def criar_widgets_frame_logo(self):
    self.o = Image.open(fp="imagens/img_alunos.png")
    self.r = self.o.resize(size=(40,40))
    self.img = ImageTk.PhotoImage(self.r)
    
    self.lbl_img = ttk.Label(self.frame_logo, image=self.img, width=40,
                            compound="left", anchor="nw", background=self.cor_fundo_logo)
    self.lbl_img.image = self.img
    self.lbl_img.place(x=0, y=3)
    self.lbl_txt = ttk.Label(self.frame_logo, text="Cadastro de Alunos", width=18,
                            compound="center", anchor="center",
                            font=self.fonte, background=self.cor_fundo_logo,
                            foreground=self.cor_fonte_logo)
    self.lbl_txt.place(x=52, y=8)
    

def main():
  root = tk.Tk()
  appGerenciaGUI(root)
  root.mainloop()

if __name__ == "__main__":
  main()