from functools import wraps


def validate_positive(func):

    ZERO = 0

    @wraps(func)
    def wrapper(*args, **kwargs):

        for a in args:
            if a <= ZERO:
                raise ValueError("Все аргументы должны быть положительными")
        return func(*args, **kwargs)
    return wrapper
