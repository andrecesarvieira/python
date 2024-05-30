"""
Este módulo exibe elementos de tkinter
Autor: André Vieira
Data: 30/05/2024
"""
from tkinter import *

frm_main = Tk()

# Valores padrões da janela
frm_title = "Janela Principal"
frm_size = "1280x720"
frm_bg = "LightGray"
frm_icon: PhotoImage = PhotoImage(file="logo.png")

frm_main.iconphoto(False, frm_icon)
frm_main.title(frm_title)
frm_main.geometry(frm_size)
frm_main.resizable(height=False, width=False)
frm_main.config(background=frm_bg)


frm_main.mainloop()
