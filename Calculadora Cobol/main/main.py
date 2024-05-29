import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from frontend.mainUI import CalculadoraLayoutCOBOL

def main():
    root = tk.Tk()
    app = CalculadoraLayoutCOBOL(root)
    root.mainloop()

if __name__ == "__main__":
    main()