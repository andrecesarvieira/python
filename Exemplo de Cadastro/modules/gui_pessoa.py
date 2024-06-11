import customtkinter

from modules.scr_padronizacao import fonte

class FramesPessoa:
    @staticmethod
    def criar(frame) -> str:
        # Caso os frames já tenham sido criados, retorna None
        for i in frame.winfo_children():
            if isinstance(i, customtkinter.CTkFrame):
                return None

        frm_pessoa = customtkinter.CTkFrame(frame, height=450, corner_radius=0, border_width=1)
        frm_pessoa.pack(expand=False, fill="x")
        
        frm_grid = customtkinter.CTkFrame(frame, height=360, corner_radius=0, border_width=1)
        frm_grid.pack(expand=False, fill="x")
        
        # Criar botões do frame menu
        btn_novo = customtkinter.CTkButton(frm_pessoa, text="Novo", corner_radius=32, font=fonte(4), 
                                           border_width=0)
        btn_alterar = customtkinter.CTkButton(frm_pessoa, text="Alterar", corner_radius=32, font=fonte(4), 
                                              border_width=0)
        btn_salvar = customtkinter.CTkButton(frm_pessoa, text="Salvar", corner_radius=32, font=fonte(4), 
                                             border_width=0)
        btn_excluir = customtkinter.CTkButton(frm_pessoa, text="Excluir", corner_radius=32, font=fonte(4),
                                              border_width=0)

        btn_novo.place(x=475, y=15)
        btn_alterar.place(x=630, y=15)
        btn_salvar.place(x=785, y=15)
        btn_excluir.place(x=995, y=15)