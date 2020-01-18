from datetime import datetime


class MyContextManager:

    def __enter__(self):
        self.start = datetime.now()
        print('Код запущен:', self.start)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = datetime.now()
        print('Код остановлен:', self.stop)
        print('Время работы:', self.stop - self.start)
