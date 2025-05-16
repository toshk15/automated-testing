def selectionSort(arr):
    for i in range(len(arr)):
        j, k = i, i
        for j in range(j, len(arr)):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]
    return arr


def shellSort(arr):
    interval = len(arr) // 2
    while interval > 0:
        for i in range(interval, len(arr)):
            temp = array[i]
            j = if
            while j >= 0 and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            
            array[j] = temp
        interval //= 2
    return array
    


if __name__ == "__main__":

    arr = [10, 30, 3, 6, 1, 23]
    
    print(selectionSort(arr))
    print(shellSort(arr))

