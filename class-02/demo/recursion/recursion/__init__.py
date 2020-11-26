__version__ = "0.1.0"


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)
