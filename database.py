import sqlite3

db_name="config.db"

def init_db():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("create table if not exists settings(id int primary key, api_key varchar(255))")
    conn.commit()

    cursor.execute("select * from settings where id = 1")
    row = cursor.fetchone()
    
    conn.close()
    return row[1] if row else None

def save_key(api_key):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("insert or replace into settings(id, api_key) values(?, ?) ", (1, api_key))
    conn.commit()
    conn.close()