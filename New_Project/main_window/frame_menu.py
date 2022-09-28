import tkinter as tk
from main_window.db_helper import Db_helper
from main_window.switcher import switcher

class Frame_menu():
    def create(self):
        self.frame = tk.Frame(self.main_window, width=530, height=350, relief= tk.RAISED, borderwidth = 2)
        self.frame.place(x=550, y=10)

    def delete(self):
        self.frame.destroy()

    def buttons_create(self, name, x , y):
        def button_function():
            self.tab = switcher.got_tab()
            if self.tab != "all":
                self.helper.execute_query_insert(f"INSERT INTO orders (id_sell_table, name_menu, counts) VALUES ({self.tab}, '{name[0]}', 1)")
                self.text_drinks.delete()
                self.text_drinks.insert(self.tab)
                self.summ_drinks.delete()
                self.summ_drinks.insert(self.tab)
                print(f"Drinks is work! tab: {self.tab}")

        self.i = tk.Button(self.frame, text=name, command=button_function, width=15, height=3, relief= tk.RAISED, borderwidth = 2)
        self.i.place(x = x, y = y)

    def menu(self):
        self.max_line_all = self.helper.execute_query_fetchall("SELECT name FROM menu")
        self.y = -55
        self.counter = 0
        for i in range(len(self.max_line_all)//3):
            self.x = 10
            self.y += 60
            for b in range(4):
                try:
                    self.buttons_create(self.max_line_all[self.counter], self.x, self.y)
                    self.x += 130
                    self.counter += 1
                except:
                    print("Botton drink error")
                    break
    def __init__(self, self_text, self_summ, main_window):
        self.main_window = main_window
        self.create()
        self.helper = Db_helper()
        self.text_drinks = self_text
        self.summ_drinks = self_summ
        self.menu()


