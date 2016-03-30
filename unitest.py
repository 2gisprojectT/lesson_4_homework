from Main import Lion
import unittest


class LionUniTest(unittest.TestCase):
    def test_LionTestIO(self):
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
