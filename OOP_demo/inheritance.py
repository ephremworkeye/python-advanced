# DRY concept 
# parent(base) and child(derived) class
# all classes inherint from object including the built-in types like int and str
# class hierarchy: python classes can inherit from another class

class Person:
    description = 'General person'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"My name is {self.name} and I am {self.age} years old")
    
    def eat(self, food):
        print(f'{self.name} eats {food}')

    def action(self):
        print(f"{self.name} jumps")

class Baby(Person):
    description = 'baby'

    def speak(self):
        print('ba ba ba ba ba')
    
    def nap(self):
        print(f'{self.name} takes a nap')

person = Person('James', 25)
person.speak()
person.eat('shiro')
person.action()

baby = Baby('Nathan', 1)
baby.speak()
baby.eat('cerial')
baby.action()

print(person.description)
print(baby.description)

# if we want to check baby is instance of Person
print(isinstance(baby, Person))
# or if we want to check Baby class is a subclass of Person
print(issubclass(Baby, Person))
# if we want to check baby is an object
print(isinstance(baby, object))