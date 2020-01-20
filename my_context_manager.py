from datetime import datetime

'''Замеряет скорость работы кода. Результат печатает в консоль и логирует в файл.'''


class MyContextManager:
    def __init__(self, log_file_path):
        self.path = log_file_path

    def __enter__(self):
        self.log = open(self.path, 'a', encoding='utf-8')
        self.start_time = datetime.now()
        self.set_event('Код запущен.')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_time = datetime.now()
        if exc_tb:
            self.set_event(f'Ошибка: {exc_val}')
            self.set_event('Код остановлен.')
        else:
            self.set_event('Код остановлен.')
            self.time = self.stop_time - self.start_time
            self.set_event(f'Время работы: {self.time}')

    def set_event(self, message):
        event = f'{datetime.now()}: {message}'
        self.log.write(event + '\n')
        print(event)
