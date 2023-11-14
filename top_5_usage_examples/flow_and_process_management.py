from multiprocessing import Process

with Process() as my_process:
    my_process.start()
    # Выполнение кода в контексте нового процесса
# Процесс будет автоматически остановлен после выхода из блока with
