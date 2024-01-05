def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


test_arr = [22, 27, 16, 2, 18, 6, 2, 4]
selection_sort(test_arr)
print("Sorted array is:", test_arr)
