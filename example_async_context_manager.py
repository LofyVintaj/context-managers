import asyncio


class AsyncTimer:
    def __aenter__(self):
        self.start_time = asyncio.get_event_loop().time()
        return self

    def __aexit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = asyncio.get_event_loop().time() - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")


# Пример использования асинхронного контекстного менеджера
async def example():
    async with AsyncTimer() as timer:
        # Ваш асинхронный блок кода
        await asyncio.sleep(2)


# Запуск асинхронной функции
asyncio.run(example())