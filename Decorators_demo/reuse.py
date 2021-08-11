from decorators import say_hi, say_something, say_selam
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

