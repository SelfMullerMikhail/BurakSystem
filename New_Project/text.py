import tkinter as tk
from db_helper import db_helper

class text():
    helper = db_helper()
    def delete(self):
        self.text.delete("1.0", tk.END)

    def insert(self, tab):
        self.text_bd = str(self.helper.execute_query_fetchall(f'SELECT * FROM summ_count WHERE Tables = {tab}')).replace('), (', '\n').strip('[').strip(']').strip('(').strip(')').strip(",").strip("'")
        self.text.insert("1.0", self.text_bd)
        print(f"Insert text is work! text_bd: {self.text_bd}")

    def __init__(self):

        self.text = tk.Text(width=45)
        self.text.place(x=130, y=10)
