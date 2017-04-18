from unittest import TestCase
import unittest
from main import Lion


class LionTests(TestCase):
    def test_constructor_wrong(self):
        try:
            lion = Lion("рырыл222")
        except ValueError:
            print("недопустимое состояние")

    def test_constructor_right(self):
        try:
            lion = Lion("сытый")
            self.assertEqual(lion.state, "сытый")
        except ValueError:
            print("недопустимое состояние")

    def test_tree_hungry(self):
        try:
            lion = Lion("голодный")
            self.assertEqual(lion.behaving("дерево"), "спать голодный")
        except ValueError:
            print("недопустимое состояние")

    def test_tree_full(self):
        try:
            lion = Lion("сытый")
            self.assertEqual(lion.behaving("дерево"), "смотреть голодный")
        except ValueError:
            print("недопустимое состояние")

    def test_unknownObj(self):
        try:
            lion = Lion("голодный")
            self.assertEqual(lion.behaving("вфвфв"), "данного объекта не предусмотрено")
        except ValueError:
            print("недопустимое состояние")

    def test_tree_antelope(self):
        try:
            lion = Lion("голодный")
            lion.behaving("дерево")
            self.assertEqual(lion.behaving("антилопа"), "съесть сытый")
        except ValueError:
            print("недопустимое состояние")

    def test_hunter(self):
        try:
            lion = Lion("сытый")
            self.assertEqual(lion.behaving("охотник"), "убежать голодный")
        except ValueError:
            print("недопустимое состояние")

    def test_tree_hunter(self):
        try:
            lion = Lion("сытый")
            lion.behaving("дерево")
            self.assertEqual(lion.behaving("охотник"), "убежать голодный")
        except ValueError:
            print("недопустимое состояние")

    def test_tree_antelope_hunter(self):
        try:
            lion = Lion("сытый")
            lion.behaving("дерево")
            lion.behaving("антилопа")
            self.assertEqual(lion.behaving("охотник"), "убежать голодный")
        except ValueError:
            print("недопустимое состояние")


if __name__ == '__main__':
    unittest.main()