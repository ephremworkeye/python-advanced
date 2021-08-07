# map() function returns a map object(which is an iterator) of the results after applying the given function to each of a given iterable
# syntax:  map(func, iter)

# we can define either in lambda or regular funciton and pass it to the map function
def square_number(x):
    return x**2

square_numbers = lambda x: x**2
result = map(square_numbers, range(4))
result2 = map(square_number, [1, 2, 3, 4, 5])
# print(result) # the will return a map object which is iterator like generators and has next method
# print(next(result))
# print(next(result))
# print(result.__next__())
# we can see the result in list or tuple but we will lose the benefit of memory
print(list(result))
print(list(result2))


# working with two lists

alist1 = [1, 3, 5]
alist2 = [2, 4, 2, 7]

result = map(lambda x, y: x + y, alist1, alist2)
print(tuple(result))

person = ['John', 'Alemu', 'Elias', 'Abiy']
output = list(map(list, person))
print(output)
