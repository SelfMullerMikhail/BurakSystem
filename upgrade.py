from main_window import window
import tkinter as tk

window = tk.Tk
def command_1():
    window.menu_upgrade()
am = tk.Button(text = "TRY", command = command_1)


window.mainloop()