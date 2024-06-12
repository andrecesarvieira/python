import customtkinter

from tkinter import ttk
from modules.scr_padronizacao import fonte

class FramesPessoa:
    def criar(self, frame) -> str:
        # Caso os frames já tenham sido criados, retorna None
        for i in frame.winfo_children():
            if isinstance(i, customtkinter.CTkFrame):
                return None

        self.frm_pessoa = customtkinter.CTkFrame(frame, height=389, width=1539, corner_radius=0, border_width=0)
        self.frm_pessoa.pack(expand=False, fill='x')
        
        self.frm_treeview = customtkinter.CTkFrame(frame, height=420, width=1539, corner_radius=0, border_width=0)
        self.frm_treeview.pack(expand=False, fill='x')

        self.widgets_pessoa()
        self.widget_treeview()
        return True
        
    def widgets_pessoa(self):
        # Criar botões do frame menu
        btn_novo = customtkinter.CTkButton(self.frm_pessoa, text='Novo', corner_radius=32, font=fonte(4), 
                                           border_width=0)
        btn_alterar = customtkinter.CTkButton(self.frm_pessoa, text='Alterar', corner_radius=32, font=fonte(4), 
                                              border_width=0)
        btn_salvar = customtkinter.CTkButton(self.frm_pessoa, text='Salvar', corner_radius=32, font=fonte(4), 
                                             border_width=0)
        btn_excluir = customtkinter.CTkButton(self.frm_pessoa, text='Excluir', corner_radius=32, font=fonte(4),
                                              border_width=0)

        btn_novo.place(x=475, y=15)
        btn_alterar.place(x=630, y=15)
        btn_salvar.place(x=785, y=15)
        btn_excluir.place(x=995, y=15)

    def widget_treeview(self):
        
        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview.Heading',
                        background='lightgray',
                        fieldbackground='#242424',
                        font=('Bebas Neue', 14, 'normal'))
        style.configure('Treeview',
                        background='lightgray',
                        fieldbackground='#242424',
                        borderwidth=1,
                        rowheight=26,
                        font=('Bebas Neue', 14, 'normal'))

        tbl_pessoa = ttk.Treeview(self.frm_treeview, columns=('id', 'nome', 'cpf', 'email', 'cel', 'sexo', 'nascimento' ), show='headings',
                                  height=15)
        
        scrollbar = ttk.Scrollbar(self.frm_treeview, orient="vertical", command=tbl_pessoa.yview)
        tbl_pessoa.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        
        tbl_pessoa.pack(expand=True, fill='both')

        tbl_pessoa.tag_configure('headings', background='lightgray')
        tbl_pessoa.heading('id', text='ID')
        tbl_pessoa.heading('nome', text='Nome')
        tbl_pessoa.heading('cpf', text='CPF')
        tbl_pessoa.heading('email', text='E-mail')
        tbl_pessoa.heading('cel', text='Celular')
        tbl_pessoa.heading('sexo', text='Sexo')
        tbl_pessoa.heading('nascimento', text='Dt. Nasc.')
        
        tbl_pessoa.column('id', width = 10, anchor='center')
        tbl_pessoa.column('nome', width = 350)
        tbl_pessoa.column('cpf', width = 50, anchor='center')
        tbl_pessoa.column('email', width = 250) 
        tbl_pessoa.column('cel', width = 50, anchor='center')
        tbl_pessoa.column('sexo', width = 10, anchor='center') 
        tbl_pessoa.column('nascimento', width = 50, anchor='center')

        # TESTE
        tbl_pessoa.insert('', 'end',text= '1',values=('1','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '2',values=('2','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '3',values=('3','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '4',values=('4','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '5',values=('5','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '6',values=('6','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '7',values=('7','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '8',values=('8','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '9',values=('9','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '10',values=('10','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '11',values=('11','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '12',values=('12','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '13',values=('13','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '14',values=('14','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '15',values=('15','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '16',values=('16','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '17',values=('17','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '18',values=('18','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '19',values=('19','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
        tbl_pessoa.insert('', 'end',text= '20',values=('20','André Vieira','999.999.999-99','teste@gmail.com','(99) 99999-9999','M','99/99/9999'))
