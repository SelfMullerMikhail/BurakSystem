import tkinter as tk
import mysql.connector
from mysql.connector import Error
from db_helper import db_helper

def table_1_func():
    global peremen
    peremen = 1

def table_2_func():
    global peremen
    peremen = 2

def table_3_func():
    global peremen
    peremen = 3

def return_table():
    try:
        return peremen
    except:
        print("Error table")

helper = db_helper()

def parsing_bd():
    text = helper.execute_query_fetchall(f'SELECT * FROM summ_count WHERE Tables = {peremen}')
    text = str(text)
    result = text.replace('), (', '\n').strip('[').strip(']').strip('(').strip(')').strip(",").strip("'")
    return result


def tables_summ():
    summ = helper.execute_query_fetchone(f'SELECT total FROM summ_one_table WHERE tables = {peremen}')
    result = str(summ).strip("((Decimal('").strip("'),)")
    return f" summ:  {result} TL"

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

