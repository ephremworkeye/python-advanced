from decor_example import *

@timer
def square_sum(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

square_sum(4)
