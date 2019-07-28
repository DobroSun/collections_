#!/usr/bin/python3

import unittest
from stack import Stack


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

"""
def create_tree():
    global tree
    tree = BinaryTree()
    tree.add(3, '3')
    tree.add(0, '0')
    tree.add(7, '7')
    tree.add(1, '1')
    tree.add(4, '4')
    tree.add(8, '8')
    tree.add(9, '9')
    tree.add(2, '2')

class TestBinaryTree(unittest.TestCase):
    
    def test_add_root(self):
        create_tree()
        self.assertEqual(tree.head.key, 3) 
    
    def test_adding(self):
        create_tree()
        self.assertEqual(tree.head.left.right.key, 1)
        self.assertEqual(tree.head.left.right.right.key, 2)
        self.assertEqual(tree.head.right.right.key, 8)
        self.assertEqual(tree.head.right.left.key, 4)

    def test_print(self):
        create_tree()
        self.assertEqual(tree.print_in_line(), [3, 0, 7, 1, 4, 8, 2, 9])
    
    def test_pop2(self):
        create_tree()
        tree.pop(2)
        self.assertEqual(tree.print_in_line(), [3, 0, 7, 1, 4, 8, 9])
        
    def test_pop0(self):
        create_tree()
        tree.pop(0)
        self.assertEqual(tree.print_in_line(), [3, 1, 7, 2, 4, 8, 9])
    
    def test_pop3(self):
        create_tree()
        tree.pop(3)
        self.assertEqual(tree.print_in_line(), [2, 0, 7, 1, 4, 8, 9])
    
    def test_pop7(self):
        create_tree()
        tree.pop(7)
        self.assertEqual(tree.print_in_line(), [3, 0, 4, 1, 8, 2, 9])
    
    def test_pop8(self):
        create_tree()
        tree.pop(8)
        self.assertEqual(tree.print_in_line(), [3, 0, 7, 1, 4, 9, 2])
                                    
    def test_pop9(self):
        create_tree()
        tree.pop(9)
        self.assertEqual(tree.print_in_line(), [3, 0, 7, 1, 4, 8, 2])

    def test_pop1(self):
        create_tree()
        tree.pop(1)
        self.assertEqual(tree.print_in_line(), [3, 0, 7, 2, 4, 8, 9])
 
    def test_pop4(self):
        create_tree()
        tree.pop(4)
        self.assertEqual(tree.print_in_line(), [3, 0, 7, 1, 8, 2, 9])
"""

if __name__ == "__main__":
    unittest.main()
