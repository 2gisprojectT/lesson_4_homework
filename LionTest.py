from Lion import Lion
from unittest import TestCase
import unittest


class LionUnittest(TestCase):
    def test_init(self):
        self.assertRaises(ValueError, Lion, "не сытый")
        self.assertRaises(ValueError, Lion, "не очень голодный")

        lion = Lion("сытый")
        self.assertEqual("сытый", lion.state, ValueError)
        lion = Lion("голодный")
        self.assertEqual("голодный", lion.state, ValueError)

    def test_act(self):
        lion = Lion("сытый")
        lion.act("антилопа")
        self.assertEqual("голодный", lion.state, ValueError)
        self.assertEqual("спать", lion.action, ValueError)

        lion = Lion("сытый")
        lion.act("охотник")
        self.assertEqual("голодный", lion.state, ValueError)
        self.assertEqual("убежать", lion.action, ValueError)

        lion = Lion("сытый")
        lion.act("дерево")
        self.assertEqual("голодный", lion.state, ValueError)
        self.assertEqual("смотреть", lion.action, ValueError)

        lion = Lion("голодный")
        lion.act("антилопа")
        self.assertEqual("сытый", lion.state, ValueError)
        self.assertEqual("съесть", lion.action, ValueError)

        lion = Lion("голодный")
        lion.act("охотник")
        self.assertEqual("голодный", lion.state, ValueError)
        self.assertEqual("убежать", lion.action, ValueError)

        lion = Lion("голодный")
        lion.act("дерево")
        self.assertEqual("голодный", lion.state, ValueError)
        self.assertEqual("спать", lion.action, ValueError)


if __name__ == '__main__':
    unittest.main()
