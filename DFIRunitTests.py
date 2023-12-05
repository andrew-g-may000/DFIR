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
    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.size(), 3)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        item = stack.pop()
        self.assertEqual(item, 3)
        self.assertEqual(stack.size(), 2)

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.size(), 3)

    def test_top(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        top = stack.top()
        self.assertEqual(top, 3)
        self.assertEqual(stack.size(), 3)

    def test_print_stack_up(self):
        stack = Stack()
        stack.push("a")
        stack.push("b")
        stack.push("c")
        stack_string = stack.print_stack_up()
        self.assertEqual(stack_string, "a\nb\nc\n")


# Unit tests for HashTable data structure
class HashTableTests(unittest.TestCase):
    hash_table = HashTable()
    hash_table.set_value(3, "apple")
    hash_table.set_value(9, "cherry")
    hash_table.set_value(6, "banana")

    def test_set_value(self):
        self.assertEqual(self.hash_table.get_value(3), "apple")
        self.assertEqual(self.hash_table.get_value(9), "cherry")
        self.assertEqual(self.hash_table.get_value(6), "banana")

    def test_get_value(self):
        self.assertEqual(self.hash_table.get_value(3), "apple")
        self.assertEqual(self.hash_table.get_value(6), "banana")
        self.assertEqual(self.hash_table.get_value(13), "No record found")
        self.assertEqual(self.hash_table.get_value(15), "No record found")

    def test_print_hash_table(self):
        self.assertEqual(self.hash_table.print_hash_table(), "3: apple\n9: cherry\n6: banana")

    def test_insertion_sort(self):
        sort_this_table = HashTable()
        sort_this_table.set_value(1, "Ace")
        sort_this_table.set_value(3, "Queen")
        sort_this_table.set_value(2, "King")
        sort_this_table.set_value(4, "Jack")
        sort_this_table.insertion_sort()
        self.assertEqual(sort_this_table.print_hash_table(), "1: Ace\n2: King\n3: Queen\n4: Jack")


if __name__ == "main":
    unittest.main()
