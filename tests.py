from unittest import TestCase
import unittest
from main import Lion


class LionTests(TestCase):
    def test1(self):
        lion = Lion("голодный")
        self.assertEqual(lion.behaving("дерево"), "спать голодный", 'Неправильная работа')

    def test1_1(self):
        lion = Lion("сытый")
        self.assertEqual(lion.behaving("дерево"), "смотреть голодный", 'Неправильная работа')

    def test2(self):
        lion = Lion("голодный")
        self.assertEqual(lion.behaving("вфвфв"), "данного объекта не предусмотрено", 'Неправильная работа')

    def test3(self):
        lion = Lion("голодный")
        lion.behaving("дерево")
        self.assertEqual(lion.behaving("антилопа"), "съесть сытый", 'Неправильная работа')

    def test4(self):
        lion = Lion("сытый")
        self.assertEqual(lion.behaving("охотник"), "убежать голодный", 'Неправильная работа')

    def test5(self):
        lion = Lion("сытый")
        lion.behaving("дерево")
        self.assertEqual(lion.behaving("охотник"), "убежать голодный", 'Неправильная работа')

    def test6(self):
        lion = Lion("сытый")
        lion.behaving("дерево")
        lion.behaving("антилопа")
        self.assertEqual(lion.behaving("охотник"), "убежать голодный", 'Неправильная работа')


if __name__ == '__main__':
    unittest.main()
