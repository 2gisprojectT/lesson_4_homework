from unittest import TestCase
from main import Lion
import unittest


class LionTest(TestCase):
    def test_constructor_positive(self):
        lion = Lion("ГолоднЫй")
        self.assertEqual("ГОЛОДНЫЙ", lion.state)

    def test_constructor_negative(self):
        lion = Lion("sds")
        self.assertEqual("СЫТЫЙ", lion.state)

    def test_wellfed_antelope(self):
        lion = Lion("СыТый")
        lion.input("АнтилОпа")
        self.assertEqual("ГОЛОДНЫЙ", lion.state)
        self.assertEqual("Спать", lion.action)

    def test_wellfed_hunter(self):
        lion = Lion("СыТый")
        lion.input("ОхотНик")
        self.assertEqual("ГОЛОДНЫЙ", lion.state)
        self.assertEqual("Убежать", lion.action)

    def test_wellfed_tree(self):
        lion = Lion("СыТый")
        lion.input("ДеРевО")
        self.assertEqual("ГОЛОДНЫЙ", lion.state)
        self.assertEqual("Смотреть", lion.action)

    def test_hungry_antelope(self):
        lion = Lion("ГолоДныЙ")
        lion.input("АнтилОпа")
        self.assertEqual("СЫТЫЙ", lion.state)
        self.assertEqual("Съесть", lion.action)

    def test_hungry_hunter(self):
        lion = Lion("ГолоДныЙ")
        lion.input("ОхотНик")
        self.assertEqual("ГОЛОДНЫЙ", lion.state)
        self.assertEqual("Убежать", lion.action)

    def test_hungry_tree(self):
        lion = Lion("ГолоДныЙ")
        lion.input("ДеРевО")
        self.assertEqual("ГОЛОДНЫЙ", lion.state)
        self.assertEqual("Спать", lion.action)

    def test_negative_hungry(self):
        lion = Lion("ГолоДныЙ")
        self.assertEqual("Неверный символ", lion.input("Чтото"))
        self.assertEqual("ГОЛОДНЫЙ", lion.state)

    def test_negative_wellfed(self):
        lion = Lion("Сытый")
        self.assertEqual("Неверный символ", lion.input("Чтото"))
        self.assertEqual("СЫТЫЙ", lion.state)


if __name__ == '__main__':
    unittest.main()
