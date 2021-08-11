# how to reuse decorators to and from another file
def say_hi(func):
    def wrapper():
        func()
        func()
    return wrapper

