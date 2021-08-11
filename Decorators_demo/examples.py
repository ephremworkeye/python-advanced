from decor_example import *

@timer
def square_sum(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

square_sum(4)

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Hello {name}!"
    else:
        return f"Hello {name} you are already {age}"

make_greeting('Sador')
make_greeting('Sador', 4)