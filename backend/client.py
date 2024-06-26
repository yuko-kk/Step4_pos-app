# client.py
import mysql.connector
from mysql.connector import errorcode, connection
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込む
load_dotenv()

# 環境変数から接続情報を取得
config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'client_flags': [mysql.connector.ClientFlag.SSL],
    'ssl_ca': os.path.join(os.path.dirname(__file__), os.getenv('SSL_CA_PATH'))
}

def get_db_connection() -> connection.MySQLConnection:
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        raise