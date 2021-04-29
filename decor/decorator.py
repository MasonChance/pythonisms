from functools import wraps
import inspect


def deck_console(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        origin = func(*args, **kwargs)
        para_break = '*' * 10 + '\n'
        return para_break + origin + '\n' + para_break
    
    return wrapper


@deck_console
def custom_console_logger(var):
    var_name = inspect.signature(custom_console_logger)
    print(var_name)
    return f'{var_name} is asigned or returns as "{var}", of type {type(var)}'
