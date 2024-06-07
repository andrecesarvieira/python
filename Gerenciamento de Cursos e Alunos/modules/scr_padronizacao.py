import customtkinter

def cor(n) -> str:
  if n == 1: return '#0E2B4A' # Cor Background logo
  if n == 2: return '#FFFFFF' # Cor Fonte branca
  if n == 3: return '#0E2B4A' # Cor Fonte padrão

def fonte(n) -> str:
  if n == 1: return customtkinter.CTkFont(family='Ubuntu Bold', size=34) # Fonte logo
  if n == 2: return customtkinter.CTkFont(family='Ubuntu Medium', size=22) # Fonte tab
  if n == 3: return customtkinter.CTkFont(family='Ubuntu Regular', size=15) # Fonte notifição