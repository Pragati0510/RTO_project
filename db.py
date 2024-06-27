import mysql.connector as m

def connect_db():
    try:
        conn = m.connect(user='root',password='root',host='localhost',database='sys')
        print('connected to DB sucessfully!')
        return conn
    except:
        print("Error connecting to DB")