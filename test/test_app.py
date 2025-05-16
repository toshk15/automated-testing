from src.app import selectionSort, shellSort

def test_selectionSort_function():
    assert selectionSort([10, 30, 3, 6, 1, 23]) == [1, 3, 6, 10, 23, 30]

def test_shellSort_function():
    assert shellSort([10, 30, 3, 6, 1, 23]) == [1, 3, 6, 10, 23, 30]
 
 

