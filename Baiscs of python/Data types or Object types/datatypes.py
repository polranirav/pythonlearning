# [],(),{} brackets for list, peranthesis for tuple, curly braces for dictionary
# number 1234, 3.14, 10, 10.0, 10 + 5j, -10, -10.0, -10 + 5j, 0, 0.0, 0 + 0j, -0, -0.0, -0 + 0j, decimal(), fraction()
student_number = 20
print(student_number)

# string = "hello world", 'spam', "bob's", b'a\x00c'
name = "nirav polara"
print(name)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1,'number', 3.14, True, None,[1,'number', 3.14, True, None]]
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_of_numbers)
print(list_of_numbers[0])  # Accessing the first element of the list

# tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1,'number', 3.14, True, None,[1,'number', 3.14, True, None])
tuple_of_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_of_numbers)
print(tuple_of_numbers[0])  # Accessing the first element of the tuple

# dictionary = {'name': 'nirav', 'age': 20, 'is_student': True, 'marks': [1, 2, 3, 4, 5], 'address': {'city': 'surat', 'state': 'gujarat'}}
dictionary = {'name': 'nirav', 'age': 20, 'is_student': True, 'marks': [1, 2, 3, 4, 5], 'address': {'city': 'surat', 'state': 'gujarat'}}
print(dictionary)
print(dictionary['name'])  # Accessing the value associated with the key 'name'


# file = open('file.txt', 'r'), open('file.txt', 'w'), open('file.txt', 'a'), open('file.txt', 'x')


# bool = True, False, None

# function = def func(): pass, lambda x: x + 1

# module = import os, import sys, from math import sqrt, from datetime import datetime
# class = class MyClass: pass, class MyClass(object): pass, class MyClass(int): pass
# exception = try: pass except Exception as e: pass, raise Exception('error'), assert condition, finally: pass

# advanced =
#   - generator: (x for x in range(10)), (yield from range(10)), (yield x for x in range(10))
#   - coroutine: async def my_coroutine(): pass, await my_coroutine(), async for x in my_coroutine()
#   - context manager: with open('file.txt', 'r') as f: pass, with
#   - decorator: @my_decorator def my_function(): pass, @classmethod def my_class_method(cls): pass, @staticmethod def my_static_method(): pass
#   -iterator: iter([1, 2, 3]), next(iter([1, 2, 3])), (x for x in range(10))
#   - slice: my_list[1:5], my_list[::2], my_list[-1]
