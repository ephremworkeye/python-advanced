# Example 1
#=============>
# import datetime
# class Employee:
#     num_of_emps = 0
#     raise_amount = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last 
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay

#         Employee.num_of_emps += 1

#     @property
#     def full_name(self):
#         return f'{self.first} {self.last}'

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)


#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amount = amount 

#     @staticmethod # it will not take wheather instance or class variable
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         else:
#             return True


# # print(Employee.num_of_emps)
# emp1 = Employee('Sador', 'Zewge', 5000)
# # print(Employee.num_of_emps)
# emp2 = Employee('Miki', 'Men', 10000)
# # print(Employee.num_of_emps)
# # print(emp1.full_name())
# # print(emp1.full_name)
# # print(Employee.raise_amount)
# # print(emp1.pay)
# # emp1.apply_raise()
# # print(emp1.pay)
# # Employee.set_raise_amt(1.05) # this class method will change the class variable
# # emp1.set_raise_amt(1.05) # calling class method from object is also changes to another object like emp1 changes emp2
# # print(Employee.raise_amount)
# # print(emp1.raise_amount)
# # print(emp2.raise_amount)

# my_date = datetime.date(2021,8,16)
# print(emp1.is_workday(my_date))

# Example 2
# ==========>

# class MyClass:
#     # instance method can modify object instance state and can modify class state
#     def instance_method(self):
#         print('instance method called', self)
    
#     @classmethod
#     # class method can't modify object instance state but can modify class state
#     def class_method(cls):
#         print('class method called', cls)
    
#     @staticmethod
#     # static method can't modify object instance state  and class state
#     def static_method():
#         print('static method called')


# my_class = MyClass()
# # we can call methods from instance
# # print(my_class.instance_method()) # we can see the instance location here
# # print(my_class.class_method()) # here we can see the class it self
# # print(my_class.static_method()) # nothing except returning value


# MyClass.class_method() # it will work
# MyClass.static_method() # it will work
# MyClass.instance_method() # throw an error TypeError


# Example 3
import math
class Pizza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    @classmethod
    def margherita(cls):
        return cls(['cheese', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['cheese', 'tomatoes','ham', 'mushrooms' ])

    def area(self):
        return self._circle_area(self.radius)
    
    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi

# print(Pizza.margherita())
# print(Pizza.prosciutto())
# p1 = Pizza(4, ['cheese', 'mushrooms'])
# print(p1.area())
print(Pizza)
print(Pizza._circle_area(5))