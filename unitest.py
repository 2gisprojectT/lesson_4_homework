from Main import *
import unittest


class LionUniTest(unittest.TestCase):
    def test_LionIO(self):
        self.assertRaises(ValueError, Lion, "Дерево", "randombred")
        self.assertRaises(EventException, Lion, "randombred", "Сытый")

        res = Lion("Дерево", "Голодный")
        self.assertEqual("Спать", res.action, "False")
        self.assertEqual("Голодный", res.condition, "False")

        res = Lion("Дерево", "Сытый")
        self.assertEqual("Смотреть", res.action, "False")
        self.assertEqual("Голодный", res.condition, "False")

        res = Lion("Охотник", "Голодный")
        self.assertEqual("Бежать", res.action, "False")
        self.assertEqual("Голодный", res.condition, "False")

        res = Lion("Охотник", "Сытый")
        self.assertEqual("Бежать", res.action, "False")
        self.assertEqual("Голодный", res.condition, "False")

        res = Lion("Антилопа", "Голодный")
        self.assertEqual("Съесть", res.action, "False")
        self.assertEqual("Сытый", res.condition, "False")

        res = Lion("Антилопа", "Сытый")
        self.assertEqual("Спать", res.action, "False")
        self.assertEqual("Голодный", res.condition, "False")


if __name__ == '__main__':
    unittest.main()
