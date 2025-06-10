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
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            
            arr[j] = temp
        interval //= 2
    return arr


def countSort(arr):
    
    cr = []    
    n = len(arr)
    maxval = max(arr)
    cr = [0] * (maxval + 1)

    for i in range(0, n):
        cr[arr[i]] += 1

    i, j = 0, 0
    while j < maxval + 1:
        if cr[j] > 0:
            arr[i] = j
            i+=1
            cr[j]-=1
        else:
            j+=1
    return arr


    


if __name__ == "__main__":
    pass
    


