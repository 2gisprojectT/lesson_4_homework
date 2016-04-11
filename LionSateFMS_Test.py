from unittest import TestCase
from LionStFMS import LionStateFSM
import unittest

states = ['сытый', 'голодный']
objects = ['антилопа', 'охотник', 'дерево']
state_list = {
                states[0]: [objects[0], objects[1], objects[2]],
                states[1]: [objects[0], objects[1], objects[2]]
            }


class LionSateFMSTest(TestCase):
    def test_init(self):
        self.assertRaises(ValueError, LionStateFSM, "сонный")

    def test_fms_bad_obj(self):
        lion = LionStateFSM(states[1])
        self.assertRaises(ValueError, lion.fsm_realisation, "обезьяна")

    def test_init_hungry(self):
        lion = LionStateFSM(states[1])
        self.assertEqual(states[1], lion.state, "Ошибка! Должен быть " + states[1])

    def test_init_fed(self):
        lion = LionStateFSM(states[0])
        self.assertEqual(states[0], lion.state, "Ошибка! Должен быть" + states[0])

    def test_fms_fed_antelope(self):
        lion = LionStateFSM(states[0])
        lion.fsm_realisation(state_list[states[0]][0])
        self.assertEqual(lion.state_list[states[0]][objects[0]][0], lion.action,
                         "Ошибка! Должен быть " + lion.state_list[states[0]][objects[0]][0])
        self.assertEqual(lion.state_list[states[0]][objects[0]][1], lion.state,
                         "Ошибка! Должен быть " + lion.state_list[states[0]][objects[0]][1])

    def test_fms_hungry_antelope(self):
        lion = LionStateFSM(states[1])
        lion.fsm_realisation(state_list[states[1]][0])
        self.assertEqual(lion.state_list[states[1]][objects[0]][0], lion.action,
                         "Ошибка! Должен быть " + lion.state_list[states[1]][objects[0]][0])
        self.assertEqual(lion.state_list[states[1]][objects[0]][1], lion.state,
                         "Ошибка! Должен быть " + lion.state_list[states[1]][objects[0]][1])

    def test_fms_fed_hunter(self):
        lion = LionStateFSM(states[0])
        lion.fsm_realisation(state_list[states[0]][1])
        self.assertEqual(lion.state_list[states[0]][objects[1]][0], lion.action,
                         "Ошибка! Должен быть " + lion.state_list[states[0]][objects[1]][0])
        self.assertEqual(lion.state_list[states[0]][objects[1]][1], lion.state,
                         "Ошибка! Должен быть " + lion.state_list[states[0]][objects[1]][1])

    def test_fms_hungry_hunter(self):
        lion = LionStateFSM(states[1])
        lion.fsm_realisation(state_list[states[1]][1])
        self.assertEqual(lion.state_list[states[1]][objects[1]][0], lion.action,
                         "Ошибка! Должен быть " + lion.state_list[states[1]][objects[1]][0])
        self.assertEqual(lion.state_list[states[1]][objects[1]][1], lion.state,
                         "Ошибка! Должен быть " + lion.state_list[states[1]][objects[1]][1])

    def test_fms_fed_tree(self):
        lion = LionStateFSM(states[0])
        lion.fsm_realisation(state_list[states[0]][2])
        self.assertEqual(lion.state_list[states[0]][objects[2]][0], lion.action,
                         "Ошибка! Должен быть " + lion.state_list[states[0]][objects[2]][0])
        self.assertEqual(lion.state_list[states[0]][objects[2]][1], lion.state,
                         "Ошибка! Должен быть " + lion.state_list[states[0]][objects[2]][1])

    def test_fms_hungry_tree(self):
        lion = LionStateFSM(states[1])
        lion.fsm_realisation(state_list[states[1]][2])
        self.assertEqual(lion.state_list[states[1]][objects[2]][0], lion.action,
                         "Ошибка! Должен быть " + lion.state_list[states[1]][objects[2]][0])
        self.assertEqual(lion.state_list[states[1]][objects[2]][1], lion.state,
                         "Ошибка! Должен быть " + lion.state_list[states[1]][objects[2]][1])

if __name__ == '__main__':
    unittest.main()
