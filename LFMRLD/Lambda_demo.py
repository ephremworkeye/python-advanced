# Lambda function is small anonymous function
# A lambda function can take any number of arguments, but can only have one expression
# Syntax  lambda arguments: expression

# with one argument
add_ten = lambda x: x + 10
print(add_ten(5)) 

# with two arguments
mult_numbers = lambda x, y: x * y
print(mult_numbers(5, 4))

# add and multiply
add_mult = lambda x, y: (x+y)*(x+y)
print(add_mult(3, 4))

# using lambda inside another function

def func(n):
    # if we want the funciton to multiplied by n
    return lambda a: a * n

result = func(2)
print(result(5))

# lambda with conditons

result = lambda x, y: x**2 if x < y else y**2
print(result(6, 4))


alist = [1, 2, 3, 4]
print(2 if 7 in alist else None)
