def selectionSort(arr):
    for i in range(len(arr)):
        j, k = i, i
        for j in range(j, len(arr)):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]
    return arr



if __name__ == "__main__":

    arr = [10, 30, 3, 6, 1, 23]
    
    print(selectionSort(arr))

