import customtkinter

class Frames():
    @staticmethod
    def criar(aba) -> tuple:
        # Criar CTkFrames na guia alunos
        frame_menu = customtkinter.CTkFrame(aba, height=50)
        frame_menu.pack(fill="x", expand=True)
        
        frame_corpo = customtkinter.CTkFrame(aba, height=320)
        frame_corpo.pack(fill="x", expand=True)
        
        frame_grade = customtkinter.CTkFrame(aba, height=350)
        frame_grade.pack(fill="x", expand=True)

        return frame_menu, frame_corpo, frame_grade
    
    def widgets_menu():
        
        
        pass
        