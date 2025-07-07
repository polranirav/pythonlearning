numberlist = '123456789'
print(numberlist[0:5])  # Output: '1 2 3 4 5'
print(numberlist[::2])  # Output: '13579'
print(numberlist[-1])   # Output: '0' (last character)
print(numberlist[1:5])  # Output: ' 2 3 4 5'
print(numberlist[1:5:2])  # Output: ' 24'
print(numberlist[1:5:-1])  # Output: '' (empty string, as the step is negative and the start index is less than the end index)
