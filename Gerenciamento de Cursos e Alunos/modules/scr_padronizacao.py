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
      return customtkinter.CTkFont(family='Bebas Neue', size=40, weight='bold') # Fonte logo
    case 2:
      return customtkinter.CTkFont(family='Bebas Neue', size=18, weight='normal') # Fonte pesquisar
    case 3:
      return customtkinter.CTkFont(family='Sans Seriff Collection Regular', size=11, weight='bold') # Fonte notifição
    case 4:
      return customtkinter.CTkFont(family='Bebas Neue', size=26, weight='normal') # Fonte botôes menu