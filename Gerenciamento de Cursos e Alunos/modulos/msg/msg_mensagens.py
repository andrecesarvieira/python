class Mensagem_Erro():

  def Origem_Msg(self, classe, arquivo) -> str:
    self.msg = "(" + classe + " -> " + arquivo + ")"
    return self.msg