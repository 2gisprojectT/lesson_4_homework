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
        self.assertEqual(lion.action + " " + lion.state, "спать голодный")

    def test_tree_full(self):
       lion = Lion("сытый")
       lion.behaving("дерево")
       self.assertEqual(lion.action + " " + lion.state, "смотреть голодный")

    def test_unknown_obj(self):
        lion = Lion("голодный")
        lion.behaving("вфвфв")
        self.assertEqual(lion.action + " " + lion.state, " голодный")

    def test_tree_antelope(self):
       lion = Lion("голодный")
       lion.behaving("дерево")
       lion.behaving("антилопа")
       self.assertEqual(lion.action + " " + lion.state, "съесть сытый")

    def test_hunter(self):
        lion = Lion("сытый")
        lion.behaving("охотник")
        self.assertEqual(lion.action + " " + lion.state, "убежать голодный")

    def test_tree_hunter(self):
        lion = Lion("сытый")
        lion.behaving("дерево")
        lion.behaving("охотник")
        self.assertEqual(lion.action + " " + lion.state, "убежать голодный")

    def test_tree_antelope_hunter(self):
        lion = Lion("сытый")
        lion.behaving("дерево")
        lion.behaving("антилопа")
        lion.behaving("охотник")
        self.assertEqual(lion.action + " " + lion.state, "убежать голодный")

if __name__ == '__main__':
    unittest.main()