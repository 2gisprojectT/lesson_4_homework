from unittest import TestCase
from main import Lion
import unittest


class LionTest(TestCase):
    def setUp(self):
        self.table = {("АНТИЛОПА", "ГОЛОДНЫЙ"): ("СЫТЫЙ", "Съесть"),
                      ("ОХОТНИК", "ГОЛОДНЫЙ"): ("ГОЛОДНЫЙ", "Убежать")}

    def test_constructor_positive(self):
        lion = Lion("ГолоднЫй", self.table)
        self.assertEqual("ГОЛОДНЫЙ", lion.state)

    def test_constructor_negative(self):
        state = "sds"
        regex = "Задаваемого состояния нет в таблице переходов: %s" % state
        self.assertRaisesRegex(ValueError, regex, Lion, state, self.table)

    def test_change_state(self):
        lion = Lion("Голодный", self.table)
        lion.input("АнтилОпа")
        self.assertEqual("СЫТЫЙ", lion.state)
        self.assertEqual("Съесть", lion.action)

    def test_save_state(self):
        lion = Lion("Голодный", self.table)
        lion.input("ОхотНик")
        self.assertEqual("ГОЛОДНЫЙ", lion.state)
        self.assertEqual("Убежать", lion.action)

    def test_wrong_input_symbol(self):
        lion = Lion("Сытый", self.table)
        symbol = "sds"
        regex = "Не верный входной символ: %s" % symbol
        self.assertRaisesRegex(ValueError, regex, lion.input, symbol)


if __name__ == '__main__':
    unittest.main()
