from unittest import TestCase
from LionStFMS import LionStateFSM
import unittest

lion_state_list = {'state': 'сытый', 'object': 'антилопа', 'action': 'спать', 'new_state': 'голодный'}
bad_state_list = {'bad_state': 'сонный', 'bad_object': 'обезьяна'}


class LionSateFMSTest(TestCase):

    def test_good_init_state(self):
        lion = LionStateFSM(lion_state_list['state'], lion_state_list)
        self.assertEqual(lion_state_list['state'], lion.state)

    def test_bad_init_state(self):
        self.assertRaises(ValueError, LionStateFSM, bad_state_list['bad_state'], lion_state_list)

    def test_init_good_obj(self):
        lion = LionStateFSM(lion_state_list['state'], lion_state_list)
        lion.fsm_realisation(lion_state_list['object'])
        self.assertEqual(lion_state_list['action'], lion.action)
        self.assertEqual(lion_state_list['new_state'], lion.state)

    def test_init_bad_obj(self):
        lion = LionStateFSM(lion_state_list['state'], lion_state_list)
        self.assertRaises(ValueError, lion.fsm_realisation, bad_state_list['bad_object'])

if __name__ == '__main__':
    unittest.main()
