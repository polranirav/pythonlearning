# inheritance  in python means use property of parent class

class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def bark(self):
        print("Dog barking")

streetdog = Dog()
streetdog.speak()
streetdog.bark()

print(" multilevel inheritance.")
class Car:
    def modal(self):
        print("premium modal cars")

class Tire:
    def smoothdriveexperience(self):
        print("smoothdrive experience")

#The child class Dog inherits the base class Animal
class TataCar(Car):
    def evcar(self):
        print("electric car")

class nexon(TataCar):
    def middlerangecar(self):
        print("it run's upto 300km per single charge")

class TataSafari(TataCar, Tire):
    def highspeedcar(self):
        print("high speed car")

bestevcar = nexon()
bestevcar.middlerangecar()
bestevcar.evcar()
bestevcar.modal()

print("-----two base class------")

scar = TataSafari()
scar.highspeedcar()
scar.smoothdriveexperience()
scar.modal()
scar.evcar()

besttire = Tire()


# The issubclass(sub,sup) method to check relationship between two classes
print(issubclass(Car, Tire))
print(issubclass(TataCar, Car))

# The isinstance (obj, class) method check relationship between object and class
print(isinstance(bestevcar, Car))
print(isinstance(besttire, Car))
