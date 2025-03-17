import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from array_list import ArrayList

class TestArrayList(unittest.TestCase):

    def test_append(self):
        lst = ArrayList()
        lst.append("A")
        self.assertEqual(lst.get(0),"A")

    def test_insert(self):
        lst = ArrayList()
        lst.append("A")
        lst.insert("B", 1)
        self.assertEqual(lst.get(1),"B")

    def test_delete(self):
        lst = ArrayList()
        lst.append("A")
        self.assertEqual(lst.delete(0),"A")
        self.assertEqual(lst.length(), 0)

    def test_delete_all(self):
        lst = ArrayList()
        lst.append("A")
        lst.append("B")
        lst.append("A")
        lst.deleteAll("A")
        self.assertEqual(lst.length(), 1)
        self.assertEqual(lst.get(0), "B")

    def test_find_first(self):
        lst = ArrayList()
        lst.append("A")
        lst.append("B")
        lst.append("A")
        self.assertEqual(lst.findFirst("A"), 0)

    def test_find_last(self):
        lst = ArrayList()
        lst.append("A")
        lst.append("B")
        lst.append("A")
        self.assertEqual(lst.findLast("A"), 2)

    def test_reverse(self):
        lst = ArrayList()
        lst.append("A")
        lst.append("B")
        lst.reverse()
        self.assertEqual(lst.get(0), "B")
        self.assertEqual(lst.get(1), "A")

    def test_clone(self):
        lst = ArrayList()
        lst.append("A")
        newlst = lst.clone()
        self.assertEqual(newlst.get(0), "A")
        self.assertEqual(newlst.length(), 1)

    def test_clear(self):
        lst = ArrayList()
        lst.append("A")
        lst.clear()
        self.assertEqual(lst.length(), 0)

    def test_extend(self):
        lst1 = ArrayList()
        lst2 = ArrayList()
        lst1.append("A")
        lst2.append("B")
        lst1.extend(lst2)
        self.assertEqual(lst1.length(), 2)
        self.assertEqual(lst1.get(1), "B")

if __name__ == '__main__':
    unittest.main()
        