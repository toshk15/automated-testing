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
            temp = arr[i]
            j = i
            while j >= 0 and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            
            arr[j] = temp
        interval //= 2
    return arr
    


if __name__ == "__main__":

    arr = [10, 30, 3, 6, 1, 23]
    
    print(selectionSort(arr))
    print(shellSort(arr))

