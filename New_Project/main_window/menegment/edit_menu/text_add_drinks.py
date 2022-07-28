import tkinter as tk
from New_Project.main_window.db_helper import Db_helper

class Text_add_drinks():

    def insert(self):
        self.drinks = self.helper.execute_query_fetchall("SELECT name, cost FROM menu")
        for i in self.drinks:
            self.insert_drinks = f"{i[0]}, {i[1]} \n"
            self.text.insert("1.0", self.insert_drinks)

    def create(self):
        self.text = tk.Text(self.add_drinks_window, width=45)
        self.text.place(x=130, y=10)

    def delete(self):
        self.text.delete("1.0", tk.END)

    def __init__(self, add_drinks_window):
        self.helper = Db_helper()
        self.add_drinks_window = add_drinks_window
        self.create()
        self.insert()