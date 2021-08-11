# what is decorator
        # A function takes another function
        # Extends the behavior of that function
        # Without explicitly modifying the funciton

# simple decorator
# def my_decorator(func):
#     def wrapper(): #wrapping functon
#         print('printed before')
#         func()
#         print('printed after')
#         # print(wrapper)
#     return wrapper  # return function for later use


# def another():
#     print('Hi another')

# def added():
#     print('Wow it is added')

# another = my_decorator(another)
# added_func = my_decorator(added)
# another()
# added_func()

# syntathic sugar

# def my_decor(my_func):
#     def wrapper():
#         print('First print')
#         my_func()
#         print('Printed after "my_func" call')
#     return wrapper

# # instead of asigninig the returned function, we can use @parent funct
# @my_decor # add this befroe defining the function
# def func_one():
#     print('func_one is printed')

# @my_decor
# def func_two():
#     print('func_two is printed')


# func_one()
# func_two()
