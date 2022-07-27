import tkinter as tk
from New_Project.main_window.db_helper import Db_helper

class Entery_data():
    def create_entery_from(self):
        self.entery_from = tk.Entry(self.history_window)
        self.entery_from.place(x = 500, y =20)
        self.entery_from.insert(0, self.dd_mm_yyyy)

    def create_entery_to(self):
        self.entery_to = tk.Entry(self.history_window)
        self.entery_to.place(x=650, y=20)
        self.entery_to.insert(0, self.dd_mm_yyyy)

    def show_history(self):
        self.data_from = self.entery_from.get()
        self.data_to = self.entery_to.get()
        self.history_text.delete()
        if self.data_from == self.dd_mm_yyyy and self.data_to == self.dd_mm_yyyy:
            self.history = self.helper.execute_query_fetchall("SELECT * FROM deposid")
            print("SELECT * FROM deposid")
            for row in self.history:
                self.history_text.insert(f"tab: {row[0]} TL: {row[1]} data: {row[2]}\n")
        else:
            self.history = self.helper.execute_query_fetchall(f'SELECT * FROM deposid WHERE DATE(times) >= "{self.data_from}" AND DATE(times) <= "{self.data_to}"')
            print('SELECT * FROM deposid WHERE DATE(times) >= "{self.data_from}" AND DATE(times) <= "{self.data_to}"')
            for row in self.history:
                self.history_text.insert(f"tab: {row[0]} TL: {row[1]} data: {row[2]}\n")
    def botton_show_func(self):
        self.botton_show = tk.Button(self.history_window, text="Show history", width=15, height=3,
                                     command=self.show_history)
        self.botton_show.place(x=780, y=10)




    def __init__(self, history_window, history_text):
        self.dd_mm_yyyy = "YYYY-MM-DD"
        self.history_text = history_text
        self.helper = Db_helper()
        self.history_window = history_window

        self.create_entery_from()
        self.create_entery_to()
        self.botton_show_func()



