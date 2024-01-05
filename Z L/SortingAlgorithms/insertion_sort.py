

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr


test_arr = [22, 27, 16, 2, 18, 6, 2, 4]
insertion_sort(test_arr)
print("Sorted array is:", test_arr)
