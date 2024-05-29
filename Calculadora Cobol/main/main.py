from frontend.mainUI import CalculadoraLayoutCOBOL
import tkinter as tk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def main():
    root = tk.Tk()
    app = CalculadoraLayoutCOBOL(root)
    root.mainloop()


if __name__ == "__main__":
    main()
