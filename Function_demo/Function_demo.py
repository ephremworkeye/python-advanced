# what is decorator
        # A function takes another function
        # Extends the behavior of that function
        # Without explicitly modifying the funciton

# def add_num(number):
#     return number + 5

# add_num(3) # calling a function

# copy_add_num = add_num # we can copy the function to another funciton, but they share the same memory address
# print(add_num) # they have the same adress location with the below one
# print(copy_add_num)

# def greeting(name):
#     return f'Hello {name}'
# print(greeting('Sador'))
# print(greeting) # we get the memory address

# def messaging(name):
#     return f'Hi {name} you are doing good'
# print(messaging('Sador'))

# these are two different function in differnet memory location
# we can pass these function into list

# funcs = [greeting, messaging]
# print(funcs[0]) # we get the memory address
# if we want we can invoke py passing the argument
# print(funcs[0]('Ephrem'))

# if we want we can loop through it 
# for func in funcs:
#     print(func)

# a function calling another function

# def func(another_func):
#     return another_func('Sador')

# print(func)
# print(func(greeting))
# print(func(messaging))

# Inner function
# def parent():
#     print('This is parent')
    
#     def child_one():
#         print('This is child one')
    
#     def child_two():
#         print('This is child two')
    
#     # we must to call the inner function inside parent function, otherwise error says funciton is not defined
#     child_two()
#     child_one()
# parent()
# child_one() # this is errror

# def parent(num):
#     print('This is parent')

#     def child_one():
#         print('This is child')
#     def child_two():
#         print('This is child two')
    
#     # if we want to call the funciton outside the parent function we need to return as callable here
#     if num == 1:
#         return child_one
#     else:
#         return child_two

# # parent(1)

# first = parent(1)
# second = parent(2)

# first()
# second()

# def User(username, password):
#     print('Welcome to our website')
#     def login():
#         print('You logged in to the dashboard')
#     def register():
#         print('Please register')
#     if username == 'sador' and password == '123':
#         return login
#     else:
#         return register

# account = User('sador', '123')
# account() # we need to call the the returned funciton



