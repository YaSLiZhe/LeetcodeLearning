def mergesort(arr, l, r):
    if l < r:
        m = l + (r - l)//2
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m, r)


def merge(arr, l, m, r):
    leng1 = m-l+1
    leng2 = r-m
    leftArr = [0]*(leng1)
    rightArr = [0]*(leng2)
    for i in range(0, leng1):
        leftArr[i] = arr[l + i]
    for j in range(0, leng2):
        rightArr[j] = arr[m + 1 + j]
    i, j, k = 0, 0, l
    while i < leng1 and j < leng2:
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1

    while i < leng1:
        arr[k] = leftArr[i]
        i += 1
        k += 1

    while j < leng2:
        arr[k] = rightArr[j]
        j += 1
        k += 1


if __name__ == '__main__':
    array = [10, 7, 8, 49, 1, 5]
    N = len(array)

    # Function call
    mergesort(array, 0, N - 1)
    print('Sorted array:')
    for x in array:
        print(x, end=" ")
