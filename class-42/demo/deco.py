from functools import wraps

def yo_mamma_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return f'Yo mamma says "{original_val}"'
    return wrapper


def sophisticated_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return f'It is with a great honor that I hear you say  "{original_val}"'
    return wrapper


@yo_mamma_decorator
@sophisticated_decorator
def just_saying(txt):
    return txt


if __name__ == "__main__":

    print(just_saying('I love star Wars'))

