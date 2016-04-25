from unittest import TestCase
from main import Lion
import unittest


class LionTest(TestCase):
    def setUp(self):
        self.table = {"Голодный": {"Антилопа": ("Сытый", "Съесть")}}

    def test_constructor_positive(self):
        lion = Lion("Голодный", self.table)
        self.assertEqual("Голодный", lion.state)
        self.assertIsNone(lion.action)

    def test_constructor_negative(self):
        state = "Дерево"
        regex = "Задаваемого состояния нет в таблице переходов: %s" % state
        self.assertRaisesRegex(ValueError, regex, Lion, state, self.table)

    def test_change_state(self):
        lion = Lion("Голодный", self.table)
        lion.input("Антилопа")
        self.assertEqual("Сытый", lion.state)
        self.assertEqual("Съесть", lion.action)

    def test_wrong_input_symbol(self):
        lion = Lion("Голодный", self.table)
        symbol = "Дерево"
        regex = "Не верный входной символ: %s" % symbol
        self.assertRaisesRegex(ValueError, regex, lion.input, symbol)


if __name__ == '__main__':
    unittest.main()
