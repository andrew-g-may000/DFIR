"""
***************************************************************
* Name: DFIR DSA Unit Tests
* Author: Andrew May
* Created: 11/23/2023
* Course: CIS 152 - Data Structures
* Version: 1.0.0
* OS: macOS Ventura 13.4
* IDE: VSCode - Version: 1.83.1 (Universal)
* Copyright: This is my own original work
* based on specifications issued by our instructor
* Description: This program performs 10 unit tests on the two
* data structure classes (Stack, HashTable), and insertion sort
* method contained with the main DFIR.py file.
* Input: N/A
* Output: N/A
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""

from DFIR import *
import unittest


# Unit tests for Stack data structure
class StackTests(unittest.TestCase):
    # Testing the Stack class' push method
    def test_push(self):
        # Arrange
        stack = Stack()
        # Act
        stack.push(1)
        stack.push(2)
        stack.push(3)
        # Assert
        self.assertEqual(stack.size(), 3)

    # Testing the Stack class' pop method
    def test_pop(self):
        # Arrange
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        # Act
        item = stack.pop()
        # Assert
        self.assertEqual(item, 3)
        self.assertEqual(stack.size(), 2)

    # Testing the Stack class' is_empty method
    def test_is_empty(self):
        # Arrange
        stack = Stack()
        # Assert
        self.assertTrue(stack.is_empty())
        # Act
        stack.push(1)
        # Assert
        self.assertFalse(stack.is_empty())

    # Testing the Stack class' size method
    def test_size(self):
        # Arrange
        stack = Stack()
        # Assert
        self.assertEqual(stack.size(), 0)
        # Act
        stack.push(1)
        stack.push(2)
        stack.push(3)
        # Assert
        self.assertEqual(stack.size(), 3)

    # Testing the Stack class' top method
    def test_top(self):
        # Arrange
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        # Act
        top = stack.top()
        # Assert
        self.assertEqual(top, 3)
        self.assertEqual(stack.size(), 3)

    # Testing the Stack class' print_stack_up method
    def test_print_stack_up(self):
        # Arrange
        stack = Stack()
        stack.push("a")
        stack.push("b")
        stack.push("c")
        # Act
        stack_string = stack.print_stack_up()
        # Assert
        self.assertEqual(stack_string, "a\nb\nc\n")


# Unit tests for HashTable data structure
class HashTableTests(unittest.TestCase):

    # Testing the HashTable class' set_value method
    def test_set_value(self):
        # Arrange
        hash_table = HashTable()
        # Act
        hash_table.set_value(3, "apple")
        # Assert
        self.assertEqual(hash_table.get_value(3), "apple")
        
    # Testing the HashTable class' get_value method
    def test_get_value(self):
        # Arrange
        hash_table = HashTable()
        # Act
        hash_table.set_value(3, "apple")
        hash_table.set_value(6, "banana")
        # Assert
        self.assertEqual(hash_table.get_value(3), "apple")
        self.assertEqual(hash_table.get_value(6), "banana")
        self.assertEqual(hash_table.get_value(13), "No record found")
        self.assertEqual(hash_table.get_value(15), "No record found")

    # Testing the HashTable class' print_hash_table method
    def test_print_hash_table(self):
        # Arrange
        hash_table = HashTable()
        # Act
        hash_table.set_value(3, "apple")
        hash_table.set_value(9, "cherry")
        hash_table.set_value(6, "banana")
        # Assert
        self.assertEqual(hash_table.print_hash_table(), "3: apple\n9: cherry\n6: banana")

    # Testing the HashTable class' insertion_sort method
    def test_insertion_sort(self):
        # Arrange
        hash_table = HashTable()
        # Act
        hash_table.set_value(3, "apple")
        hash_table.set_value(9, "cherry")
        hash_table.set_value(6, "banana")
        hash_table.insertion_sort()
        # Assert
        self.assertEqual(hash_table.print_hash_table(), "3: apple\n6: banana\n9: cherry")


if __name__ == "main":
    unittest.main()
