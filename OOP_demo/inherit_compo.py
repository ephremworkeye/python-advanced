# Inheritance and compostion
# Inheritance : what common attributes and behaviours exist between real world objects
# compostion : How are objects in the real world composed(made up) of one another

# Modeling Classes in Python
    # Large Python projects often have many classes
    # These classes are often related in some way
        # One class might be very similar to another with a few small modifications

# What is inheritance?
    # Inheritance models is a relationship

# every class is inherited from object implicitly
# o = object()
# print(dict(o))


class Employee:
    def __init__(self, name, age, id, wage):
        self.name = name
        self.age = age
        self.id = id
        self.wage = wage
    
    def clock_in(self):
        pass

    def work(self):
        pass

    def clock_out(self):
        pass

    def report_info():
        pass

class Waitress(Employee):
    def __init__(self, shifts, tips_total):
        super().__init__(shifts, tips_total):
            self.shifts = shifts
            self.tips_total = tips_total

    def take_break(self):
        pass

    def work(self):
        pass


class Cashier(Employee):
    customer_served

    def work(self):
        pass



