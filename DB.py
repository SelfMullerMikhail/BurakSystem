import tkinter as tk

import mysql.connector
from mysql.connector import Error
#from window_sis import upgrade

def table_1_func():
    global peremen
    peremen = 1

def table_2_func():
    global peremen
    peremen = 2

def table_3_func():
    global peremen
    peremen = 3


def addTable(name):
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sell_table () VALUES ()')
    conn.close()

def parsing_bd():
    conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'zuma057195Z!', db = 'posterposs')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM summ_count WHERE Tables = {peremen} ORDER BY Tables')
    a = (str(cursor.fetchall()).replace('), (', '\n')).strip('[').strip(']').strip('(').strip(')').strip(",").strip("'")
    return a
    conn.close()

def menu_pars():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM menu')
    a = str(cursor.fetchall()).replace("), (", '\n').strip('[').strip(']').strip('(').strip(')')
    return a
    conn.close()

def tables_summ():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute(f'SELECT total FROM summ_one_table WHERE tables = {peremen}')
    a = 'summ: ' + str(cursor.fetchall()).strip("[(Decimal('").strip("'),)]") + ' TL'
    return a
    conn.close()

def clear():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM orders WHERE id_sell_table = {peremen}')
    conn.commit()
    conn.close()

def Americano_add():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute(f'INSERT orders (id_sell_table, id_menu, counts) VALUES ({peremen}, 3, 1)')
    conn.commit()
    conn.close()

def Latte_add():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute(f'INSERT orders (id_sell_table, id_menu, counts) VALUES ({peremen}, 1, 1)')
    conn.commit()
    conn.close()

def Cappuccino_add():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute(f'INSERT orders (id_sell_table, id_menu, counts) VALUES ({peremen}, 2, 1)')
    conn.commit()
    conn.close()


# table_3 = tk.Button(text = 'table_3', width = 15, height = 3, command = switch_table_3)
# table_3.place(x = 270, y = 25)

# class add_drinks():
#     def __init__(self, peremen):
#         self.conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
#         self.cursor = conn.cursor()
#         self.cursor.execute(f'INSERT orders (id_sell_table, id_menu, counts) VALUES ({peremen}, 2, 1)')
#         self.conn.commit()
#         self.conn.close()
#

def got_menu():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM menu')
    menu = cursor.fetchone()
    return  menu
    conn.close()

def got_count_menu():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute('SELECT max(id) FROM menu')
    count_menu = cursor.fetchone()
    return count_menu
    conn.close()




    #
    #
    # def espresso_d():
    #     espresso_add()
    #     upgrade()