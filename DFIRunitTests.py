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
    hash_table.set_value("apple", "3")
    hash_table.set_value("banana", "6")
    hash_table.set_value("cherry", "9")

    def test_set_value(self):
        self.hash_table2 = HashTable()
        self.hash_table2.set_value("date", 12)
        self.assertIn("date", self.hash_table2.print_hash_table())

    def test_get_value(self):
        self.assertEqual(self.hash_table.get_value("mango"), "No record found")
        self.assertEqual(self.hash_table.get_value("grape"), "No record found")

    def test_insertion_sort(self):
        self.hash_table.insertion_sort()
        self.assertEqual(self.hash_table.print_hash_table(), "apple: 3\nbanana: 6\ncherry: 9")

    def test_print_hash_table(self):
        self.assertEqual(self.hash_table.print_hash_table(), "apple: 3\nbanana: 6\ncherry: 9")


if __name__ == "main":
    unittest.main()

