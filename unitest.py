import unittest

from Main import *


class lion_unit_test(unittest.TestCase):
    def test_lionIO(self):
        self.assertRaises(ValueError, lion, "Дерево", "randombred")
        self.assertRaises(EventException, lion, "randombred", "Сытый")

        res = lion("Дерево", "Голодный")
        self.assertEqual("Спать", res.action, "False")
        self.assertEqual("Голодный", res.condition, "False")

        res.introduce_new_event("Антилопа")
        self.assertEqual("Съесть", res.action, "False")
        self.assertEqual("Сытый", res.condition, "False")

        res = lion("Дерево", "Сытый")
        self.assertEqual("Смотреть", res.action, "False")
        self.assertEqual("Голодный", res.condition, "False")

        res = lion("Охотник", "Голодный")
        self.assertEqual("Бежать", res.action, "False")
        self.assertEqual("Голодный", res.condition, "False")

        res = lion("Охотник", "Сытый")
        self.assertEqual("Бежать", res.action, "False")
        self.assertEqual("Голодный", res.condition, "False")

        res.introduce_new_event("Охотник")
        self.assertEqual("Бежать", res.action, "False")
        self.assertEqual("Голодный", res.condition, "False")

        res = lion("Антилопа", "Голодный")
        self.assertEqual("Съесть", res.action, "False")
        self.assertEqual("Сытый", res.condition, "False")

        res.introduce_new_event("Антилопа")
        self.assertEqual("Спать", res.action, "False")
        self.assertEqual("Голодный", res.condition, "False")

        res = lion("Антилопа", "Сытый")
        self.assertEqual("Спать", res.action, "False")
        self.assertEqual("Голодный", res.condition, "False")


if __name__ == '__main__':
    unittest.main()
