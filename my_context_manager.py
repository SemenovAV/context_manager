from datetime import datetime


class MyContextManager:
    def __init__(self, log_file_path):
        self.path = log_file_path
        self.timestamp = lambda: datetime.now()

    def __enter__(self):
        self.log = open(self.path, 'a', encoding='utf-8')
        self.start = datetime.now()
        self.set_event('Код запущен.')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = datetime.now()
        if exc_tb:
            self.set_event(f'Ошибка: {exc_val}')
            self.set_event('Код остановлен.')
        else:
            self.set_event('Код остановлен.')
            self.time = self.stop - self.start
            self.set_event(f'Время работы: {self.time}')

    def set_event(self, message):
        event = f'{self.timestamp()}: {message}'
        self.log.write(event + '\n')
        print(event)
