# how to reuse decorators to and from another file
import functools
def say_hi(func):
    def wrapper():
        func()
        func()
    return wrapper

#with arguments
def say_something(func1):
    def wrapper_arg(argument):
        func1(argument)
    return wrapper_arg

# using *args and **kwargs
def say_selam(func3):
    def wrapper2(*args, **kwargs):
        func3(*args, **kwargs)
    return wrapper2

# retruning value from decorators
def return_greet(func4):
    @functools.wraps(func4) # this line is added for accurate introspection
    def wrapper_return(*args, **kwargs):
        return func4(*args, **kwargs)
    return wrapper_return
