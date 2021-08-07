from functools import reduce

# The reduce function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along
# how to work?
    # 1. picked the first two elements and results obtained
    # 2. Apply same function to the previously attained result and the number just succeeding the second element and the the result is again stored and continue to the end

result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6])
print(result)


find_maximum = reduce(lambda a, b: a if a > b else b, [5, 2, 5, 3, 6, 9, 1])
print(find_maximum)

find_minimum = reduce(lambda f, g: f if f < g else g, [2, 7, 3, 5, 1, 7])
print(find_minimum)