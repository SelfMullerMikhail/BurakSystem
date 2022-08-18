import sqlite3
import os

class Db_helper():

    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.BASE_DIR, "PossSqLited.db")

    def execute_query_fetchone(self, query):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.result = self.cursor.fetchone()
        self.conn.close()
        return self.result
        

    def execute_query_fetchall(self, query):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        self.conn.close()
        return self.result

    def execute_query_insert(self, query):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.conn.commit()
        self.conn.close()