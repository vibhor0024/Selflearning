import unittest

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

class TestHeapSort(unittest.TestCase):

    def test_empty_array(self):
        arr = []
        heapSort(arr)
        self.assertEqual(arr, [])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        heapSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        heapSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_random_array(self):
        arr = [4, 1, 7, 3, 9, 2]
        heapSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 7, 9])
    
    def test_allzero_array(self):
        arr = [0, 0, 0, 0, 0, 0]
        heapSort(arr)
        self.assertEqual(arr, [0, 0, 0, 0, 0, 0])
    
    def test_negnumbers_array(self):
        arr = [-6, -1, -4, -3, -2, -9]
        heapSort(arr)
        self.assertEqual(arr, [-9, -6, -4, -3, -2, -1])
    
    def test_duplicates_array(self):
        arr = [4, 4, 2, 2, 8, 8]
        heapSort(arr)
        self.assertEqual(arr, [2, 2, 4, 4, 8, 8])

if __name__ == '__main__':
    unittest.main(verbosity=2)
