from unittest import TestCase
from LionStFMS import LionStateFSM
import unittest

class LionSateFMS_Test(TestCase):

    #Тест вывода ошибки конструктором, при вводе не верных значений символа и состояния
    def test_init(self):
        self.assertRaises(NameError, LionStateFSM("фывваыв", "sdfaf"))

    #Тест корректности работы конечного автомата состояния
    def test_fms(self):
        lion = LionStateFSM("антилопа", "сытый")
        lion.fsm_realisation()
        self.assertEqual("спать", lion.action, "Ошибка! Должен быть спать")
        self.assertEqual("голодный", lion.state, "Ошибка! Должен быть голодный")

        lion = LionStateFSM("антилопа", "голодный")
        lion.fsm_realisation()
        self.assertEqual("съесть", lion.action, "Ошибка! Должен быть съесть")
        self.assertEqual("сытый", lion.state, "Ошибка! Должен быть сытый")

        lion = LionStateFSM("охотник", "сытый")
        lion.fsm_realisation()
        self.assertEqual("убежать", lion.action, "Ошибка! Должен быть убежать")
        self.assertEqual("голодный", lion.state, "Ошибка! Должен быть голодный")

        lion = LionStateFSM("охотник", "голодный")
        lion.fsm_realisation()
        self.assertEqual("убежать", lion.action, "Ошибка! Должен быть убежать")
        self.assertEqual("голодный", lion.state, "Ошибка! Должен быть голодный")

        lion = LionStateFSM("дерево", "сытый")
        lion.fsm_realisation()
        self.assertEqual("смотреть", lion.action, "Ошибка! Должен быть убежать")
        self.assertEqual("голодный", lion.state, "Ошибка! Должен быть голодный")

        lion = LionStateFSM("дерево", "голодный")
        lion.fsm_realisation()
        self.assertEqual("спать", lion.action, "Ошибка! Должен быть спать")
        self.assertEqual("голодный", lion.state, "Ошибка! Должен быть голодный")

if __name__ == '__main__':
    unittest.main()





