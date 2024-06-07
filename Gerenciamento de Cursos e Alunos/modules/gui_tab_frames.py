import customtkinter

class Frames():
    @staticmethod
    def criar(tab) -> str:
        # Caso os frames já tenham sido criados, retorna None
        for i in tab.winfo_children():
            if isinstance(i, customtkinter.CTkFrame):
                return None

        # Criar frames nas tab passada por parametro
        frm2_menu = customtkinter.CTkFrame(tab, height=50)
        frm2_corpo = customtkinter.CTkFrame(tab, height=320)
        frm2_grade = customtkinter.CTkFrame(tab, height=330)
        frm2_menu.pack(fill="x", expand=False)
        frm2_corpo.pack(fill="both", expand=True)
        frm2_grade.pack(fill="x", expand=False)
        
        return frm2_corpo

    def widgets_menu():
        pass
        