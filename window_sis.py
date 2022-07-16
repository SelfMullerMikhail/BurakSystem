import tkinter as tk
from function_1 import parsing_bd, add_order, clear, menu_pars, tables_summ, table_1_func, table_2_func

# Functions
def upgrade():
    window_enter.delete('1.0', tk.END)
    bg = parsing_bd()
    window_enter.insert('1.0', bg)
    # sums = tables_summ()

def show_menu():
    window_enter.delete('1.0', tk.END)
    men = menu_pars()
    window_enter.insert('1.0', men)

def show_summ():
    window_enter.delete('1.0', tk.END)
    sums = tables_summ()
    window_enter.insert('1.0', sums)

def print_but():
    print(return_peremen())

def AddOrderAndUpdate():
    add_order()
    upgrade()

def clear_tabl():
    clear()
    upgrade()

window = tk.Tk()
window.columnconfigure(1, minsize=1000)
window.rowconfigure([0, 1], minsize=350)

########## Button
menu_but = tk.Button(text="Menu", width = 15, height = 3, command = show_menu)
menu_but.place(x = 10, y = 25)

clear_but = tk.Button(text = 'clear', width = 15, height = 3, command = clear_tabl)
clear_but.place(x = 140, y = 25)

add_but = tk.Button(text = 'add', width = 15, height = 3, command = AddOrderAndUpdate)
add_but.place(x = 270, y = 25)

upgr_but = tk.Button(text = 'upgrade', width = 15, height = 3, command = upgrade)
upgr_but.place(x = 400, y = 25)

tables_summ_but = tk.Button(text = 'summ', width = 15, height = 3, command = show_summ)
tables_summ_but.place(x = 310, y = 500)

table_1 = tk.Button(text = 'table_1', width = 15, height = 3, command = table_1_func)
table_1.place(x = 10, y = 500)

table_2 = tk.Button(text = 'table_2', width = 15, height = 3, command = table_2_func)
table_2.place(x = 140, y = 500)

# table_3 = tk.Button(text = 'table_3', width = 15, height = 3, command = print_but)
# table_3.place(x = 140, y = 650)




label2 = tk.Label(text="BurakSystem")
label2.grid(row=0, column=1, sticky = "n")

# bg = parsing_bd()
window_enter = tk.Text(width = 50)
# window_enter.insert('1.0', bg)
window_enter.place(x = 20, y = 90)

window.mainloop()
