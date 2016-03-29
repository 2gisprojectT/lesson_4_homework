from unittest import TestCase
from homework4 import LionStates
import unittest


class LionStatesTest(TestCase):
    # Тест на перехват ошибки, при передаче конструктору некорректного значения
    def test_args(self):
        self.assertRaises(ValueError, LionStates, "asds2gda", "asdasd")
        self.assertRaises(ValueError, LionStates, "блаблабла", "adfasf")

    # Тесты на корректность поведения льва в зависимости от входных данных
    def test_LionStates(self):
        lion = LionStates("сытый", "антилопа")
        lion.implementation_fsm()
        self.assertEqual("голодный", lion.state, "wrong state, should be 'голодный'!")
        self.assertEqual("спать", lion.action, "wrong action, should be 'спать'!")

        lion = LionStates("сытый", "охотник")
        lion.implementation_fsm()
        self.assertEqual("голодный", lion.state, "wrong state, should be 'голодный'!")
        self.assertEqual("убежать", lion.action, "wrong action, should be 'убежать'!")

        lion = LionStates("сытый", "дерево")
        lion.implementation_fsm()
        self.assertEqual("голодный", lion.state, "wrong state, should be 'голодный'!")
        self.assertEqual("смотреть", lion.action, "wrong action, should be 'смотреть'!")

        lion = LionStates("голодный", "антилопа")
        lion.implementation_fsm()
        self.assertEqual("сытый", lion.state, "wrong state, should be 'сытый'!")
        self.assertEqual("съесть", lion.action, "wrong action, should be 'съесть'!")

        lion = LionStates("голодный", "охотник")
        lion.implementation_fsm()
        self.assertEqual("голодный", lion.state, "wrong state, should be 'голодный'!")
        self.assertEqual("убежать", lion.action, "wrong action, should be 'убежать'!")

        lion = LionStates("голодный", "дерево")
        lion.implementation_fsm()
        self.assertEqual("голодный", lion.state, "wrong state, should be 'голодный'!")
        self.assertEqual("спать", lion.action, "wrong action, should be 'спать'!")


if __name__ == '__main__':
    unittest.main()
