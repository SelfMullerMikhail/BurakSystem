import tkinter as tk
from New_Project.main_window.db_helper import Db_helper

class Add_drinks():

    def add(self):
        self.drink = self.entry_name.get()
        self.cost = int(self.entry_cost.get())
        self.helper.execute_query_insert(f"INSERT menu (name, cost)  VALUES ('{self.drink}', {self.cost})")



    def create_entry(self):
        self.entry_name = tk.Entry(self.window_frame)
        self.entry_name.place(x = 500, y = 20)
        self.entry_cost = tk.Entry(self.window_frame)
        self.entry_cost.place(x=500, y=50)

    def create_botton(self):
        self.botton = tk.Button(self.window_frame, text = "ADD drinks", width=15, height=3, command = self.add)
        self.botton.place(x = 630, y = 20)

    def __init__(self, window_frame):
        # self.text_drinks = text_drinks
        self.helper = Db_helper()
        self.window_frame = window_frame
        self.create_entry()
        self.create_botton()

