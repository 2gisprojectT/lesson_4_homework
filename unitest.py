from Main import autoLion
import unittest

class Unit_tests_lion(unittest.TestCase):
    def test_hunter_hungry(self):
        a = autoLion("охотник", "голодный")
        a.check()
        self.assertEqual("убежать", a.action, "Ошибка, неверное действие")
        self.assertEqual("голодный", a.status, "Ошибка, неверный статус")

    def test_hunter_full(self):
        a = autoLion("охотник", "сытый")
        a.check()
        self.assertEqual("убежать", a.action, "Ошибка, неверное действие")
        self.assertEqual("голодный", a.status, "Ошибка, неверный статус")

    def test_antelope_hungry(self):
        a = autoLion("антилопа", "голодный")
        a.check()
        self.assertEqual("съесть", a.action, "Ошибка, неверное действие")
        self.assertEqual("сытый", a.status, "Ошибка, неверный статус")

    def test_antelope_full(self):
        a = autoLion("антилопа", "сытый")
        a.check()
        self.assertEqual("спать", a.action, "Ошибка, неверное действие")
        self.assertEqual("голодный", a.status, "Ошибка, неверный статус")

    def test_tree_hungry(self):
        a = autoLion("дерево", "голодный")
        a.check()
        self.assertEqual("спать", a.action, "Ошибка, неверное действие")
        self.assertEqual("голодный", a.status, "Ошибка, неверный статус")

    def test_tree_full(self):
        a = autoLion("дерево", "сытый")
        a.check()
        self.assertEqual("смотреть", a.action, "Ошибка, неверное действие")
        self.assertEqual("голодный", a.status, "Ошибка, неверный статус")


if __name__ == '__main__':
    unittest.main()