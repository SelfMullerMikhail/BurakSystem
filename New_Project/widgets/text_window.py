import tkinter as tk
from main_window.db_helper import Db_helper

class Text_window():

    def show_orders(self): 
        print(self.type_of_show)
        if self.type_of_show == "today_story":
            self.history = self.helper.execute_query_fetchall("SELECT * FROM deposid WHERE DATE(times) = CURRENT_DATE ")
            for row in self.history:
                self.text.insert(f"1.0", f"cash: {row[1]} card: {row[2]} total: {row[3]}\n\n")         
                self.info = self.helper.execute_query_fetchall(f"""SELECT tables, menu_name, price, datetimes
                FROM full_history WHERE
                datetimes = '{row[4]}' AND DATE(datetimes) = CURRENT_DATE; """)
                for raw in self.info:
                    self.text.insert(f"1.0", f"--{raw[1]}  tl: {raw[2]}\n")
                self.text.insert(f"1.0", f"{row[4]} tab:{row[0]}\n")

        elif self.type_of_show == "full_story":
            self.history = self.helper.execute_query_fetchall("SELECT * FROM deposid ")
            for row in self.history:
                self.text.insert(f"1.0", f"cash: {row[1]} card: {row[2]} total: {row[3]}\n\n")         
                self.info = self.helper.execute_query_fetchall(f"""SELECT tables, menu_name, price, datetimes
                FROM full_history WHERE datetimes = '{row[4]}' """)
                for raw in self.info:
                    self.text.insert(f"1.0", f"--{raw[1]}  tl: {raw[2]}\n")
                self.text.insert(f"1.0", f"{row[4]} tab:{row[0]}\n")



    def create(self):
        self.text = tk.Text(self.window, width=45)
        self.text.place(x=self.x, y=self.y)

    def delete(self):
        self.text.delete("1.0", tk.END)

    def __init__(self, window, x, y, type_of_show):
        self.type_of_show = type_of_show
        self.window = window
        self.x = x 
        self.y = y
        self.helper = Db_helper()
        self.create()
        self.show_orders()
       
        
        