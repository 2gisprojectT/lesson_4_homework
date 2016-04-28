from Lion import Lion
from unittest import TestCase
import unittest


class LionUnittest(TestCase):
    def test_init(self):
        self.assertRaises(ValueError, Lion, "ошибочное значение")

        lion = Lion("сытый")
        self.assertEqual("сытый", lion.state)
        lion = Lion("голодный")
        self.assertEqual("голодный", lion.state)

    def test_act_full_antelope(self):
        lion = Lion("сытый")
        lion.act("антилопа")
        self.assertEqual("голодный", lion.state)
        self.assertEqual("спать", lion.action)

    def test_act_full_hunter(self):
        lion = Lion("сытый")
        lion.act("охотник")
        self.assertEqual("голодный", lion.state)
        self.assertEqual("убежать", lion.action)

    def test_act_full_tree(self):
        lion = Lion("сытый")
        lion.act("дерево")
        self.assertEqual("голодный", lion.state)
        self.assertEqual("смотреть", lion.action)

    def test_act_hungry_antelope(self):
        lion = Lion("голодный")
        lion.act("антилопа")
        self.assertEqual("сытый", lion.state)
        self.assertEqual("съесть", lion.action)

    def test_act_hungry_hunter(self):
        lion = Lion("голодный")
        lion.act("охотник")
        self.assertEqual("голодный", lion.state)
        self.assertEqual("убежать", lion.action)

    def test_act_hungry_tree(self):
        lion = Lion("голодный")
        lion.act("дерево")
        self.assertEqual("голодный", lion.state)
        self.assertEqual("спать", lion.action)


if __name__ == '__main__':
    unittest.main()
