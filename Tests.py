from unittest import TestCase
from main import Lion
import unittest

class LionTest(TestCase):
    def test_constrcuctor_positive(self):
        lion=Lion("СыТый");
        self.assertEqual("СЫТЫЙ", lion.state, 'STATE have wrong value');

    def test_constrcuctor_negative(self):
        lion=Lion("sds");
        self.assertEqual("Неверный входной параметр",lion.err,"Error does not set");

    def test_wellfed_antilopa(self):
        lion=Lion("СыТый");
        lion.input("АнтилОпа");
        self.assertEqual("ГОЛОДНЫЙ", lion.state, 'STATE have wrong value');
        self.assertEqual("Спать", lion.action, 'ACTION have wrong value');

    def test_wellfed_hunter(self):
        lion=Lion("СыТый");
        lion.input("ОхотНик");
        self.assertEqual("ГОЛОДНЫЙ", lion.state, 'STATE have wrong value');
        self.assertEqual("Убежать", lion.action, 'ACTION have wrong value');

    def test_wellfed_tree(self):
        lion=Lion("СыТый");
        lion.input("ДеРевО");
        self.assertEqual("ГОЛОДНЫЙ", lion.state, 'STATE have wrong value');
        self.assertEqual("Смотреть", lion.action, 'ACTION have wrong value');

    def test_hungry_antilopa(self):
        lion=Lion("ГолоДныЙ");
        lion.input("АнтилОпа");
        self.assertEqual("СЫТЫЙ", lion.state, 'STATE have wrong value');
        self.assertEqual("Съесть", lion.action, 'ACTION have wrong value');

    def test_hungry_hunter(self):
        lion=Lion("ГолоДныЙ");
        lion.input("ОхотНик");
        self.assertEqual("ГОЛОДНЫЙ", lion.state, 'STATE have wrong value');
        self.assertEqual("Убежать", lion.action, 'ACTION have wrong value');

    def test_hungry_tree(self):
        lion=Lion("ГолоДныЙ");
        lion.input("ДеРевО");
        self.assertEqual("ГОЛОДНЫЙ", lion.state, 'STATE have wrong value');
        self.assertEqual("Спать", lion.action, 'ACTION have wrong value');

    def test_negative_hunry(self):
        lion=Lion("ГолоДныЙ");
        lion.input("Чтото");
        self.assertEqual("ГОЛОДНЫЙ", lion.state, 'STATE have wrong value');
        self.assertEqual("Неверный символ", lion.err, 'Error does not set');

    def test_negative_wellfed(self):
        lion=Lion("Сытый");
        lion.input("Чтото");
        self.assertEqual("СЫТЫЙ", lion.state, 'STATE have wrong value');
        self.assertEqual("Неверный символ", lion.err, 'Error does not set');


if __name__ == '__main__':
    unittest.main();