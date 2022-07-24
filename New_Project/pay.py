import tkinter as tk

class Pay():
    def pay(self):
        print("Pay")

    def __init__(self):
        self.pay = tk.Button(text="Pay", width=15, height=3, command=self.pay)
        self.pay.place(x=250, y=400)