import random


def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i],  arr[j]
            i = i + 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, pi+1, high)
        quicksort(arr, low, pi-1)


if __name__ == '__main__':
    array = [10, 7, 8, 49, 1, 5]
    N = len(array)

    # Function call
    quicksort(array, 0, N - 1)
    print('Sorted array:')
    for x in array:
        print(x, end=" ")
