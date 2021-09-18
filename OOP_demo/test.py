class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def full_name(self):
        print(self.fname + self.lname)


class Student(Person):
    def __init__(self, fname, lname, courses, grades):
        super.__init__(self, fname, lname)
        self.courses = courses
        self.grade = grade


    def courses_taken(self):
        for course in self.courses:
            print(course)


p = Person('sador', 'ephrem')
s = Student()
        

