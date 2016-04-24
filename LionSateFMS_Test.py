from unittest import TestCase
from LionStFMS import LionStateFSM
import unittest

lion_state_list = {
                     'сытый': {
                         'антилопа': {'action': 'спать', 'new_state': 'голодный'}
                     }
                   }

state_list_wrapper = {
                      'state': list(lion_state_list.keys())[0],
                      'object': list(lion_state_list[list(lion_state_list.keys())[0]].keys())[0],
                      'bad_obj': 'обезьяна',
                      'bad_state': 'сонный'
                    }


class LionSateFMSTest(TestCase):

    def test_good_init_state(self):
        lion = LionStateFSM(state_list_wrapper['state'], lion_state_list)
        self.assertEqual(state_list_wrapper['state'], lion.state)
        self.assertEqual(lion_state_list, lion.state_list)
        self.assertEqual(None, lion.action)

    def test_bad_init_state(self):
        self.assertRaises(ValueError, LionStateFSM, state_list_wrapper['bad_state'], lion_state_list)

    def test_empty_data(self):
        self.assertRaises(ValueError, LionStateFSM, None, None)

    def test_init_good_obj(self):
        lion = LionStateFSM(state_list_wrapper['state'], lion_state_list)
        lion.fsm_realisation(state_list_wrapper['object'])
        self.assertEqual(lion_state_list[state_list_wrapper['state']][state_list_wrapper['object']]['action'], lion.action)
        self.assertEqual(lion_state_list[state_list_wrapper['state']][state_list_wrapper['object']]['new_state'], lion.state)

    def test_init_bad_obj(self):
        lion = LionStateFSM(state_list_wrapper['state'], lion_state_list)
        self.assertRaises(ValueError, lion.fsm_realisation, state_list_wrapper['bad_obj'])

if __name__ == '__main__':
    unittest.main()
