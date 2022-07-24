import tkinter as tk
from New_Project.tab import Switch_tab
from New_Project.db_helper import Db_helper

class Window_orders():
    tabe = Switch_tab()

    def insert(self):
        self.tab = self.tabe.got_tab()
        print(self.tab)
        self.window_orders = tk.Text(self.window, width=35)
        self.window_orders.place(x=10, y=10)
        self.text_bd = str(self.helper.execute_query_fetchall(f'SELECT * FROM summ_count WHERE Tables = 1')).replace('), (','\n').strip('[').strip(']').strip('(').strip(')').strip(",").strip("'")
        self.window_orders.insert("1.0", self.text_bd)

    def __init__(self, window):
        self.window = window
        self.helper = Db_helper()
        self.insert()
