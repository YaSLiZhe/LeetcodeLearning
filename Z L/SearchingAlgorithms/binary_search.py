def binary_search(arr, target):
    n = len(arr)
    left, right = 0, n-1
    while left <= right:
        middle = left + (right - left)//2
        if target > arr[middle]:
            left = middle + 1
        elif target < arr[middle]:
            right = middle - 1
        else:
            return middle
    return -1


test_arr = [2, 4, 6, 7, 9, 11, 12]
print('The target index is', binary_search(test_arr, 6))
