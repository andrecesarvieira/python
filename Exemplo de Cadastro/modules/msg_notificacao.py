# Objetivo: Enviar notificações para o usuário
# Autor...: André Vieira
# Data....: 5/6/24 -> desenvolvimento

import customtkinter
from PIL import Image
from datetime import datetime

from modules.scr_padronizacao import fonte

class Notificacao:
  @staticmethod
  def criar(frame_rodape, msg):
        # Criar label de mensagem para o usuário no frame_msg
        img = customtkinter.CTkImage(Image.open('Exemplo de Cadastro/pics/img_notificacao.png'), size=(18,18))
        
        lbl_msg_img = customtkinter.CTkLabel(frame_rodape, image=img, text='', anchor='w',
                                             compound="left", justify="left")
        lbl_msg_img.place(x=70, y=1)

        hora = datetime.now()
        lbl_hora = customtkinter.CTkLabel(frame_rodape, text=hora.strftime('%H:%M:%S') + "  -  ",
                                          compound="left", justify="left", anchor="w", font=fonte(3))
        lbl_hora.place(x=95, y=1)
        
        lbl_msg_txt = customtkinter.CTkLabel(frame_rodape, text=msg, font=fonte(3), width=200,
                                             compound="left", justify="left", anchor="w")
        lbl_msg_txt.place(x=152, y=1)        
        
        lbl_msg_img.after(10000, lambda: lbl_msg_img.destroy())
        lbl_hora.after(10000, lambda: lbl_hora.destroy())
        lbl_msg_txt.after(10000, lambda: lbl_msg_txt.destroy())