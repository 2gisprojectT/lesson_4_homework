from unittest import TestCase
from LionStFMS import LionStateFSM
import unittest


class LionSateFMSTest(TestCase):

    def test_init(self):
        self.assertRaises(ValueError, LionStateFSM, "сонный")

    def test_fms_bad_obj(self):
        lion = LionStateFSM("голодный")
        self.assertRaises(ValueError, lion.fsm_realisation, "обезьяна")

    def test_init_hungry(self):
        lion = LionStateFSM("голодный")
        self.assertEqual("голодный", lion.state, "Ошибка! Должен быть голодный")

    def test_init_fed(self):
        lion = LionStateFSM("сытый")
        self.assertEqual("сытый", lion.state, "Ошибка! Должен быть сытый")

    def test_fms_fed_antelope(self):
        lion = LionStateFSM("сытый")
        lion.fsm_realisation("антилопа")
        self.assertEqual("спать", lion.action, "Ошибка! Должен быть спать")
        self.assertEqual("голодный", lion.state, "Ошибка! Должен быть голодный")

    def test_fms_hungry_antelope(self):
        lion = LionStateFSM("голодный")
        lion.fsm_realisation("антилопа")
        self.assertEqual("съесть", lion.action, "Ошибка! Должен быть съесть")

    def test_fms_fed_hunter(self):
        lion = LionStateFSM("сытый")
        lion.fsm_realisation("охотник")
        self.assertEqual("убежать", lion.action, "Ошибка! Должен быть убежать")
        self.assertEqual("голодный", lion.state, "Ошибка! Должен быть голодный")

    def test_fms_hungry_hunter(self):
        lion = LionStateFSM("голодный")
        lion.fsm_realisation("охотник")
        self.assertEqual("убежать", lion.action, "Ошибка! Должен быть убежать")
        self.assertEqual("голодный", lion.state, "Ошибка! Должен быть голодный")

    def test_fms_fed_tree(self):
        lion = LionStateFSM("сытый")
        lion.fsm_realisation("дерево")
        self.assertEqual("смотреть", lion.action, "Ошибка! Должен быть убежать")
        self.assertEqual("голодный", lion.state, "Ошибка! Должен быть голодный")

    def test_fms_hungry_tree(self):
        lion = LionStateFSM("голодный")
        lion.fsm_realisation("дерево")
        self.assertEqual("спать", lion.action, "Ошибка! Должен быть спать")
        self.assertEqual("голодный", lion.state, "Ошибка! Должен быть голодный")

if __name__ == '__main__':
    unittest.main()
