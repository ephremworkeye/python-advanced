# *args and **kwargs allow you to pass multiple arguments or keyword arguments to a function
# args is for tuple

def sum_list(*args):
    result = 0
    for num in args:
        result += num
    return result

print(sum_list(1, 2, 3, 4, 5))


# if we want to change the name args

def sum_list(*integers):
    result = 0
    for num in integers:
        result += num
    return result

print(sum_list(1, 2, 3, 4, 5))



def f(a, *, b):
    return a, b

print(f(1, b=2)) # it will print(1, 2)
print(f.__code__)
print(f.__code__.co_varnames) # local variable in funciton
print(f.__code__.co_argcount)


# kwargs fro dictionary
def display_fullname(**kwargs):
    result = ''
    for name in kwargs.values():
        result += name + ' '
    return result

print(display_fullname(first="John", lname= 'Walter'))

# we can  change the name kwargs

def display_fullname(**person):
    result = ''
    for name in person.values():
        result += name + ' '
    return result

print(display_fullname(first="John", lname= 'Walter'))


# ordering matters in args and kwargs
# this is correct order
def func(a, b, *args, **kwargs):
    pass

# this is not the corrrect order
def func2(a, b, **kwargs, *args):
    pass


# unpacking
integers = [1, 2, 3, 4] # it was list 
print(*integers) # but now it is content of list

numbers = [1, 2, 3,4, 5]
numberOne, numberTwo, *others = numbers # 
first, *all_middle, last = numbers
print(numberOne, numberTwo, others)
print(first, all_middle, last)

# if we want to unpack string inside the list
word = [*'hello world']
*another, = 'hellow world' 
print(word)
print(another)