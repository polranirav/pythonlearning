try:
    first_input = input("Enter first number ")
    second_input = input("Enter second number ")

    # Attempt to convert user inputs to float
    first = float(first_input)
    second = float(second_input)


    result = first / second
    print(f"{first} divided by {second} is {result}")

except ValueError:
    print("Please enter valid numbers")
except ZeroDivisionError:
    print("You can't divide by zero")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Print the counts of each type of exception raised
    print(f"ZeroDivisionError occurred times.")
    print(f"FileNotFoundError occurred times.")