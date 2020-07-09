arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]


def linear_search(arr, target):
    # Your code here
    if len(arr) == 0:
        return -1

    for index, val in enumerate(arr):
        if val == target:
            return index
    return -1   # not found


print(linear_search(arr1, 6))
print(linear_search(arr1, -6))
print(linear_search(arr1, 0))
print(linear_search(arr1, 3))

# Write an iterative implementation of Binary Search

arr2 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]


def binary_search(arr, target):

    # Your code here
    first = 0
    last = len(arr) - 1
    found = 0

    while first <= last and not found:
        # Find middle
        middle = (first + last) // 2
        if arr[middle] == target:
            found = arr.index(target)
            return found
        else:
            if target < arr[middle]:
                # Search the lower half
                last = middle - 1
            else:
                # Search the upper half of array
                first = middle + 1

    return -1  # not found


print('*******')
print(binary_search(arr2, -8))
print(binary_search(arr2, 0))
print(binary_search(arr2, 6))
print(binary_search(arr2, 0))
