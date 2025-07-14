from functools import singledispatch, singledispatchmethod

# Traditional Method Overloading (Not Supported)
# one methods with the same name but different sets of arguments.(method ovreloading)


class Example:

    # show() method with single argument
    def show(self, a):
        print(f"Single argument: {a}")

    # show() method with two arguments
    def show(self, a, b):
        print(f"Two arguments: {a}, {b}")

# instantiating the class
obj = Example()

# calling the method
# obj.show(5) it doesn't matter last one method called...weather it's one or two arguments.
obj.show(5, 18)

# let's execute method overloading with different approach
# method 1 Default Parameter Values

class Simple_Calculators:

    def add(self, a, b=0, c=0):
        # here i have to set value 0 for b and c otherwise it couldn't perform
        return a + b + c

my_calculator = Simple_Calculators()

# calling the add() method
print(my_calculator.add(5))  # single argument
print(my_calculator.add(5, 10))  # two arguments
print(my_calculator.add(5, 10, 15))  # three arguments

# Method 2: Using *args

class Simple_Calculator:

    # defining a function to add numbers
    def add(self, *args):
        return sum(args)

my_calculatorss = Simple_Calculator()

# calling the add() method
print(my_calculatorss.add(6))  # single argument
print(my_calculatorss.add(6, 12))  # two arguments
print(my_calculatorss.add(6, 12, 18))  # three arguments
print(my_calculatorss.add(5,3,5,3,21)) # five arguments

# Method 3: Using @singledispatchmethod from functools

# creating a class
class Normal_Calculator:

  # defining a method to calculate sum of two numbers
  @singledispatchmethod
  def add(self, a, b):
    # raising error for unsupported data type
    raise NotImplementedError("Unsupported Data Type")

  # method overloading for variables of int data type
  @add.register(int)
  def _(self, a: int, b: int) -> int:
    return a + b
  # method overloading for variables of float data type
  @add.register(float)
  def _(self, a: float, b: float) -> float:
    return a + b

# creating an object
my_calculatorsss = Normal_Calculator()

# calling the add() method
print(my_calculatorsss.add(9, 14)) # only int variables
print(my_calculatorsss.add(3.72, 1.54))  # only float variables
try:
  print(my_calculatorsss.add("tpoint", "tech")) # trying to pass str
except NotImplementedError as e:
  print(e)


# Method 4 (Optional): Using @dispatch from multipledispatch
# @dispatch from multipledispatch is not a built-in Python feature.
# It comes from an external library and may not be ideal for performance-critical applications.

