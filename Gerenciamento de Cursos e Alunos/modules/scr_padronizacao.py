import customtkinter

def cor(n) -> str:
  match n:
    case 1:
      return '#0E2B4A' # Cor Background logo
    case 2:
      return '#FFFFFF' # Cor Fonte branca
    case 3:
      return '#0E2B4A' # Cor Fonte padrão

def fonte(n) -> str:
  
  match n:
    case 1:
      return customtkinter.CTkFont(family='Ubuntu Bold', size=34) # Fonte logo
    case 2:
      return customtkinter.CTkFont(family='Ubuntu Medium', size=20) # Fonte tab
    case 3:
      return customtkinter.CTkFont(family='Ubuntu Medium', size=15) # Fonte notifição