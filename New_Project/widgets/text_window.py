import tkinter as tk
from main_window.db_helper import Db_helper

class Text_window():

    def show_orders(self): 
        self.history = self.helper.execute_query_fetchall("SELECT * FROM deposid ")
        self.counter =0
        for row in self.history:
            self.text.insert(f"1.0", f"cash: {row[1]} card: {row[2]} total: {row[3]}\n\n")         
            self.info = self.helper.execute_query_fetchall(f"""SELECT tables, menu_name, price, datetimes
            FROM full_history WHERE datetimes = '{row[4]}' """)
            for raw in self.info:
                self.text.insert(f"1.0", f"--{raw[1]}  tl: {raw[2]}\n")
                self.counter += 1
            self.text.insert(f"1.0", f"{row[4]} tab:{row[0]}\n")
            self.counter += 1

    def create(self):
        self.text = tk.Text(self.window, width=45)
        self.text.place(x=self.x, y=self.y)

    def delete(self):
        self.text.delete("1.0", tk.END)

    def __init__(self, window, x, y):
        self.window = window
        self.x = x 
        self.y = y
        self.helper = Db_helper()
        self.create()
        self.show_orders()
       
        
        