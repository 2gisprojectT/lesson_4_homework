from unittest import TestCase
from object import Lion
import unittest


class TestLion(TestCase):
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

    def test_unknown_input(self):
        lion = Lion("сытый")
        self.assertRaises(ValueError, lion.work, "приветики")

    def test_wrong_state(self):
        self.assertRaises(ValueError, Lion, "приветики")

    def test_empty_constructor(self):
        self.assertRaises(ValueError, Lion, None)

    def test_right_state(self):
        lion = Lion("сытый")
        self.assertEqual(lion.state, "сытый")
        lion = Lion("голодный")
        self.assertEqual(lion.state, "голодный")


if __name__ == '__main__':
    unittest.main()