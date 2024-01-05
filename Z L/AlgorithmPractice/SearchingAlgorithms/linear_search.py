def linear_search(arr, target):
    n = len(arr)
    for i in range(n):
        if target == arr[i]:
            return i

    return -1


arr = [1, 2, 3, 4, 53, 2, 5, 34]
print("the target index is", linear_search(arr, 53))
