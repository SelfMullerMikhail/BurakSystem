import tkinter as tk
from main_window.db_helper import Db_helper

class Add_drinks():

    def add(self):
        try:
            self.drink = self.entry_name.get()
            self.cost = int(self.entry_cost.get())
            if len(self.drink) >= 3:
                self.helper.execute_query_insert(f"INSERT menu (name, cost)  VALUES ('{self.drink}', {self.cost})")
                self.text_window.delete()
                self.text_window.insert()
                self.entry_name.delete(0, tk.END)
                self.entry_cost.delete(0, tk.END)
            else:
                print("More then 3 symbol ")
        except:
            print("Error add_drinks")



    def create_entry(self):
        self.entry_name = tk.Entry(self.window_frame)
        self.entry_name.place(x = 500, y = 20)
        self.entry_name.insert(0, "Name")

        self.entry_cost = tk.Entry(self.window_frame)
        self.entry_cost.place(x=500, y=50)
        self.entry_cost.insert(0, "Price")

    def create_botton(self):
        self.botton = tk.Button(self.window_frame, text = "ADD drinks", width=15, height=3, command = self.add)
        self.botton.place(x = 630, y = 20)


    def __init__(self, window_frame, text_window):
        self.text_window = text_window
        self.helper = Db_helper()
        self.window_frame = window_frame
        self.create_entry()
        self.create_botton()

