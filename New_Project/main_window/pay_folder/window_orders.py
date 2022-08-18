import tkinter as tk
from main_window.table import switcher
from main_window.db_helper import Db_helper

class Window_orders():

    def delete(self):
        self.window_orders.delete("1.0", tk.END)

    def insert(self):
        self.tab = switcher.got_tab()
        print(self.tab)
        self.window_orders = tk.Text(self.window, width=35)
        self.window_orders.place(x=10, y=10)
        self.text_bd = self.helper.execute_query_fetchall(f'SELECT * FROM show_orders WHERE tables = {self.tab}')
        for i in self.text_bd:
            self.info = str(f"tab: {i[2]}   {i[1]} tl: {i[0]}\n")
            self.window_orders.insert("1.0", self.info)

    def __init__(self, window):
        self.window = window
        self.helper = Db_helper()
        self.insert()
