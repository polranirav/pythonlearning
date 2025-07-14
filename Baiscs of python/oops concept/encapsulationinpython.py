# It refers to class as collections of data (variables) and methods that operate on that data.
# Public :-  self.var
# Protected :-  self._var
# Private :- self.__var


class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute
        self._automation = 'automation programming'
        self.__selfdriving = 'selfdriving'

    def display(self):
        print(f"Car: {self.brand} {self.model} {self._automation}")
        print(f"Car: {self.__selfdriving}")
    # Creating an object
class Tata(Car):
        def display(self):
            print("Tata")

car = Car("Toyota", "Corolla")

# Accessing public members
print(car.brand)
print(car.model)
# print(car.__selfdriving)
car.display()

car1 = Tata("tata","safari")
car1.display()
print(car1._automation)
# Calling public

