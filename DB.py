import tkinter as tk
from db_helper import db_helper

def table_1_bd():
    global peremen
    peremen = 1

def table_2_bd():
    global peremen
    peremen = 2

def table_3_bd():
    global peremen
    peremen = 3

def return_table():
    try:
        return peremen
    except:
        print("Error return_table")

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

def clear_bd():
    text = helper.execute_query_insert(f'DELETE FROM orders WHERE id_sell_table = {peremen}')

def got_name(id_fuc):
    name = helper.execute_query_fetchone(f'SELECT name FROM menu WHERE id = {id_fuc}')
    result = str(name).strip('{"(').strip(',)"}')
    return result
