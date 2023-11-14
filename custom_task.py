"""
    Вам нужно создать простой контекстный менеджер для работы с файлами.
    Контекстный менеджер должен записывать логи о времени начала и окончания работы с файлом.
"""

import time


class FileManager:

    def __init__(self, file_name):
        self.file = open(file_name, "w")

    def __enter__(self):
        self.start_time = time.time()
        self.file.write(f"Начало записи в файл - {self.start_time} \n")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.file.write(f"\nКонец записи в файл: {self.end_time} ")
        self.file.write(f"\nElapsed time: {self.end_time - self.start_time:.2f} seconds")
        self.file.close()
        # Другие операции с файлом могут быть выполнены здесь

    def write(self, text):
        self.file.write(text+"\n")


with FileManager("log.txt") as file:
    for i in range(0, 100000):
        print(i)
    file.write("Это данные, которые мы записываем в файл.")