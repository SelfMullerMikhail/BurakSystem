import tkinter as tk
from New_Project.main_window.db_helper import Db_helper

class Delete_drinks():
    def delete(self):
        self.name = self.entry.get()
        self.helper.execute_query_insert(f"DELETE FROM menu WHERE name = '{self.name}'")


    def create_botton(self):
        self.botton = tk.Button(self.edit_window, text = "Delete", command = self.delete)
        self.botton.place(x = 650, y = 150)

    def create_entry_name(self):
        self.entry = tk.Entry(self.edit_window)
        self.entry.place(x = 500, y = 150)

    def __init__(self, edit_window):
        self.helper = Db_helper()
        self.edit_window = edit_window
        self.create_entry_name()
        self.create_botton()
