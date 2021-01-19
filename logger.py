import datetime
def simple_logger(function):
    def new_function(*args, **kwargs):
        path = 'simple.log'
        print(args)
        print(kwargs)
        with open(path, 'a', encoding='utf-8') as f:
            f.write(f'{datetime.datetime.now()} вызвана функция {function.__name__},\n аргументы {args}, {kwargs}. '
                    f'\nВозвращаемое значение - {function(*args, **kwargs)} \n\n')
        return function
    return new_function

def complex_logger(path):
    def _complex_logger(function):
        def new_function(*args, **kwargs):
            print(args)
            print(kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'{datetime.datetime.now()} вызвана функция {function.__name__},\n аргументы {args}, {kwargs}. '
                        f'\nВозвращаемое значение - {function(*args, **kwargs)} \n\n')
            return function

        return new_function
    return _complex_logger