from unittest import TestCase
from LionStFMS import LionStateFSM
import unittest

lion_state_list = {
                     'сытый': {
                         'антилопа': {'action': 'спать', 'new_state': 'голодный', 'bad_obj': 'обезьяна', 'bad_state': 'сонный'}
                     }
                   }

state_list_wrapper = {
                      'state': tuple(lion_state_list)[0],
                      'object': tuple(lion_state_list[tuple(lion_state_list)[0]])[0],
                      'action': lion_state_list[tuple(lion_state_list)[0]][tuple(lion_state_list[tuple(lion_state_list)[0]])[0]]['action'],
                      'new_state': lion_state_list[tuple(lion_state_list)[0]][tuple(lion_state_list[tuple(lion_state_list)[0]])[0]]['new_state'],
                      'bad_state': lion_state_list[tuple(lion_state_list)[0]][tuple(lion_state_list[tuple(lion_state_list)[0]])[0]]['bad_state'],
                      'bad_obj': lion_state_list[tuple(lion_state_list)[0]][tuple(lion_state_list[tuple(lion_state_list)[0]])[0]]['bad_obj']
                      }


class LionSateFMSTest(TestCase):

    def test_good_init_state(self):
        lion = LionStateFSM(state_list_wrapper['state'], lion_state_list)
        self.assertEqual(state_list_wrapper['state'], lion.state)
        self.assertEqual(None, lion.action)

    def test_bad_init_state(self):
        self.assertRaises(ValueError, LionStateFSM, state_list_wrapper['bad_state'], lion_state_list)

    def test_empty_data(self):
        self.assertRaises(ValueError, LionStateFSM, state_list_wrapper[None], None)

    def test_init_good_obj(self):
        lion = LionStateFSM(state_list_wrapper['state'], lion_state_list)
        lion.fsm_realisation(state_list_wrapper['object'])
        self.assertEqual(state_list_wrapper['action'], lion.action)
        self.assertEqual(state_list_wrapper['new_state'], lion.state)

    def test_init_bad_obj(self):
        lion = LionStateFSM(state_list_wrapper['state'], lion_state_list)
        self.assertRaises(ValueError, lion.fsm_realisation, state_list_wrapper['bad_obj'])

if __name__ == '__main__':
    unittest.main()
    
