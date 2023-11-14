import sqlite3

with sqlite3.connect('example.db') as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM table_name')
    data = cursor.fetchall()
# Соединение с базой данных будет автоматически закрыто после выхода из блока with

