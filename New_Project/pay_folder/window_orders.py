import tkinter as tk
# from New_Project.switcher import switcher
from New_Project.table import switcher
from New_Project.db_helper import Db_helper

class Window_orders():

    def insert(self):
        self.tab = switcher.got_tab()
        print(self.tab)
        self.window_orders = tk.Text(self.window, width=35)
        self.window_orders.place(x=10, y=10)
        self.text_bd = str(self.helper.execute_query_fetchall(f'SELECT * FROM summ_count WHERE Tables = {self.tab}')).replace('), (','\n').strip('[').strip(']').strip('(').strip(')').strip(",").strip("'")
        self.window_orders.insert("1.0", self.text_bd)

    def __init__(self, window):
        self.window = window
        self.helper = Db_helper()
        self.insert()
