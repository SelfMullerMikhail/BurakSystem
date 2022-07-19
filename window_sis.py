import tkinter as tk
from DB import *

# Functions
def upgrade():
    window_enter.delete('1.0', tk.END)
    bg = parsing_bd()
    show_summ()
    window_enter.insert('1.0', bg)

# def show_menu():
#     window_enter.delete('1.0', tk.END)
#     men = menu_pars()
#     window_enter.insert('1.0', men)

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

################################## Create buttons menu
# functions = []
# got_hight_menu = got_count_menu()
# line = (got_hight_menu[0]//3) + 1
# counter = 1
# y=30
# for i in range(line):
#     x = 550
#     y += 60
#     for i in range(3):
#         conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
#         cursor = conn.cursor()
#         cursor.execute(f'SELECT name FROM menu WHERE id = {counter}')
#         menu = cursor.fetchone()
#         counter += 1
#         menu = str(menu)
#         if menu == "None":
#             conn.close()
#             break
#         i = tk.Button(text=f'{menu}', width=15, height=3, command=menu)
#         i.place(x=x, y=y)
#         x += 130
#         conn.close()
#         def drink_add():
#             conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
#             cursor = conn.cursor()
#             cursor.execute(f'INSERT orders (id_sell_table, id_menu, counts) VALUES (1, 3, 1)')
#             conn.commit()
#             conn.close()
#         def menu():
#             upgrade()
#             drink_add()
#         functions.append(menu)

#  Lable
label = tk.Label(text="BurakSystem")
label.grid(row=0, column=1, sticky = "n")
# main window
window_enter = tk.Text(width = 45)
window_enter.place(x = 20, y = 90)
# summ_window
window_summ = tk.Entry()
window_summ.place(x = 260, y = 480)

window.mainloop()
