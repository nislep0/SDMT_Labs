import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from linked_list import DoubleLinkedList

class TestDoubleLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.list = DoubleLinkedList()

    def testAppend(self):
        self.list.append("A")
        self.list.append("B")
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(0),"A")
        self.assertEqual(self.list.get(1),"B")

    def testInsert(self):
        self.list.append("A")
        self.list.append("C")
        self.list.insert("B", 1)
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list.get(1),"B")
        with self.assertRaises(IndexError):
            self.list.insert("X", 5)

    def testDelete(self):
        self.list.append("A")
        self.list.append("B")
        self.list.append("C")

        self.assertEqual(self.list.delete(1),"B")
        self.assertEqual(self.list.length(), 2)

    def testDeleteAll(self):
        self.list.append("A")
        self.list.append("B")
        self.list.append("A")
        self.list.deleteAll("A")
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0),"B")

    def testFind(self):
        self.list.append("A")
        self.list.append("B")
        self.list.append("A")
        self.assertEqual(self.list.findFirst("A"), 0)
        self.assertEqual(self.list.findLast("A"), 2)
        self.assertEqual(self.list.findFirst("D"), -1)

    def testReverse(self):
        self.list.append("A")
        self.list.append("B")
        self.list.append("C")
        self.list.reverse()
        self.assertEqual(self.list.get(0),"C")
        self.assertEqual(self.list.get(1),"B")
        self.assertEqual(self.list.get(2),"A")

    def testClone(self):
        self.list.append("A")
        self.list.append("B")
        new_list = self.list.clone()
        self.assertEqual(new_list.length(), 2)
        self.assertEqual(new_list.get(0), "A")
        self.assertEqual(new_list.get(1), "B")

    def testExtend(self):
        self.list.append("A")
        self.list.append("B")
        new_list = DoubleLinkedList()
        new_list.append("C")
        new_list.append("D")
        self.list.extend(new_list)
        self.assertEqual(self.list.length(), 4)
        self.assertEqual(self.list.get(2), "C")
        self.assertEqual(self.list.get(3), "D")

    def testClear(self):
        self.list.append("A")
        self.list.append("B")
        self.list.clear()
        self.assertEqual(self.list.length(), 0)

if __name__ == "__main__":
    unittest.main()