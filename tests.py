from unittest import TestCase
from Lion import Lion
import unittest


class LionTest(TestCase):
    def test_state(self):
        self.assertRaises(ValueError, Lion, "голлоддный")

    def test_fed_antelope(self):
        lion = Lion("Сытый")
        lion.input_object("антилопа")
        self.assertEqual("голодный", lion.state, 'wrong state')
        self.assertEqual("спать", lion.action, 'wrong action')

    def test_hungry_antelope(self):
        lion = Lion("гОлодный")
        lion.input_object("антилопа")
        self.assertEqual("сытый", lion.state, 'wrong state')
        self.assertEqual("съесть", lion.action, 'wrong action')

    def test_fed_hunter(self):
        lion = Lion("сытый")
        lion.input_object("охотник")
        self.assertEqual("голодный", lion.state, 'wrong state')
        self.assertEqual("убежать", lion.action, 'wrong action')

    def test_hungry_hunter(self):
        lion = Lion("голодный")
        lion.input_object("охотник")
        self.assertEqual("голодный", lion.state, 'wrong state')
        self.assertEqual("убежать", lion.action, 'wrong action')

    def test_hungry_tree(self):
        lion = Lion("голодный")
        lion.input_object("дерево")
        self.assertEqual("голодный", lion.state, 'wrong state')
        self.assertEqual("спать", lion.action, 'wrong action')

    def test_fed_tree(self):
        lion = Lion("сытый")
        lion.input_object("дерево")
        self.assertEqual("голодный", lion.state, 'wrong state')
        self.assertEqual("смотреть", lion.action, 'wrong action')

    def test_fed_false_object(self):
        lion = Lion("сытый")
        self.assertRaises(ValueError, lion.input_object, "павпвы")

    def test_hungry_false_object(self):
        lion = Lion("голодный")
        self.assertRaises(ValueError, lion.input_object, "hdghdjs")


if __name__ == '__main__':
    unittest.main()
