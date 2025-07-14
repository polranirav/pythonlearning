class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name
    # A constructor is a special type of method (function) which is used to initialize the instance members of the class.
    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


emp1 = Employee("John", 101)
emp2 = Employee("David", 102)

# accessing display() method to print employee 1 information

emp1.display()

# accessing display() method to print employee 2 information
emp2.display()


# def __init__(self):
#     print("This is non parametrized constructor")
#
#  def __init__(self, name):
#         print("This is parametrized constructor")


# the object of the class will always call the last constructor if the class has multiple constructors
class Student:
    def __init__(self):
        print("The First Constructor")

    def __init__(self):
        print("The second contructor")
st = Student()
