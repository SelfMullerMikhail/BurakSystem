from http.client import CONTINUE
from msilib.schema import tables
import tkinter as tk
from main_window.db_helper import Db_helper

class Text():
    
    def delete(self):
        self.text.delete("1.0", tk.END)

    def insert(self, tab):
        self.text_bd = self.helper.execute_query_fetchall(f"""SELECT id_sell_table, name_menu, cost 
                                                            FROM orders, menu 
                                                            WHERE orders.name_menu = menu.name 
                                                            AND id_sell_table = {tab}""")
        for i in self.text_bd:
            self.info = f"- {i[1]}, {i[2]}\n"
            self.text.insert("1.0", self.info)

    def insert_all(self):
        self.text_bd = self.helper.execute_query_fetchall(f"""SELECT id_sell_table, name_menu, cost 
                                                            FROM orders, menu 
                                                            WHERE orders.name_menu = menu.name
                                                            ORDER BY id_sell_table""")
        for i in self.text_bd:
            self.info = f"- {i[1]}, {i[2]}\n"
            if self.numb_me == i[0]:
                self.numb_me = i[0]
                self.text.insert("1.0", self.info)
            else:
                self.numb_me = i[0]
                self.text.insert("1.0", f'Table: {i[0]}\n\n')
                self.text.insert("1.0", self.info)

    def create_text(self):
        self.text = tk.Text(self.tables_from, width=45)
        self.text.place(x=130, y=30)

    def __init__(self, tables_from):
        self.tables_from = tables_from
        self.helper = Db_helper()
        self.numb_me = 0
        self.create_text()


