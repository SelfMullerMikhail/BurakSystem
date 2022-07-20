from DB import *
import tkinter as tk
from upgrade_all import upgrade

class create_menu_botton():
    helper = db_helper()
    upgrade = upgrade()
    def get_line(self):
        self.line = self.helper.execute_query_fetchone("SELECT max(id) FROM menu")
        self.line = (self.line[0] // 3) + 1
        return self.line

    def buttons_create(self, counter, y, x):
        def button_function():
            table = return_table()
            self.helper.execute_query_insert(f"INSERT orders (id_sell_table, id_menu, counts) VALUES({table}, {counter}, 1)")
            upgrade.upgrade_all()
            print("Work!")
        self.i = tk.Button(text=self.name, command=button_function, width=15, height=3)
        self.i.place(y=y, x=x)


    def __init__(self):
        self.counter = 1
        self.line = self.get_line()
        self.y = 20
        for b in range(self.line):
            self.x = 450
            self.y += 60
            for i in range(3):
                self.name = got_name(self.counter)
                if self.name == "None":
                    break
                self.x += 130
                self.buttons_create(self.counter, self.y, self.x)
                self.counter += 1

