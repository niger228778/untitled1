import sqlite3
connet = sqlite3.connect('qwe.sqlite')

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query executed successfuly')
    except str as e:
        print(f"The error `{e}` occured")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except str as e:
        print(f"The error `{e}` occured")

execute_query(connet, """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL,
    pass TEXT NOT NULL
);
""")

execute_query(connet, """
INSERT INTO
    users (login, pass)
VALUES
    ('ДИМОООООН', '1234'),
    ('ДИМОООООН1', '1234'),
    ('ДИМОООООН2', '1234'),
    ('ДИМОООООН3', '1234'),
    ('ДИМОООООН4', '1234')
""")

users = execute_read_query(connet, "SELECT * from 'users'")

for i in users:
    print(i)

connet.close()