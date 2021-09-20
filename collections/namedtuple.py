from collections import namedtuple
Car = namedtuple('Car', ['color', 'make', 'model', 'mileage'])
my_car = Car('Gray', 'Toyota', 'Camry', 10000)
print(my_car.color)
print(my_car[0])
