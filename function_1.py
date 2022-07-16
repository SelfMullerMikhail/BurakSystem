import mysql.connector
from mysql.connector import Error
#from window_sis import upgrade

def table_1_func():
    global peremen
    peremen = 1
    print(peremen)

def table_2_func():
    global peremen
    peremen = 2
    print(peremen)

def addTable(name):
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sell_table () VALUES ()')
    conn.close()

def parsing_bd():
    conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'zuma057195Z!', db = 'posterposs')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM summ_count')
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
    cursor.execute(f'SELECT tables, total FROM summ_one_table WHERE tables = {peremen}')
    a = str(cursor.fetchall()).replace("Decimal(", " ").strip("[(").strip("))]").replace(")), (", "\n")
    return a
    conn.close()

def add_order():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute(f'INSERT orders (id_sell_table, id_menu, counts) VALUES ({peremen}, 2, 3)')
    conn.commit()
    conn.close()

def clear():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM orders WHERE id_sell_table = {peremen}')
    conn.commit()
    conn.close()


