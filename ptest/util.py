from functools import wraps
from time import time


def timed(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        start = time()
        result = f(*args, **kwds)
        elapsed = time() - start
        print("\n%s took %f s to finish\n" % (f.__name__, elapsed))
        return result
    return wrapper
