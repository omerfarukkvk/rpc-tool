import tkinter as tk
from gui.widgets import set_rpc_names

def init_app():
    window = tk.Tk()
    window.title("Rpc Tool")
    window.geometry("800x400")
    window.minsize(800, 400)
    window.resizable(True, True)
    window.iconphoto(False, tk.PhotoImage(file="./assets/icon.png"))

    set_rpc_names(window)

    window.mainloop()
