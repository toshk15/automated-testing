def bubbleSort(arr):

    n = len(arr)
    flag = True

    for i in range(n):
        flag = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if flag == False:
            break
            
    return arr


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


def insertSort(arr):

    for i in range(1, len(arr)):
        j = i - 1
        aux = arr[i]

        while j >= 0 and aux < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = aux

    return arr

def mergeSort(arr):
    if len(arr) > 1:        
    
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1            
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            arr[k] = right[j]  
            j+=1
            k+=1

    return arr    


if __name__ == "__main__":
    pass
    


