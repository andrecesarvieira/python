import customtkinter

from PIL import Image

class MainGui():
  def __init__(self):
    self.root = customtkinter.CTk()
    self.root.title('UI Moderna Tkinter')
    self.root.resizable(False, False)

    # Centralizar o início da aplicação, considerando a resolução do sistema
    LARGURA = 1600
    ALTURA = 900
    MENU_DO_WINDOWS = 80
    tela_largura = self.root.winfo_screenwidth()
    tela_altura = self.root.winfo_screenheight() - MENU_DO_WINDOWS
    x_coordenada = int((tela_largura / 2) - (LARGURA / 2))
    y_coordenada = int((tela_altura / 2) - (ALTURA / 2))
    self.root.geometry(f'{LARGURA}x{ALTURA}+{x_coordenada}+{y_coordenada}')

    customtkinter.set_appearance_mode('System')

    frm_main1 = customtkinter.CTkFrame(self.root, fg_color='black', 
                                          border_width=0, corner_radius=0)
    frm_main1.pack(side='right', expand=True, fill='both')

    lbl_main1 = customtkinter.CTkLabel(frm_main1, text='UI Moderna Tkinter', font=('Arial', 140))
    lbl_main1.pack(expand=True)

    self.menu_fechado()
    self.root.mainloop()

  def menu_fechado(self):
    frm_hub1 = customtkinter.CTkFrame(self.root, fg_color='gray', height=900, width=60,
                                          border_width=0, corner_radius=0)
    frm_hub1.place(x=0, y=0)

    img = customtkinter.CTkImage(Image.open(r'abrir.png'), size=(40, 40))
    btn_hub1 = customtkinter.CTkButton(frm_hub1, image=img, width=50, text='',
                                            border_width=0, corner_radius=0, command=self.menu_aberto,
                                            fg_color='transparent', hover_color='gray')
    btn_hub1.place(x=5, y=5)

  def menu_aberto(self):
    def destruir():
      frm_hub2.destroy()
    
    frm_hub2 = customtkinter.CTkFrame(self.root, fg_color='gray', height=900, width=280,
                                      border_width=0, corner_radius=0)
    frm_hub2.place(x=0, y=0)

    img = customtkinter.CTkImage(Image.open(r'fechar.png'), size=(40, 40))
    btn_hub2 = customtkinter.CTkButton(frm_hub2, image=img, width=50, text='',
                                            border_width=0, corner_radius=0, command=destruir,
                                            fg_color='transparent', hover_color='gray')
    btn_hub2.place(x=5, y=5)

if __name__ == '__main__':
  MainGui()

