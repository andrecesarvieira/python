import customtkinter

from modules.scr_padronizacao import fonte
from modules.scr_padronizacao import cor

class Frames:
    @staticmethod
    def criar(tab) -> str:
        # Caso os frames já tenham sido criados, retorna None
        for i in tab.winfo_children():
            if isinstance(i, customtkinter.CTkFrame):
                return None

        # Criar frames nas tab passada por parametro
        frm2_menu = customtkinter.CTkFrame(tab, height=50, corner_radius=0)
        frm2_corpo = customtkinter.CTkFrame(tab, height=320, corner_radius=0)
        frm2_grade = customtkinter.CTkFrame(tab, height=330, corner_radius=0)
        frm2_menu.pack(fill="x", expand=False)
        frm2_corpo.pack(fill="both", expand=True)
        frm2_grade.pack(fill="x", expand=False)
        
        # Criar botões do frame menu
        btn_novo = customtkinter.CTkButton(frm2_menu, text="Novo", corner_radius=32, font=fonte(4), 
                                           text_color=cor(2), border_width=2, border_color=cor(2))
        btn_alterar = customtkinter.CTkButton(frm2_menu, text="Alterar", corner_radius=32, font=fonte(4), 
                                              text_color=cor(2), border_width=2, border_color=cor(2))
        btn_salvar = customtkinter.CTkButton(frm2_menu, text="Salvar", corner_radius=32, font=fonte(4), 
                                             text_color=cor(2), border_width=2, border_color=cor(2))
        btn_excluir = customtkinter.CTkButton(frm2_menu, text="Excluir", corner_radius=32, font=fonte(4),
                                              text_color=cor(2), border_width=2, border_color=cor(2))

        btn_novo.pack(side='left', padx=10, pady=15)
        btn_alterar.pack(side='left', padx=5, pady=15)   
        btn_salvar.pack(side='left', padx=10, pady=15)
        btn_excluir.pack(side='left', padx=45, pady=15)
                
        return frm2_corpo