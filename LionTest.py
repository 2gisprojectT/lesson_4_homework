from unittest import TestCase
from Lion import Lion
import unittest


class LionUnittest(TestCase):
    def test_new_full(self):
        lion = Lion("голодный")
        self.assertEqual("голодный", lion.state)

    def test_new_hungry(self):
        lion = Lion("сытый")
        self.assertEqual("сытый", lion.state)

    def test_new_negative(self):
        lion = Lion("уставший")
        self.assertIsNone(lion.state)

    def test_transition_hungry_antelope(self):
        lion = Lion("голодный")
        lion.transition("антилопа")
        self.assertEqual("съесть", lion.action, "ошибка действия")
        self.assertEqual("сытый", lion.state, "ошибка состояния")

    def test_transition_full_antelope(self):
        lion = Lion("сытый")
        lion.transition("антилопа")
        self.assertEqual("спать", lion.action, "ошибка действия")
        self.assertEqual("голодный", lion.state, "ошибка состояния")

    def test_transition_hungry_hunter(self):
        lion = Lion("голодный")
        lion.transition("охотник")
        self.assertEqual("убежать", lion.action, "ошибка действия")
        self.assertEqual("голодный", lion.state, "ошибка состояния")

    def test_transition_full_hunter(self):
        lion = Lion("сытый")
        lion.transition("охотник")
        self.assertEqual("убежать", lion.action, "ошибка действия")
        self.assertEqual("голодный", lion.state, "ошибка состояния")

    def test_transition_hungry_tree(self):
        lion = Lion("голодный")
        lion.transition("дерево")
        self.assertEqual("спать", lion.action, "ошибка действия")
        self.assertEqual("голодный", lion.state, "ошибка состояния")

    def test_transition_full_tree(self):
        lion = Lion("сытый")
        lion.transition("дерево")
        self.assertEqual("смотреть", lion.action, "ошибка действия")
        self.assertEqual("голодный", lion.state, "ошибка состояния")

    def test_transition_hungry_negative(self):
        lion = Lion("голодный")
        self.assertEqual("Неверный входной символ", lion.transition("НЛО"), "ошибка действия")
        self.assertEqual("голодный", lion.state, "ошибка состояния")

    def test_transition_full_negative(self):
        lion = Lion("сытый")
        self.assertEqual("Неверный входной символ", lion.transition("НЛО"), "ошибка действия")
        self.assertEqual("сытый", lion.state, "ошибка состояния")


if __name__ == '__main__':
    unittest.main()