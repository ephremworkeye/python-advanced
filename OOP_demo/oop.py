 # classes are used to create objects
 # we can create many, unique objects from a single class
 # classes define a type
 # the process of creating an object from a class is called instantiation

 # 'properties' are actually called attributes
 # Instance attributes are unique to each object created

 # initializer /constructor 

class Dog:
    species = 'mammal' # class attibutes - Every dog will be created as a mammal
    def __init__(self, name, age):
        # initializer
        self.name = name  
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} sounds {sound}"

    def birthday(self):
        self.age += 1

# instaniation of class
# these objects are unique
kobe = Dog("kobe", 3)
milo = Dog("milo", 4)
# print(kobe.name, kobe.age)
# kobe.age = 10
# kobe.species = 'canis'
# # print(kobe == milo) # false
# print(kobe.name, kobe.age)

print(kobe.description())
print(kobe.speak('wooowoo!'))
kobe.birthday()
print(kobe.description()) # here is the age will be changed becuase of birthday function
