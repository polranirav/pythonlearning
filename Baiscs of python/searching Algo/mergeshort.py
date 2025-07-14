# Here, we are declaring the function to divide the lists in to the two sub lists
# Here, we are passing the list1, left index, right index as the parameters
def merge_sort(list1, left_index, right_index):
    if left_index >= right_index:    # here, we are checking the if condition
        return
    print(left_index, right_index)
    middle = (left_index + right_index)//2
# Here, we are finding the middle of the given two numbers
    merge_sort(list1, left_index, middle)
# Here, we are calling the merge sort function till the middle number we got
    merge_sort(list1, middle + 1, right_index)
# Here, we are calling the merge sort function till the end of the list i.e., right index
    merge(list1, left_index, right_index, middle)
# Here, we are calling the merge function to merge the divided list using the merge   # sort function above
# Here, we are defining a function for merge the list after dividing
def merge(list1, left_index, right_index, middle):
   # Here, we are creating subparts of a lists
    left_sublist = list1[left_index:middle + 1]
    right_sublist = list1[middle+1:right_index+1]
    # Here, we are initializing the values for variables that we use to keep
    # track of where we are in each list1
    left_sublist_index = 0
    right_sublist_index = 0
    sorted_index = left_index
    # Here, we are traversing the both copies until we get run out one element
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):        # here, we are declaring a while loop
        # If our left_sublist has the smaller element, put it in the sorted
        # part and then move forward in left_sublist (by increasing the pointer)
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:
        # Here, we are checking the if condition, if it is true then we will enter the block
            list1[sorted_index] = left_sublist[left_sublist_index]
            left_sublist_index = left_sublist_index + 1
        # Otherwise add it into the right sublist
        else:
            list1[sorted_index] = right_sublist[right_sublist_index]
            right_sublist_index = right_sublist_index + 1
            # Here, we are moving forward in the sorted part
        sorted_index = sorted_index + 1
     # Here, we will go through the remaining elements and add them
    while left_sublist_index < len(left_sublist):  # here, we are declaring a while loop
        list1[sorted_index] = left_sublist[left_sublist_index]
        left_sublist_index = left_sublist_index + 1
        sorted_index = sorted_index + 1
    while right_sublist_index < len(right_sublist):# here, we are declaring a while loop
        list1[sorted_index] = right_sublist[right_sublist_index]
        right_sublist_index = right_sublist_index + 1
        sorted_index = sorted_index + 1
list1 = [44, 65, 2, 3, 58, 14, 57, 23, 10, 1, 7, 74, 48]
print("The given list before performing the merge sort is: ", list1)
# Here, this is the input unsorted array given by the user
merge_sort(list1, 0, len(list1) -1)
print("The given list after performing the merge sort is:", list1)
# here, we are printing the list1 after performing the merge sort amd the merge
# functions