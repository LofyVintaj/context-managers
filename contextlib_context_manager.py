import time
from contextlib import contextmanager


@contextmanager # декоратор для создания функции констекстного менеджера
def timer():
    start_time = time.time() # простой отсчет времени
    yield # что это?
    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time:.2f} seconds")


with timer():
    # действия, для которых хотим измерить время выполнения
    for i in range(0, 10000000):
        print(f'i - {i}')