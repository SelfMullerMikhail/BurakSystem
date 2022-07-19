import mysql.connector

class db_helper():
    def execute_query(self, query):
        conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        return result
        conn.close()