import tkinter as tk
from New_Project.main_window.db_helper import Db_helper
from New_Project.main_window.switcher import switcher
import re

class Drinks():
    helper = Db_helper()
    # tabel = Switch_tab()
    def got_name_drink(self, counter):
        self.name = str(self.helper.execute_query_fetchone(f"SELECT name FROM menu WHERE id = {counter}"))
        self.name = re.findall(r"\w+", self.name)
        return self.name

    def get_line(self):
        self.max_line = self.helper.execute_query_fetchone("SELECT max(id) FROM menu")
        self.max_line = (self.max_line[0] // 3) + 1
        return self.max_line

    def buttons_create(self, counter, y, x):
        def button_function():
            # self.tab = self.tabel.got_tab()
            self.tab = switcher.got_tab()
            self.helper.execute_query_insert(
                f"INSERT orders (id_sell_table, id_menu, counts) VALUES({self.tab}, {counter}, 1)")
            self.text_drinks.delete()
            self.text_drinks.insert(self.tab)
            self.summ_drinks.delete()
            self.summ_drinks.insert(self.tab)
            print(f"Drinks is work! tab: {self.tab}")
        self.i = tk.Button(text=self.name, command=button_function, width=15, height=3)
        self.i.place(y=y, x=x)

    def menu(self):
        self.counter = 1
        self.max_line = self.get_line()
        self.y = 20
        for b in range(self.max_line):
            self.x = 450
            self.y += 60
            for i in range(3):
                self.name = self.got_name_drink(self.counter)
                if self.name[0] == "None":
                    break
                self.x += 130
                self.buttons_create(self.counter, self.y, self.x)
                self.counter += 1

    def __init__(self, self_text, self_summ):
        self.text_drinks = self_text
        self.summ_drinks = self_summ
        self.menu()
