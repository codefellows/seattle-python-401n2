from functools import wraps

def emphasize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        return_val_from_undecorated_function = func(*args, **kwargs)

        emphasized = return_val_from_undecorated_function.upper() + "!!!"

        return emphasized

    return wrapper

def sarcastic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Sure, I\'d love to do "{orig_val}"'

    return wrapper




# @emphasize
@sarcastic_decorator
def proclaim(txt):
    # print('proclaim starting')
    return txt

@sarcastic_decorator
@emphasize
def restaurant_suggestion(cuisine):
    return cuisine

if __name__ == "__main__":
    # print(proclaim('spam is better than eggs'))
    # print(proclaim("Want to go for a walk?"))

    print(restaurant_suggestion('Mexican'))
