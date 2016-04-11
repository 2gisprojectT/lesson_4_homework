from unittest import TestCase
from Lion import Lion
import unittest


class LionUnittest(TestCase):
    def test_init_full(self):
        lion = Lion("голодный")
        self.assertEqual("голодный", lion.state)

    def test_init_hungry(self):
        lion = Lion("сытый")
        self.assertEqual("сытый", lion.state)

    def test_init_negative(self):
        self.assertRaises(ValueError, Lion, "уставший")

    def test_transition_hungry_antelope(self):
        lion = Lion("голодный")
        lion.transition("антилопа")
        self.assertEqual("съесть", lion.action)
        self.assertEqual("сытый", lion.state)

    def test_transition_full_antelope(self):
        lion = Lion("сытый")
        lion.transition("антилопа")
        self.assertEqual("спать", lion.action)
        self.assertEqual("голодный", lion.state)

    def test_transition_hungry_hunter(self):
        lion = Lion("голодный")
        lion.transition("охотник")
        self.assertEqual("убежать", lion.action)
        self.assertEqual("голодный", lion.state)

    def test_transition_full_hunter(self):
        lion = Lion("сытый")
        lion.transition("охотник")
        self.assertEqual("убежать", lion.action)
        self.assertEqual("голодный", lion.state)

    def test_transition_hungry_tree(self):
        lion = Lion("голодный")
        lion.transition("дерево")
        self.assertEqual("спать", lion.action)
        self.assertEqual("голодный", lion.state)

    def test_transition_full_tree(self):
        lion = Lion("сытый")
        lion.transition("дерево")
        self.assertEqual("смотреть", lion.action)
        self.assertEqual("голодный", lion.state)

    def test_transition_hungry_negative(self):
        lion = Lion("голодный")
        self.assertRaises(ValueError, lion.transition, "НЛО")

    def test_transition_full_negative(self):
        lion = Lion("сытый")
        self.assertRaises(ValueError, lion.transition, "НЛО")


if __name__ == '__main__':
    unittest.main()
