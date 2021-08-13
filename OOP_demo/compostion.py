# compostition:
    # composition models has a relationship
    # as part of relationship

    # example of composition
    # car and engine: car has engine and engine is a part of car

    # in python, one class can be a component of another composite class
    # in the last example, car was a composite class made up of an engine component


class Car:
    def __init__(self, brand, model, year, engine):
        self.brand = brand # str data type
        self.model model # str data type
        self.year = year # int data type
        self.engine = engine # does not have in buit in data type so composition comes here

    def turn_on(self):
        pass

    def accelerat(self):
        pass

    def park(self):
        pass

    def turn_off(self):
        pass

class Engine:
    def __init__(self, cylinders, efficieny, weight):
        self.cylinders = cylinders
        self.efficieny = efficieny
        self.weight = weight

    def ignite(self):
        pass

# question for compostion
# What is the type of engine attribute? 
    # engine
# Does the accelerate() method have access to the efficieny attribute?
    # yes the car object keeps tracj ojf an engine attribure (variable), which contains an efficiency attribure
# Can ignite() method in the enigine class access the brand attriburte?
    # no the engine class is 'blind' to where it's being used becuase it is not inheritance rather part of car class