#!/usr/bin/env python3

import unittest
from stack import Stack
from heap import Heap, heapsort
from queue import Queue



class TestStack(unittest.TestCase):
    def test_append(self):
        A = Stack()
        A.append(3)
        A.append(101)
        self.assertEqual(A.arr, [3, 101])

        A = Stack()
        with self.assertRaises(AssertionError):
            A.append('qwerty')
        
        A.append((3, {3:0}))
        self.assertEqual(A.arr, [(3, {3: 0})])

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

    def test_iter(self):
        A = Stack([1, 3, 7, 2])
        L = []
        for i in A:
            L.append(i)
        self.assertEqual(L, [1, 3, 7, 2])

    def test_reversed(self):
        A = Stack([3, 0, 7, 1])
        L = []
        for i in reversed(A):
            L.append(i)
        self.assertEqual(L, [1, 7, 0, 3])

    def test_len(self):
        A = Stack([3, 0, 2, 6])
        self.assertEqual(len(A), 4)

    def test_str(self):
        A = Stack([3, 2, 1, 0])
        self.assertEqual(str(A), '[3, 2, 1, 0]')

    def test_funcs(self):
        A = Stack([2, 4, 9, 0])
        self.assertEqual(min(A), 0)
        self.assertEqual(max(A), 9)
        self.assertEqual(sum(A), 15)




class TestQueue(unittest.TestCase):
    def test_iter(self):
        Q = Queue([3, 9, 0 ,5])
        L = []
        for i in Q:
            L.append(i)
        self.assertEqual(L, [3, 9, 0, 5])

    def test_reversed(self):
        Q = Queue([3, 9, 0 ,5])
        L = []
        for i in reversed(Q):
            L.append(i)
        self.assertEqual(L, [5, 0, 9, 3])
        
    def test_len(self):
        Q = Queue((0, 7, 8, 9))
        self.assertEqual(len(Q), 4)

    def test_str(self):
        Q = Queue([3, 9, 0, 4])
        Q.append(2)
        self.assertEqual(str(Q), '[3, 9, 0, 4, 2]')

    def test_append(self):
        Q = Queue()

        Q.append(2)
        self.assertEqual(Q.first.value, 2)
        self.assertEqual(Q.last.value, 2)

        self.assertEqual(Q.first.prev, None)
        self.assertEqual(Q.last.next, None)
        self.assertEqual(str(Q), '[2]')

        Q.addleft(3)
        self.assertEqual(Q.first.value, 3)
        self.assertEqual(Q.last.value, 2)
        self.assertEqual(str(Q), '[3, 2]')

    def test_args(self):
        Q = Queue([3, 5], (2, ), {1: 3})
        self.assertEqual(str(Q), '[3, 5, 2, 1]')

    def test_pop(self):
        Q = Queue([2, 2, 3, 4, 8])
        self.assertEqual(Q.pop(), 8)

        self.assertEqual(Q.popleft(), 2)
        
        self.assertEqual(Q.pop(), 4)

        self.assertEqual(Q.pop_k(3), 3)
        self.assertEqual(Q.pop_k(10), None)

    def test_clear(self):
        Q = Queue([4, 2, 1])
        Q.clear()
        self.assertEqual(str(Q), '[]') 

        self.assertEqual(Q.pop(), None)

    def test_reverse(self):
        Q = Queue((2, 9, 0, 7, 5))
        Q.reverse()
        self.assertEqual(str(Q), '[5, 7, 0, 9, 2]')

    def test_sort(self):
        Q = Queue([3, 5, 2, 9])
        Q.sort()
        self.assertEqual(str(Q), '[2, 3, 5, 9]')

    def test_search(self):
        Q = Queue({3: 0, 2: 1, 6: 9})
        self.assertEqual(Q.search(2), True)
        self.assertEqual(Q.search(10), False)






if __name__ == "__main__":
    unittest.main()
