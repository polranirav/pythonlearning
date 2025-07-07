# list = [1, 2, 3, 4, 5]
# print(list) # Output: [10, 2, 3, 4, 5]
# print(list[0])
# list[0] = 10
# print(list[0]) # This will not raise an error because lists are mutable in Python
# print(list) # Output: [10, 2, 3, 4, 5]


mylistone = [1, 2, 3, 4, 5]
mylisttwo = mylistone  # mylisttwo is a reference to the same list as mylistone
print(mylistone)  # Output: [1, 2, 3, 4, 5]
print(mylisttwo)  # Output: [1, 2
mylistone = 'nirav polara'  # Now mylistone is a string, not a list
print(mylistone)  # Output: 'nirav polara'
mylistone = [1, 2, 3, 4, 5]  # Reassigning mylistone to a new list
print(mylistone)  # Output: [1, 2, 3, 4, 5]
mylistone[0] = 10  # Changing the first element of mylistone
print(mylistone)  # Output: [10, 2, 3,
print(mylisttwo)  # Output: [1, 2, 3,


