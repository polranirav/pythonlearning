# 1) bubble short : This arranging technique repeatedly checks the places of two contiguous things, trading them if vital.
print("-----------bubbleSort------------")
# 2) Selection Sort  : finds the minimal element repeatedly and arranges it in ascending order.
# Implementing the Bubble Sort Algorithm in Python 3
def bubbleSort(arr):
    n = len(arr)
    # For loop to iterate through all
    # components of an array
    for i in range(n):
        print("print iii",i)
        for j in range(0, n - i - 1):
            print("print j ",j)
            # The array's range is 0 to n-i-1.
            # If an element is discovered, swap the elements.
            # is larger than the element in front of it.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print("going into condition")
            # Driver code


# Example to test the above code
arr = [5,18,3,14]
bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])

# Selection Sort
print("------selectionSort--------")
# Selection Sort algorithm in Python
def selectionSort(array, size):
    for s in range(size):
        print("sort ",s)
        min_idx = s
        for i in range(s + 1, size):
            print("print the value of i", i)
            #for minimum element in each loop when sorting in descending order
            if array[i] < array[min_idx]:
                print("print the value of min index",min_idx)
                min_idx = i
                print("going into condition")
        # Placing min at the appropriate location
        (array[s], array[min_idx]) = (array[min_idx], array[s])
# Driver code
data = [ 9, 4, 3, 8]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order is :')
print(data)


# Insertion Sort
print("------insertionSort--------")
# A sub-array that is always sorted is maintained using this sorting method.
# Values from the array's unsorted portion are positioned correctly in the sorted portion
# The development of an insertion sort function
def insertion_sort(list1):
        # Len(list1) outer loop to traverse
        for i in range(1, len(list1)):
            a = list1[i]
            print("insert ",a)
            # List1[0 to i-1],
           # Bigger elements should be moved one position
           # forward of where they are now at.
            j = i - 1
            while j >= 0 and a < list1[j]:
                list1[j + 1] = list1[j]
                j -= 1
            list1[j + 1] = a
        return list1
# Driver code
list1 = [ 7, 2, 1, 6 ]
print("The unsorted list is:", list1)
print("The sorted new list is:", insertion_sort(list1))




