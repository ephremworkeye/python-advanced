# UML
# Unified Modeling Language(UML) is a standardized way to view the design of system
# Often used to show class hierarchies in software projects
# planning a project lets us make crucial design choices before we start coding

# + and - denote public and private accessibility
    # python does not support formal access modifiers, so we mark every member as public
# A data type sometimes follows an attribute or method
    # type of attribute
    # return type of the method

# Expressing inheritance with UML
    # An arrow points from the child(derived) class to the parent(base) class 
    # We can write extends to make it clear this is inheritance
        # if a derived class extends a base class, that means it inherits from it

# Expressing composition with UML
    # a number indicates the number of component instances contained in the composite class
    # The * symbol indicates that the composite class can contain a variable number of component instances
    # A range indicates the composite class can contain a certain range of instances
        # (1..4) means between 1 and 4
        # (1..*) means at least one

# What is inerface 
    # Conceptually, an interface is description of the features and behaviours an object has
        # The set of attributes and methods that make up class
        # Not the implementation of the method,  jst the decalration
    # Some OOP languages have actual mechanisms called interfaces.Python does not have (or need) this
    # python supports multiple inheritance so we do need interface explicitly 

# Liskov Substituition Principle
    # Any where our program expects a base class object, we can give it an derived class
    # becuase derived class is base class
    # it inherits the interface of its parent, sot it has the same capabilities that out program expects

# intefaces in UML
    # <<interface>> at the top
    # not a class! Just a listing of the members that confirming classes must have
    # Dashed arrow that says "implemnets"

# questions on interface in UML
    # What is Employee called?
        # Base class of SalaryEmployee and HourlyEmployee directly
    # What is SalaryEmployee called?
        # Child class of Employee and base class of CommissionEmployee
    # What interface does Emplyee expose?
        # id and name
    # What inteface does HourlyEmployee expose?
        # id, name, calculate_payroll()
    # Why might CommissionEmployee inherit from SalayEmployee?
        # CommissionEmployee might utilize the calculate_payroll method in salaryEmployee
        # and it will provide its own implemntation of that method that will automatically hide the implementaion of its parent
    # What is the difference between an interface and a class
        # An inreface is nothing more than a lsit fo memvers.These members can be attribures or methods
        # Any class that implements, or conforms to this interface must declare these members