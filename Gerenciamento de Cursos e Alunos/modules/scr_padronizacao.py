import customtkinter

def cor(n) -> str:
  match n:
    case 1:
      return '#14375E' # Cor Background logo
    case 2:
      return '#FFFFFF' # Cor Fonte branca

def fonte(n) -> str:
  match n:
    case 1:
      return customtkinter.CTkFont(family='Lucida Sans', size=38, weight='bold') # Fonte logo
    case 2:
      return customtkinter.CTkFont(family='Lucida Sans', size=22, weight='bold') # Fonte tab
    case 3:
      return customtkinter.CTkFont(family='Lucida Sans', size=11, weight='bold') # Fonte notifição
    case 4:
      return customtkinter.CTkFont(family='Lucida Sans', size=12, weight='bold') # Fonte botôes menu