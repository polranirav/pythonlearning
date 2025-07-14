# program meets an error, it stops the execution of the rest of the program where we have to manage exception

# Python code after removing the syntax error
string = "Python Exceptions"

# for s in string:
#     if (s != o:
#         print( s )
# invalid syntax

# for s in string:
#     if (s != o):
#         print(s)
# NameError: name 'o' is not defined

# We can throw an exception at any line of code using the raise keyword.

# Using the assert keyword, we may check to see if a specific condition is fulfilled and raise an exception if it is not.

# All statements are carried out in the try clause until an exception is found.

# The try clause's exception(s) are detected and handled using the except function.

# If no exceptions are thrown in the try code block, we can write code to be executed in the else code block.


# Python Built-in Exceptions

# BaseException
class CustomException(BaseException):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

raise CustomException("This is a custom exception.")

# exception

class MyException(Exception):
    pass
try:
    raise MyException(" This is a custom exception. ")
except MyException as e:
    print(" A custom exception was raised : ", e)

# AttributeError
class MyClass:
    pass
obj = MyClass()
try:
    print(obj.non_existent_attribute)
except AttributeError as e:
    print(" An attribute error occurred : ", e)

# TypeError  : object of an incorrect type
try:
    result   = "10" + 10
except TypeError as e:
    print(" A type error occurred : ", e)

# ValueError : built-in method or functions has the correct type but the incorrect value
try:
    int("  a ")
except ValueError as e:
    print(" A value error occurred  : ", e)


# KeyError : dictionary is searched in Python with a key that really doesn't exist,
my_dict = {' a ': 1, ' b ': 2}

try:
    value = my_dict[' c ']
except KeyError as e:
    print(" A key error occurred : ", e)

# IndexError :  index is out of range.
# Python program for Index Error
my_list = [1, 2, 3]

try:
    value = my_list[3]
except IndexError as e:
    print(" An index error occurred : ", e)


# FileNotFoundError
try:
    with open(" myfile.txt ") as f:
        contents = f.read()
except FileNotFoundError as e:
    print(" A file not found error occurred : ", e)

# ImportError :  import statement fails

try:
    import nonexistent_module
except ImportError as e:
    print(" An import error occurred : ", e)

# ArithmeticError : Whenever an arithmetic operation (such dividing by zero or calculating the square root of a negative integer) fails

try:
    result = 1/0
except ArithmeticError as e:
    print(" An arithmetic error occurred : ", e)

# OverflowError : Whenever an arithmetic operation yields a result that is simply too big to be represented
try:
    result = 10 ** 100000
except OverflowError as e:
    print(" An overflow error occurred : ", e)

# SyntaxError : When the Python interpreter comes across a syntax issue in your code
x = 5
if x > 10:
    print(" x is greater than 10 ")

# AssertionError : Whenever an assert statement failures
# Python program for Assertion Error
x = 5
assert x > 10, " x is not greater than 10 "

# FloatingPointError : Whenever an operation involving floating-point integers yields an undefinable or pointless mathematical conclusion
x = float(' inf ')
y = x / x
print(y)

# EOFError : Whenever the end-of-file (EOF) marker is encountered and there is no further data to somehow be read
try:
    file = open(" example.txt ", " r ")
    for line in file:
        print(line)
    file.read()
except EOFError:
    print(" Reached end of file. ")
finally:
    file.close()

