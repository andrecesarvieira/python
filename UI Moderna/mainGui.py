import customtkinter
from PIL import Image

class MainGui():
  def __init__(self):
    self.root = customtkinter.CTk()
    self.root.title('UI Moderna Tkinter')
    self.root.resizable(False, False)

    self.centralizar_janela()
    self.frame_pesquisa()
    self.frame_principal()
    self.frame_compactado()

    self.root.mainloop()

  def sair_app(self):
    self.root.destroy()    

  def modo_aparencia(self):
    # Configurações para mudar modo aparência
    tema = customtkinter.get_appearance_mode()
    if tema == 'Dark':
      customtkinter.set_appearance_mode('light')
    else:
      customtkinter.set_appearance_mode('dark')

  def centralizar_janela(self):
    # Centralizar o início da aplicação, considerando a resolução do sistema
    LARGURA = 1600
    ALTURA = 900
    MENU_DO_WINDOWS = 80
    tela_largura = self.root.winfo_screenwidth()
    tela_altura = self.root.winfo_screenheight() - MENU_DO_WINDOWS
    x_coordenada = int((tela_largura / 2) - (LARGURA / 2))
    y_coordenada = int((tela_altura / 2) - (ALTURA / 2))
    self.root.geometry(f'{LARGURA}x{ALTURA}+{x_coordenada}+{y_coordenada}')

  def frame_pesquisa(self):
    # Criar frame de pesquisa no topo
    frm_search = customtkinter.CTkFrame(self.root, height=60, border_width=0, corner_radius=0)
    frm_search.pack(side='top', expand=False, fill='x')

    font1 = customtkinter.CTkFont(family='Bebas Neue', size=18, weight='normal')
    lbl_search = customtkinter.CTkLabel(frm_search, text='Pesquisar:', font=font1)
    lbl_search.place(x=1115, y=16)

    entry_search = customtkinter.CTkEntry(frm_search, width=400, font=('Arial', 13, 'normal'), corner_radius=5,
                                          placeholder_text='Digite o texto para pesquisar')
    entry_search.place(x=1185, y=15)

  def frame_principal(self):
    # Criar frame principal
    frm_main1 = customtkinter.CTkFrame(self.root, border_width=0, corner_radius=0)
    frm_main1.pack(side='bottom', expand=True, fill='both')

    lbl_main1 = customtkinter.CTkLabel(frm_main1, text='UI Moderna Tkinter', font=('Arial', 140))
    lbl_main1.pack(expand=True)

  def frame_compactado(self):
    self.frm_hub1 = customtkinter.CTkFrame(self.root, fg_color='gray', height=900, width=60,
                                          border_width=0, corner_radius=0)
    self.frm_hub1.place(x=0, y=0)

    # Botão abrir -> expandir menu
    img = customtkinter.CTkImage(Image.open('imagens//abrir.png'), size=(40, 40))
    btn_hub1 = customtkinter.CTkButton(self.frm_hub1, image=img, width=50, text='',
                                            border_width=0, corner_radius=0, command=self.frame_expandido,
                                            fg_color='transparent', hover_color='gray')
    btn_hub1.place(x=5, y=5)

    self.criar_widgets(self.frm_hub1)

  def frame_expandido(self):
    def destruir():
      self.frm_hub2.destroy()
    
    # Frame do menu expandido
    self.frm_hub2 = customtkinter.CTkFrame(self.root, fg_color='gray', height=900, width=230,
                                      border_width=0, corner_radius=0)
    self.frm_hub2.place(x=0, y=0)

    # Botão fechar -> compactar menu
    img = customtkinter.CTkImage(Image.open('imagens//fechar.png'), size=(40, 40))
    btn_hub2 = customtkinter.CTkButton(self.frm_hub2, image=img, width=50, text='',
                                            border_width=0, corner_radius=0, command=destruir,
                                            fg_color='transparent', hover_color='gray')
    btn_hub2.place(x=5, y=5)

    # Label do botão Sair
    font2 = customtkinter.CTkFont(family='Bebas Neue', size=26, weight='normal')
    lbl_sair = customtkinter.CTkLabel(self.frm_hub2, text = 'Sair do programa', font=font2,
                                      text_color='#1C1C1C')
    lbl_sair.place(x=60, y=854)

    self.criar_widgets(self.frm_hub2)

  def criar_widgets(self, frame):
    self.frame = frame

    self.img_modo = customtkinter.CTkImage(light_image=Image.open('imagens//mudar_escuro.png'),
                                           dark_image=Image.open('imagens//mudar_claro.png'), size=(40, 40))
    self.btn_modo = customtkinter.CTkButton(self.frame, image=self.img_modo, width=50, text='',
                                        border_width=0, corner_radius=0, command=self.modo_aparencia,
                                        fg_color='transparent', hover_color='gray')
    self.btn_modo.place(x=5, y=787)

    # Botão sair do programa
    img_sair = customtkinter.CTkImage(Image.open('imagens//sair.png'), size=(40, 40))
    btn_sair = customtkinter.CTkButton(self.frame, image=img_sair, width=50, text='',
                                            border_width=0, corner_radius=0, command=self.sair_app,
                                            fg_color='transparent', hover_color='gray')
    btn_sair.place(x=5, y=845)

if __name__ == '__main__':
  MainGui()