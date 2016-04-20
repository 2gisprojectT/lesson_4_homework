from unittest import TestCase
from object import Lion
import unittest


class TestLion(TestCase):
    def test_default(self):
        lion = Lion()
        self.assertEqual(lion.state, "сытый")
        self.assertEqual(lion.act, "спать")

    def test_full_antelope(self):
        lion = Lion("сытый")
        lion.work("антилопа")
        self.assertEqual(lion.state, "голодный")
        self.assertEqual(lion.act, "спать")

    def test_full_hunter(self):
        lion = Lion("сытый")
        lion.work("охотник")
        self.assertEqual(lion.state, "голодный")
        self.assertEqual(lion.act, "убежать")

    def test_full_tree(self):
        lion = Lion("сытый")
        lion.work("дерево")
        self.assertEqual(lion.state, "голодный")
        self.assertEqual(lion.act, "смотреть")

    def test_hungry_antelope(self):
        lion = Lion("голодный")
        lion.work("антилопа")
        self.assertEqual(lion.state, "сытый")
        self.assertEqual(lion.act, "съесть")

    def test_hungry_hunter(self):
        lion = Lion("голодный")
        lion.work("охотник")
        self.assertEqual(lion.state, "голодный")
        self.assertEqual(lion.act, "убежать")

    def test_hungry_tree(self):
        lion = Lion("голодный")
        lion.work("дерево")
        self.assertEqual(lion.state, "голодный")
        self.assertEqual(lion.act, "спать")

    def test_full_unknown(self):
        lion = Lion("сытый")
        lion.work("приветики")
        self.assertEqual(lion.state, "голодный")
        self.assertEqual(lion.act, "смотреть")

    def test_hungry_unknown(self):
        lion = Lion("голодный")
        lion.work("приветики")
        self.assertEqual(lion.state, "голодный")
        self.assertEqual(lion.act, "смотреть")

if __name__ == '__main__':
    unittest.main()