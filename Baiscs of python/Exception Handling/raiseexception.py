# The raise statement in Python is used to raise an exception

# We can throw an exception and immediately halt the running of your programme by using the raise keyword.

# Python looks for the closest exception handler, which is often defined using a try-except block, when an exception is triggered.

# If an exception handler is discovered, its code is performed, and the try-except block's starting point is reached again.

# If an exception handler cannot be located, the software crashes and an error message appears.

# Python program to raise an exception
# divide function
def divide(a, b):
    if b == 0:
        raise Exception(" Cannot divide by zero. ")
    return a / b
try:
    result = divide(5, 0)
except Exception as e:
    print(" An error occurred: ", e)


# Python program to raise an exception
# check_age function checks the age
def check_age(age):
    if age < 18:
        raise Exception(" Age must be 18 or above. ")
    else:
        print(" Age is valid. ")
try:
    check_age(15)
except Exception as e:
    print(" An error occurred: ", e)
    