import tkinter as tk
from DB import *

# Functions
def upgrade():
    window_enter.delete('1.0', tk.END)
    bg = parsing_bd()
    show_summ()
    window_enter.insert('1.0', bg)
    # sums = tables_summ()

def show_menu():
    window_enter.delete('1.0', tk.END)
    men = menu_pars()
    window_enter.insert('1.0', men)

def show_summ():
    window_summ.delete(1, tk.END)
    sums = tables_summ()
    window_summ.insert(1, sums)

def clear_tabl():
    clear()
    upgrade()

def switch_table_1():
    table_1_func()
    upgrade()

def switch_table_2():
    table_2_func()
    upgrade()

def switch_table_3():
    table_3_func()
    upgrade()



window = tk.Tk()
window.columnconfigure(1, minsize=1000)
window.rowconfigure([0, 1], minsize=350)

########## Button

clear_but = tk.Button(text = 'clear', width = 15, height = 3, command = clear_tabl)
clear_but.place(x = 390, y = 415)

table_1 = tk.Button(text = 'table_1', width = 15, height = 3, command = switch_table_1)
table_1.place(x = 10, y = 25)

table_2 = tk.Button(text = 'table_2', width = 15, height = 3, command = switch_table_2)
table_2.place(x = 140, y = 25)

table_3 = tk.Button(text = 'table_3', width = 15, height = 3, command = switch_table_3)
table_3.place(x = 270, y = 25)

def americano_f():
    Americano_add()
    upgrade()
americano = tk.Button(text = 'Americano', width = 15, height = 3, command = americano_f)
americano.place(x = 550, y = 90)

def latte_f():
    Latte_add()
    upgrade()
latte = tk.Button(text = 'Latte', width = 15, height = 3, command = latte_f)
latte.place(x = 680, y = 90)

def cuppuccino_f():
    Cappuccino_add()
    upgrade()
cappuccino = tk.Button(text = 'Cappuccino', width = 15, height = 3, command = cuppuccino_f)
cappuccino.place(x = 810, y = 90)









label = tk.Label(text="BurakSystem")
label.grid(row=0, column=1, sticky = "n")

window_enter = tk.Text(width = 45)
window_enter.place(x = 20, y = 90)

window_summ = tk.Entry()
window_summ.place(x = 260, y = 480)

window.mainloop()
