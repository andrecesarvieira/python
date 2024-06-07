# Objetivo: Enviar notificações para o usuário
# Autor...: André Vieira
# Data....: 5/6/24 -> desenvolvimento

import customtkinter
from PIL import Image
from datetime import datetime

from modulos.scr_padronizacao import cor
from modulos.scr_padronizacao import fonte

class Notificar():
  def __init__(self, frame_rodape, msg):
        # Criar label de mensagem para o usuário no frame_msg
        img = customtkinter.CTkImage(Image.open('imagens/notificacao.png'), size=(22, 22))
        lbl_msg_img = customtkinter.CTkLabel(frame_rodape, image=img, text='', anchor='w')
        lbl_msg_img.place(x=7, y=6)

        hora = datetime.now()
        lbl_msg_txt = customtkinter.CTkLabel(frame_rodape, text=hora.strftime('%H:%M:%S') + msg,
                                anchor='nw', font=fonte(3))
        lbl_msg_txt.place(x=35, y=9)
        
        lbl_msg_img.after(8000, lambda: lbl_msg_img.destroy())
        lbl_msg_txt.after(8000, lambda: lbl_msg_txt.destroy())