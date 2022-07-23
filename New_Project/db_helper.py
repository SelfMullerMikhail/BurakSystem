import mysql.connector

class db_helper():

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = 'zuma057195Z!'
        self.db = 'posterposs'

    def execute_query_fetchone(self, query):
        self.conn = mysql.connector.connect(host=f'{self.host}', user=f'{self.user}', passwd=f'{self.passwd}', db=f'{self.db}')
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.result = self.cursor.fetchone()
        return self.result
        conn.close()

    def execute_query_fetchall(self, query):
        self.conn = mysql.connector.connect(host=f'{self.host}', user=f'{self.user}', passwd=f'{self.passwd}', db=f'{self.db}')
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        return self.result
        conn.close()

    def execute_query_insert(self, query):
        self.conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.conn.commit()
        self.conn.close()