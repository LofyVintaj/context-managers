import sqlite3

class DatabaseConnection: # объявление класса
    def __init__(self, db_name):
        # конструктор который принимает в качестве аргумента имя бд
        self.db_name = db_name

    def __enter__(self):
        # точка входа это коннект по названию
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self,
                 exc_type,# непонятно что за аргумент
                 exc_val, # непонятно что за аргумент
                 exc_tb # непонятно что за аргумент
                 ):

        # точка выхода это просто обрыв соеденения
        self.conn.close()