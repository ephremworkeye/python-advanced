class Person:
    def __init__(self, name=''):
        self.__name = 'sador'



class Student(Person): 
    def __init__(self):
        Person.__init__(self)
        print(self.__name)
        


p = Person()

s = Student()
print(s)