import time


def sleep(timeout):
    def the_real_decorator(function):
        def wrapper(*args, **kwargs):
            value = function(*args, **kwargs)
            time.sleep(timeout)
            return value
        return wrapper
    return the_real_decorator