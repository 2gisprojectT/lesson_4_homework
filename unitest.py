from Main import Lion
import unittest

class LionUniTest(unittest.TestCase):
    def test_LionTestIO (self):
        res = Lion("Дерево","Голодный")
        self.assertEqual("Спать", res.action, "False")
        self.assertEqual("Голодный",res.condition,"Error")

        res = Lion("Дерево", "Сытый")
        self.assertEqual("Смотреть", res.action, "False")
        self.assertEqual("Голодный", res.condition, "Error")



if __name__ == '__main__':
    unittest.main()