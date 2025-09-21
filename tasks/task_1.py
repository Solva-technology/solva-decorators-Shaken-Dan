from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(str(a) for a in args)
        print(f"Вызов: {func.__name__}({args_str})")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper
