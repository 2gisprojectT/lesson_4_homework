import unittest

from Main import Lion, EventException, HungryException


class LionUnitTest(unittest.TestCase):
    def test_lionIO(self):
        self.assertRaises(HungryException, Lion, "Дерево", "randomed")
        self.assertRaises(EventException, Lion, "randomed", "Голодный")

    def test_hungry_tree(self):
        res = Lion("Дерево", "Голодный")
        res.launch()
        self.assertEqual("Спать", res.get_action(), "False")
        self.assertEqual("Голодный", res.get_condition(), "False")

    def test_satisfied_tree(self):
        res = Lion("Дерево", "Сытый")
        res.launch()
        self.assertEqual("Смотреть", res.get_action(), "False")
        self.assertEqual("Голодный", res.get_condition(), "False")

    def test_hungry_hunt(self):
        res = Lion("Охотник", "Голодный")
        res.launch()
        self.assertEqual("Бежать", res.get_action(), "False")
        self.assertEqual("Голодный", res.get_condition(), "False")

    def test_satisfied_hunt(self):
        res = Lion("Охотник", "Сытый")
        res.launch()
        self.assertEqual("Бежать", res.get_action(), "False")
        self.assertEqual("Голодный", res.get_condition(), "False")

    def test_hungry_antelope(self):
        res = Lion("Антилопа", "Голодный")
        res.launch()
        self.assertEqual("Съесть", res.get_action(), "False")
        self.assertEqual("Сытый", res.get_condition(), "False")

    def test_satisfied_antelope(self):
        res = Lion("Антилопа", "Сытый")
        res.launch()
        self.assertEqual("Спать", res.get_action(), "False")
        self.assertEqual("Голодный", res.get_condition(), "False")

    def test_hungry_tree_add_event(self):
        res = Lion("Дерево", "Голодный")
        res.launch()
        res.add_event("Дерево")
        res.launch()
        self.assertEqual("Спать", res.get_action(), "False")
        self.assertEqual("Голодный", res.get_condition(), "False")
        res = Lion("Дерево", "Голодный")
        res.launch()
        res.add_event("Охотник")
        res.launch()
        self.assertEqual("Бежать", res.get_action(), "False")
        self.assertEqual("Голодный", res.get_condition(), "False")
        res = Lion("Дерево", "Голодный")
        res.launch()
        res.add_event("Антилопа")
        res.launch()
        self.assertEqual("Съесть", res.get_action(), "False")
        self.assertEqual("Сытый", res.get_condition(), "False")

    def test_satisfied_antelope_add_event(self):
        res = Lion("Антилопа", "Сытый")
        res.launch()
        res.add_event("Дерево")
        res.launch()
        self.assertEqual("Спать", res.get_action(), "False")
        self.assertEqual("Голодный", res.get_condition(), "False")
        res = Lion("Дерево", "Сытый")
        res.launch()
        res.add_event("Охотник")
        res.launch()
        self.assertEqual("Бежать", res.get_action(), "False")
        self.assertEqual("Голодный", res.get_condition(), "False")
        res = Lion("Дерево", "Голодный")
        res.launch()
        res.add_event("Антилопа")
        res.launch()
        self.assertEqual("Съесть", res.get_action(), "False")
        self.assertEqual("Сытый", res.get_condition(), "False")
