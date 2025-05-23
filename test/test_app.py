from src.app import selectionSort, shellSort

def test_selectionSort_function():
    assert selectionSort([10, 30, 3, 6, 1, 23]) == [1, 3, 6, 10, 23, 30]
    assert selectionSort([1, 18, 3, 9, 1, 3]) == [1, 1, 3, 3, 9, 18]
    assert selectionSort([22, 3, 12, 6, 2, 20]) == [2, 3, 6, 12, 20, 22]

def test_shellSort_function():
    assert shellSort([10, 30, 3, 6, 1, 23]) == [1, 3, 6, 10, 23, 30]
    assert selectionSort([1, 18, 3, 9, 1, 3]) == [1, 1, 3, 3, 9, 18]
    assert selectionSort([22, 3, 12, 6, 2, 20]) == [2, 3, 6, 12, 20, 22]
 
 

