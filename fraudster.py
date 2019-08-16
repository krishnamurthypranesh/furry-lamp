"""Random script in which we try to check if a decorator has certain functions
inside it. Functional programming's equivalent to hasattr(). Booyah!
pep-8 compliant 😏
"""

def timeFunc(func):

    def wrapper(*args, **kwargs):

        start = time.time()
        rv = func(*args, **kwargs)
        def something():
            pass
        end = time.time()
        print(end - start)
        return rv
    return wrapper


@timeFunc
def loopster(n):
    for i in range(n):
        print(i)

print([loopster.__closure__[i].cell_contents.__name__ for i in range(len(loopster.__closure__))])
