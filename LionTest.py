from unittest import TestCase
from Lion import Lion
import unittest


class LionUnittest(TestCase):
    def test_init(self):
        lion = Lion("Голодный")
        self.assertEqual("голодный", lion.state, "ошибка инициализации состояния")
        lion = Lion("Сытый")
        self.assertEqual("сытый", lion.state, "ошибка инициализации состояния")

    def test_action(self):
        lion = Lion("голодный")
        self.assertEqual("съесть", lion.action("антилопа"), "ошибка действия из состояния голодный по символу 'антилопа'")
        self.assertEqual("сытый", lion.state, "ошибка смены состояний голодный-сытый по символу 'антилопа'")

        lion = Lion("сытый")
        self.assertEqual("спать", lion.action("антилопа"), "ошибка действия из состояния сытый по символу 'антилопа'")
        self.assertEqual("голодный", lion.state, "ошибка смены состояний сытый-голодный по символу 'антилопа'")

        lion = Lion("голодный")
        self.assertEqual("убежать", lion.action("охотник"), "ошибка действия из состояния голодный по символу 'охотник'")
        self.assertEqual("голодный", lion.state, "ошибка смены состояний голодный-голодный по символу 'охотник'")

        lion = Lion("сытый")
        self.assertEqual("убежать", lion.action("охотник"), "ошибка действия из состояния сытый по символу 'охотник'")
        self.assertEqual("голодный", lion.state, "ошибка смены состояний сытый-голодный по символу 'охотник'")

        lion = Lion("голодный")
        self.assertEqual("спать", lion.action("дерево"), "ошибка действия из состояния голодный по символу 'дерево'")
        self.assertEqual("голодный", lion.state, "ошибка смены состояний голодный-голодный по символу 'дерево'")

        lion = Lion("сытый")
        self.assertEqual("смотреть", lion.action("дерево"), "ошибка действия из состояния сытый по символу 'дерево'")
        self.assertEqual("голодный", lion.state, "ошибка смены состояний сытый-голодный по символу 'дерево'")


if __name__ == '__main__':
    unittest.main()