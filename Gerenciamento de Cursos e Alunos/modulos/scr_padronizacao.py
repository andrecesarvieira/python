import customtkinter

def cor(n) -> str:
  if n == 1: return '#0E2B4A' # Cor Background logo
  if n == 2: return '#FFFFFF' # Cor Fonte branca
  if n == 3: return '#0E2B4A' # Cor Fonte padrão

def fonte(n) -> str:
  if n == 1: return customtkinter.CTkFont(family='JetBrains Mono ExtraBold', size=26) # Fonte logo
  if n == 2: return customtkinter.CTkFont(family='JetBrains Mono Bold', size=16) # Fonte padrão
  if n == 3: return customtkinter.CTkFont(family='Calibri', size=13, weight="bold") # Fonte notifição