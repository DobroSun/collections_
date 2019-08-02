#!/libs/env/bin/python3

import unittest
from stack import Stack
from heap import Heap, heapsort

class TestStack(unittest.TestCase):
    def test_append(self):
        A = Stack()
        A.append(3)
        A.append(101)
        self.assertEqual(A.arr, [3, 101])

        A = Stack()
        with self.assertRaises(AssertionError):
            A.append('qwerty')

    def test_pop(self):
        A = Stack()
        self.assertEqual(A.pop(), None)
        A.append(2)
        self.assertEqual(A.pop(), 2)

    def test_create_stack(self):
        A = Stack([1, 0, 3])
        self.assertEqual(A.arr, [1, 0, 3])
        A = Stack({1: 0, 2: 7}, (0, 9, 8), [2, 4])
        self.assertEqual(A.arr, [1, 2, 0, 9, 8, 2, 4])

    def test_max_min(self):
        A = Stack([1, 3, 5])
        self.assertEqual(A.max, 5)
        self.assertEqual(A.min, 1)

        A = Stack((1, ))
        self.assertEqual(A.max, 1)
        self.assertEqual(A.min, 1)
        
        A.pop()
        self.assertEqual(A.max, None)
        self.assertEqual(A.min, None)

        A = Stack((1, 2, 3, 4, 5))
        A.pop()
        self.assertEqual(A.max, 4)
        self.assertEqual(A.min, 1)

    def test_sort(self):
        A = Stack([1, 4, 9, 3])
        A.sort()
        self.assertEqual(A.arr, [1, 3, 4, 9])

    def test_clear(self):
        A = Stack([1, 4, 3, 7, 9])
        A.clear()
        self.assertEqual(A.arr, [])

class TestHashMap(unittest.TestCase):
    pass

"""
class TestHeap(unittest.TestCase):
    def test_add(self):
        heap = Heap()
        heap.add(5)
        heap.add(3)
        heap.add(7)

        heap.add(1)
        self.assertEqual(heap.arr, [7, 3, 5, 1])

    def test_pop(self):
        heap = Heap()
        heap.add(5)
        heap.add(3)
        heap.add(7)
        heap.add(1)
        self.assertEqual(heap.pop(), 7)

        self.assertEqual(heap.arr, [5, 3, 1])

    def test_heapsort(self):
        arr = [1, 5, 9, 3, 0, 2]
        sorted_arr = heapsort(arr)
        
        self.assertEqual(sorted_arr, [0, 1, 2, 3, 5, 9])
"""

if __name__ == "__main__":
    unittest.main()
