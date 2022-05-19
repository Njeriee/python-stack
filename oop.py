#    classes
class School:
    # initialising the class instance
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    # methods 
    # this method is available to all instance of the class school
    def show (self):
        print(self.name , self.level)

s1 = School('kenya high','high-school')
s1.show()

# inheritance
# here I am going to define a child class for school
class Student(School):
    def __init__(self, name, level ,fname, lname):
        # super() refers to the parent class
        super().__init__(name, level)
        self.fname = fname
        self.lname = lname
        self.fullname = self.fname + self.lname
    def show(self):
        print(f"Hi my name is  {self.fullname} and I go to {self.name } which is a {self.level} school")

stu1 = Student('Nairobi', 'junior sec','Kamau','John')
stu1.show()

# class attributes and methods
class Person:
    # this is a class attribute
    gravity = -9.8 
    def __init__(self,height,weight):
        self.weight = weight
        self.height = height
    # this is a class method
    @classmethod
    def grv(cls):
        print(cls.gravity)
    @staticmethod
    def bmi():
        bmi = (weight*height)/gravity
        return bmi

p1 = Person(18,65)
Person.grv()
Person.bmi()
