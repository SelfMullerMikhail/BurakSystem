import tkinter as tk
import mysql.connector
from mysql.connector import Error

def table_1_func():
    global peremen
    peremen = 1

def table_2_func():
    global peremen
    peremen = 2

def table_3_func():
    global peremen
    peremen = 3


def parsing_bd():
    conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'zuma057195Z!', db = 'posterposs')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM summ_count WHERE Tables = {peremen}')
    a = (str(cursor.fetchall()).replace('), (', '\n')).strip('[').strip(']').strip('(').strip(')').strip(",").strip("'")
    print(a)
    return a
    conn.close()

def tables_summ():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute(f'SELECT total FROM summ_one_table WHERE tables = 1')
    a = 'summ: ' + str(cursor.fetchall()).strip("[(Decimal('").strip("'),)]") + ' TL'
    return a
    conn.close()

def clear():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM orders WHERE id_sell_table = {peremen}')
    conn.commit()
    conn.close()


def got_count_menu():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute('SELECT max(id) FROM menu')
    count_menu = cursor.fetchone()
    return count_menu
    conn.close()

def got_name(id_fuc):
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute(f'SELECT name FROM menu WHERE id = {id_fuc}')
    name = str(cursor.fetchone()).strip('{"(').strip(',)"}')
    return name
    conn.close()

