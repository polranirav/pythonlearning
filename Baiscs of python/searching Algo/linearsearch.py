# Linear search is a method of finding elements within a list. It is also called a sequential search
# [1 ,3, 5, 4, 9, 7] search from 1 element to the last element one by one 1, 3, 5 then....


def linear_Search(list1, n, key):
    # Searching list1 sequentially
    for i in range(0, n):
        if (list1[i] == key):
            return i
    return -1

list1 = [1 ,3, 5, 4, 9, 7]
key = 7
n = len(list1)
print(n)
res = linear_Search(list1, n, key)
print(res)
if(res == -1):
    print("Element not found")
else:
    print("Element found at index: ", res)

