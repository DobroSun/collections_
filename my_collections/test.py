#!/usr/bin/python3

import unittest
from binarytree import BinaryTree


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
   
if __name__ == "__main__":
    unittest.main()

