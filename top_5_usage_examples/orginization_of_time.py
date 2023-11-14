from contextlib import contextmanager
from time import time, sleep

@contextmanager
def timing():
    start_time = time()
    yield
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")

with timing():
    # Код, для которого измеряется время выполнения
    sleep(2)
# Время выполнения будет автоматически измерено и выведено после выхода из блока with