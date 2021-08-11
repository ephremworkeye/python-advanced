from decorators import say_hi, say_something, say_selam, return_greet
#with out arguments
@say_hi
def greet():
    print('printed from decorators file')

greet()



# with arguments
@say_something
def greeting(name):
    print(f'Hello {name}')

greeting('Sador')

#with args and kwargs
@say_selam
def selamta():
    print('this is without arguments')

selamta()

#with arguments
@say_selam
def selmata2(name):
    print(f'Selam {name}')

selmata2('Demelash')

@return_greet
def greet_return(name):
    print('Creating greeting...')
    return f'Hi {name}'

# print(greet_return('Sador'))
# or if we want to assign the retrun value
hi_sador = greet_return('Sador')
print(hi_sador)