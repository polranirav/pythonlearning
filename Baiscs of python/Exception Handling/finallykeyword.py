# The basic role of the finally block is to ensure that specific code statements execute

# The code in the finally block executes whether or not a special case was raised or caught.

try:
    k = 5//0      # here, an exception raises i.e., divide by zero exception.
    print(k)
# Here, we are going to handles zero division exception
except ZeroDivisionError:     # here, we are declaring the except block
    print("Can't divide by zero")      # here, we are printing the exception raised
finally:      # here, we are declaring the finally block
    # Here, the finally block will always executed regardless of exception generation.
    print('This block is always executed')