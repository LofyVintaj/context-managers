import time


class CalculateTime:

    def __init__(self):
        pass

    def __enter__(self):
        self.start_time = time.time()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print(f"Elapsed time: {self.end_time - self.start_time:.2f} seconds")


with CalculateTime():
    for i in range(0, 10000000):
        print(f'i - {i}')