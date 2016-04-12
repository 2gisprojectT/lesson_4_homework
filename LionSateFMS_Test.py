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

    def test_init_state(self):
        for state in states:
            lion = LionStateFSM(state)
            self.assertEqual(state, lion.state, "Ошибка! Должен быть " + state)

    def test_bad_init(self):
        self.assertRaises(ValueError, LionStateFSM, "сонный")

    def test_init_obj_at_fed_lion(self):
        for obj in state_list[states[0]]:
            lion = LionStateFSM(states[0])
            lion.fsm_realisation(obj)
            self.assertEqual(lion.state_list[states[0]][obj]['action'], lion.action,
                             "Ошибка! Должен быть " + lion.state_list[states[0]][obj]['action'])
            self.assertEqual(lion.state_list[states[0]][obj]['state'], lion.state,
                             "Ошибка! Должен быть " + lion.state_list[states[0]][obj]['state'])

    def test_init_obj_at_hungry_lion(self):
        for obj in state_list[states[1]]:
            lion = LionStateFSM(states[1])
            lion.fsm_realisation(obj)
            self.assertEqual(lion.state_list[states[1]][obj]['action'], lion.action,
                             "Ошибка! Должен быть " + lion.state_list[states[0]][obj]['action'])
            self.assertEqual(lion.state_list[states[1]][obj]['state'], lion.state,
                             "Ошибка! Должен быть " + lion.state_list[states[0]][obj]['state'])

    def test_init_bad_obj(self):
        lion = LionStateFSM(states[1])
        self.assertRaises(ValueError, lion.fsm_realisation, "обезьяна")

if __name__ == '__main__':
    unittest.main()
