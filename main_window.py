from DB import *
from db_helper import db_helper
from create_menu_botton import create_menu_botton, create_menegment_botton
from upgrade_all import upgrade

class Window(tk.Tk):
    helper = db_helper()

    def __init__(self):
        super().__init__()

        # self.Table_1 = tk.Button(self, text="Table_1", command=self.Table_1, width = 15, height = 3)
        # self.Table_1.grid()
        #
        # self.Table_2 = tk.Button(self, text="Table_2", command=self.Table_2, width = 15, height = 3)
        # self.Table_2.grid()
        #
        # self.Table_3 = tk.Button(self, text="Table_3", command=self.Table_3, width = 15, height = 3)
        # self.Table_3.grid()
        #
        # self.Table_Clear = tk.Button(self, text = "Clear", command = self.clear_button, width = 15, height =3)
        # self.Table_Clear.place(x = 380, y = 430)

        self.label = tk.Label(self, text="BurakSystem")
        self.label.place(x=900, y=570)
        self.window_enter = tk.Text(self, width=45)
        self.window_enter.place(x=130, y=10)

        self.window_summ = tk.Entry(self)
        self.window_summ.place(x=370, y=400)

        self.menu_upgrade = upgrade()

        self.menu_botton = create_menu_botton()

        self.tables_botton = create_menegment_botton()



    # def Table_1(self):
    #     switch_table_bd(1)
    #     self.menu_upgrade.upgrade_all(self.window_enter, self.window_summ)
    #
    # def Table_2(self):
    #     switch_table_bd(2)
    #     self.menu_upgrade.upgrade_all(self.window_enter, self.window_summ)
    #
    # def Table_3(self):
    #     switch_table_bd(3)
    #     self.menu_upgrade.upgrade_all(self.window_enter, self.window_summ)

    def clear_button(self):
        self.menu_upgrade.clear(self.window_enter, self.window_summ)

    def menu_upgrade(self):
        self.menu_upgrade.upgrade_all(self.window_enter, self.window_summ)



if __name__ == "__main__":
    window = Window()
    window.geometry("1000x600")
    window.mainloop()



