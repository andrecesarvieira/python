"""
Este módulo exibe elementos de tkinter
Autor: André Vieira
Data: 30/05/2024
"""
from tkinter import *

# Cores
cor_fundo = "LightGray"

frm_main = Tk()

frm_main.title(string="Janela Principal")
frm_main.geometry(newGeometry="1280x720")
frm_main.resizable(height=False, width=False)
frm_main.config(background=cor_fundo)
frm_main.iconphoto(False, PhotoImage(file="icon.png"))

frm_main.mainloop()
