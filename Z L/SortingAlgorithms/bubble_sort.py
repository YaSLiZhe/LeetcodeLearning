def bubble_sort(arr):
    n = len(arr)
    # The outer loop controls how many times to pass through the list. Since each pass places one element in its correct position, the range is typically range(n-1).
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
    print(arr)
    return arr


bubble_sort([2, 4, 4, 5, 6, 21, 1, 3])
