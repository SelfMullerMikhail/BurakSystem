from pydoc import Helper
import tkinter as tk
from main_window.db_helper import Db_helper

class Create_botton_insert():
    def insert(self):
        self.text_info = self.text.get()
        self.helper.execute_query_insert(f"INSERT INTO warehouse (name_ingr, total, id_massa) VALUES ('{self.text_info}', 1000, 'gr');")
        self.info_window.clear()
        self.info_window.insert()
        
    def create(self):
        self.botton = tk.Button(self.warehouse_window, text="Insert", command=self.insert)
        self.botton.place(x = 550, y = 30)
    
    def __init__(self, warehouse_window, text, info_window):
        self.info_window = info_window
        self.text = text
        self.helper = Db_helper()
        self.warehouse_window = warehouse_window
        self.create()