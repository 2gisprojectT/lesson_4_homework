from unittest import TestCase
import unittest
from main import Lion


class LionTests(TestCase):
    def test_constructor_wrong(self):
        self.assertRaises(ValueError, Lion, "рырыл222")

    def test_constructor_right(self):
        lion = Lion("сытый")
        self.assertEqual(lion.state, "сытый")

    def test_tree_hungry(self):
        lion = Lion("голодный")
        lion.behaving("дерево")
        self.assertEqual(lion.action, "спать")
        self.assertEqual(lion.state, "голодный")

    def test_tree_full(self):
       lion = Lion("сытый")
       lion.behaving("дерево")
       self.assertEqual(lion.action, "смотреть")
       self.assertEqual(lion.state, "голодный")

    def test_unknown_obj(self):
        lion = Lion("голодный")
        self.assertRaises(ValueError, lion.behaving, "вфвфв")

    def test_antelope_hungry(self):
       lion = Lion("голодный")
       lion.behaving("антилопа")
       self.assertEqual(lion.action, "съесть")
       self.assertEqual(lion.state, "сытый")

    def test_antelope_full(self):
        lion = Lion("сытый")
        lion.behaving("антилопа")
        self.assertEqual(lion.action, "спать")
        self.assertEqual(lion.state, "голодный")

    def test_hunter_full(self):
        lion = Lion("сытый")
        lion.behaving("охотник")
        self.assertEqual(lion.action, "убежать")
        self.assertEqual(lion.state, "голодный")

    def test_hunter_hungry(self):
        lion = Lion("голодный")
        lion.behaving("охотник")
        self.assertEqual(lion.action, "убежать")
        self.assertEqual(lion.state, "голодный")


if __name__ == '__main__':
    unittest.main()
