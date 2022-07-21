from BD import db_helper, BD
import tkinter as tk
from upgrade_all import upgrade

class create_menu_botton():
    helper = db_helper()
    upgrade_class = upgrade()
    database = BD()

    def get_line(self):
        self.line = self.helper.execute_query_fetchone("SELECT max(id) FROM menu")
        self.line = (self.line[0] // 3) + 1
        return self.line

    def buttons_create(self, counter, y, x, wind, summ):
        def button_function():
            table = self.database.return_table()
            self.helper.execute_query_insert(f"INSERT orders (id_sell_table, id_menu, counts) VALUES({table}, {counter}, 1)")
            self.upgrade_class.upgrade_all(wind, summ)
        self.i = tk.Button(text=self.name, command=button_function, width=15, height=3)
        self.i.place(y=y, x=x)


    def __init__(self, wind, summ):
        self.counter = 1
        self.line = self.get_line()
        self.y = 20
        for b in range(self.line):
            self.x = 450
            self.y += 60
            for i in range(3):

                self.name =self.database.got_name(self.counter)
                if self.name == "None":
                    break
                self.x += 130
                self.buttons_create(self.counter, self.y, self.x, wind, summ)
                self.counter += 1

class create_menegment_botton():
    database = BD()
    upgrade_class = upgrade()
    def buttons_create(self, number, wind, summ):
        def button_function():
            self.database.switch_table_bd(number)
            self.upgrade_class.upgrade_all(wind, summ)
        self.i = tk.Button(text=f"Table {number}", command=button_function, width=15, height=3)
        self.i.grid()

    def __init__(self, win, sum):
        self.helper = db_helper()
        self.line = self.helper.execute_query_fetchone("SELECT max(id) FROM sell_table")
        for i in range(self.line[0]):
            self.buttons_create(i+1, win, sum)



