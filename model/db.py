from abc import ABC
import mysql.connector

# import sys
# sys.path.append(
#     "C:/Users/ASTONLILLE012/OneDrive/Aston/Flask/demo_aston/venv/Lib/site-packages")


class DB(ABC):
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        database='beer',
        port=3306
    )

    @staticmethod
    def connect():
        try:
            cursor = DB.conn.cursor(dictionary=True)
            return cursor
        except mysql.connector.Error as e:
            print(e)
