from unittest import TestCase
import unittest
from main import LionFSM


class LionTests(TestCase):
    def test_hungry_tree(self):
        lion = LionFSM("голодный")
        lion.input("дерево")
        self.assertEqual(lion.action, "спать")
        self.assertEqual(lion.state, "голодный")

    def test_hungry_antelope(self):
        lion = LionFSM("голодный")
        lion.input("антилопа")
        self.assertEqual(lion.action, "съесть")
        self.assertEqual(lion.state, "сытый")

    def test_hungry_hunter(self):
        lion = LionFSM("голодный")
        lion.input("охотник")
        self.assertEqual(lion.action, "убежать")
        self.assertEqual(lion.state, "голодный")

    def test_full_tree(self):
        lion = LionFSM("сытый")
        lion.input("дерево")
        self.assertEqual(lion.action, "смотреть")
        self.assertEqual(lion.state, "голодный")

    def test_full_antelope(self):
        lion = LionFSM("сытый")
        lion.input("антилопа")
        self.assertEqual(lion.action, "спать")
        self.assertEqual(lion.state, "голодный")

    def test_full_hunter(self):
        lion = LionFSM("сытый")
        lion.input("охотник")
        self.assertEqual(lion.action, "убежать")
        self.assertEqual(lion.state, "голодный")

if __name__ == '__main__':
    unittest.main()
