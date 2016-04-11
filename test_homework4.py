from unittest import TestCase
from homework4 import LionStates
import unittest


class LionStatesTest(TestCase):
    def test_args(self):
        self.assertRaises(ValueError, LionStates, "asds2gda")
        self.assertRaises(ValueError, LionStates, "блаблабла")

    def test_constructor_hungry(self):
        lion = LionStates("голодный")
        self.assertEqual("голодный", lion.state)

    def test_constructor_full(self):
        lion = LionStates("сытый")
        self.assertEqual("сытый", lion.state)

    def test_incorrect_symbol_full(self):
        lion = LionStates("сытый")
        self.assertRaises(ValueError, lion.implementation_fsm, "Leva")

    def test_incorrect_symbol_hungry(self):
        lion = LionStates("голодный")
        self.assertRaises(ValueError, lion.implementation_fsm, "Дом")

    def test_antelope_full(self):
        lion = LionStates("сытый")
        lion.implementation_fsm("антилопа")
        self.assertEqual("голодный", lion.state)
        self.assertEqual("спать", lion.action)

    def test_antelope_hungry(self):
        lion = LionStates("голодный")
        lion.implementation_fsm("антилопа")
        self.assertEqual("сытый", lion.state)
        self.assertEqual("съесть", lion.action)

    def test_hunter_full(self):
        lion = LionStates("сытый")
        lion.implementation_fsm("охотник")
        self.assertEqual("голодный", lion.state)
        self.assertEqual("убежать", lion.action)

    def test_hunter_hungry(self):
        lion = LionStates("голодный")
        lion.implementation_fsm("охотник")
        self.assertEqual("голодный", lion.state)
        self.assertEqual("убежать", lion.action)

    def test_tree_full(self):
        lion = LionStates("сытый")
        lion.implementation_fsm("дерево")
        self.assertEqual("голодный", lion.state)
        self.assertEqual("смотреть", lion.action)

    def test_tree_hungry(self):
        lion = LionStates("голодный")
        lion.implementation_fsm("дерево")
        self.assertEqual("голодный", lion.state)
        self.assertEqual("спать", lion.action)

if __name__ == '__main__':
    unittest.main()
