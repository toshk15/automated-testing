from src.app import selectionSort, shellSort, countSort, insertSort, bubbleSort, mergeSort, quickSort

def test_selectionSort_function():
    assert selectionSort([10, 30, 3, 6, 1, 23]) == [1, 3, 6, 10, 23, 30]
    assert selectionSort([1, 18, 3, 9, 1, 3]) == [1, 1, 3, 3, 9, 18]
    assert selectionSort([22, 3, 12, 6, 2, 20]) == [2, 3, 6, 12, 20, 22]

def test_shellSort_function():
    assert shellSort([10, 30, 3, 6, 1, 23]) == [1, 3, 6, 10, 23, 30]
    assert shellSort([1, 18, 3, 9, 1, 3]) == [1, 1, 3, 3, 9, 18]
    assert shellSort([22, 3, 12, 6, 2, 20]) == [2, 3, 6, 12, 20, 22]

def test_countSort_function():
    assert countSort([10, 30, 3, 6, 1, 23]) == [1, 3, 6, 10, 23, 30]
    assert countSort([1, 18, 3, 9, 1, 3]) == [1, 1, 3, 3, 9, 18]
    assert countSort([22, 3, 12, 6, 2, 20]) == [2, 3, 6, 12, 20, 22]
 
def test_insertSort_function():
    assert insertSort([10, 30, 3, 6, 1, 23]) == [1, 3, 6, 10, 23, 30]
    assert insertSort([1, 18, 3, 9, 1, 3]) == [1, 1, 3, 3, 9, 18]
    assert insertSort([22, 3, 12, 6, 2, 20]) == [2, 3, 6, 12, 20, 22]

def test_bubbleSort_function():
    assert bubbleSort([10, 30, 3, 6, 1, 23]) == [1, 3, 6, 10, 23, 30]
    assert bubbleSort([1, 18, 3, 9, 1, 3]) == [1, 1, 3, 3, 9, 18]
    assert bubbleSort([22, 3, 12, 6, 2, 20]) == [2, 3, 6, 12, 20, 22]

def test_mergeSort_function():
    assert mergeSort([10, 30, 3, 6, 1, 23]) == [1, 3, 6, 10, 23, 30]
    assert mergeSort([1, 18, 3, 9, 1, 3]) == [1, 1, 3, 3, 9, 18]
    assert mergeSort([22, 3, 12, 6, 2, 20]) == [2, 3, 6, 12, 20, 22]

def test_quickeSort_function():
    assert quickSort([10, 30, 3, 6, 1, 23]) == [1, 3, 6, 10, 23, 30]
    assert quickSort([1, 18, 3, 9, 1, 3]) == [1, 1, 3, 3, 9, 18]
    assert quickSort([22, 3, 12, 6, 2, 20]) == [2, 3, 6, 12, 20, 22]
