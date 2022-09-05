from pydoc import Helper
import tkinter as tk
from main_window.db_helper import Db_helper


class Info_window():
    def create_info_window(self):
        self.info_window = tk.Text(self.warehouse_window, width=45)
        self.info_window.place(x = 10, y =10)
        

    def insert(self):
        self.info = self.helper.execute_query_fetchall("SELECT * FROM warehouse")
        for raw in self.info:
            self.info_insert = f"{raw[0]} =  {raw[1]}\n"
            self.info_window.insert("1.0", self.info_insert)


    def clear(self):
        self.info_window.delete("1.0", tk.END)

    def __init__(self, warehouse_window):
        self.helper = Db_helper()
        self.warehouse_window = warehouse_window
        self.create_info_window()
        self.insert()
