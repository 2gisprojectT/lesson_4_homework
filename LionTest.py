from Lion import Lion
from unittest import TestCase
import unittest


class LionUnittest(TestCase):
    def test_init(self):
        lion = Lion("СыТЫй")
        self.assertEqual("сытый", lion.state, "неверное состояние")

        lion = Lion("голодный")
        self.assertEqual("голодный", lion.state, "неверное состояние")

    def test_act(self):
        lion = Lion("сытый")
        lion.act("антилопа")
        self.assertEqual("голодный", lion.state, lion.err)
        self.assertEqual("спать", lion.action, lion.err)

        lion = Lion("голодный")
        lion.act("антилопа")
        self.assertEqual("сытый", lion.state, lion.err)
        self.assertEqual("съесть", lion.action, lion.err)

        lion = Lion("сытый")
        lion.act("охотник")
        self.assertEqual("голодный", lion.state, lion.err)
        self.assertEqual("убежать", lion.action, lion.err)

        lion = Lion("голодный")
        lion.act("охотник")
        self.assertEqual("голодный", lion.state, lion.err)
        self.assertEqual("убежать", lion.action, lion.err)

        lion = Lion("сытый")
        lion.act("дерево")
        self.assertEqual("голодный", lion.state, lion.err)
        self.assertEqual("смотреть", lion.action, lion.err)

        lion = Lion("голодный")
        lion.act("дерево")
        self.assertEqual("голодный", lion.state, lion.err)
        self.assertEqual("спать", lion.action, lion.err)


if __name__ == '__main__':
    unittest.main()
