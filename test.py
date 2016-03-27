from mainLion import Lion
from unittest import TestCase
import unittest

class LionTest (TestCase) :
    def test_init (self) :
        res = Lion(1, "hunter")
        self.assertEqual(0, res.state, "wrong")
        self.assertEqual("run", res.action, "wrong")

        res = Lion(1, "antelope")
        self.assertEqual(0, res.state, "wrong")
        self.assertEqual("sleep", res.action, "wrong")

        res = Lion(1, "tree")
        self.assertEqual(0, res.state, "wrong")
        self.assertEqual("look", res.action, "wrong")

        res = Lion(1, "rabbit")
        self.assertEqual(1, res.state, "wrong")
        self.assertEqual("error", res.action, "wrong")

        res = Lion(0, "hunter")
        self.assertEqual(0, res.state, "wrong")
        self.assertEqual("run", res.action, "wrong")

        res = Lion(0, "antelope")
        self.assertEqual(1, res.state, "wrong")
        self.assertEqual("eat", res.action, "wrong")

        res = Lion(0, "tree")
        self.assertEqual(0, res.state, "wrong")
        self.assertEqual("sleep", res.action, "wrong")

        res = Lion(0, "rabbit")
        self.assertEqual(0, res.state, "wrong")
        self.assertEqual("error", res.action, "wrong")

    if __name__ == '__main__' :
        unittest.main()