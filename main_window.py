import tkinter as tk
from db_helper import db_helper
from create_menu_botton import create_menu_botton, create_menegment_botton
from upgrade_all import upgrade
from widget import Label

class Window(tk.Tk):



    def __init__(self):
        super().__init__()
        self.helper = db_helper()
        
        self.Table_Clear = tk.Button(self, text = "Clear", command = self.clear_button, width = 15, height =3)
        self.Table_Clear.place(x = 380, y = 430)

        self.window_enter = tk.Text(self, width=45)
        self.window_enter.place(x=130, y=10)

        self.window_summ = tk.Entry(self)
        self.window_summ.place(x=370, y=400)

        self.label_window = Label.label(self, "BurakSystem")

        self.menu_upgrade = upgrade()

        self.menu_botton = create_menu_botton(self.window_enter, self.window_summ)

        self.tables_botton = create_menegment_botton(self.window_enter, self.window_summ)
    def clear_button(self):
        self.menu_upgrade.clear(self.window_enter, self.window_summ)

    def menu_upgrade(self):
        self.menu_upgrade.upgrade_all(self.window_enter, self.window_summ)



if __name__ == "__main__":
    window = Window()
    window.geometry("1000x600")
    window.mainloop()



