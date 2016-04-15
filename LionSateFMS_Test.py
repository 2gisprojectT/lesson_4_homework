from unittest import TestCase
from LionStFMS import LionStateFSM
import unittest

lion_state_list = {
                    'сытый': {
                        'антилопа': {'action': 'спать', 'new_state': 'голодный'}
                    }
                  }


class LionSateFMSTest(TestCase):

    def test_good_init_state(self):
            lion = LionStateFSM('сытый', lion_state_list)
            self.assertEqual('сытый', lion.state, "Ошибка! Должен быть " + 'сытый')

    def test_bad_init_state(self):
        self.assertRaises(ValueError, LionStateFSM, "сонный", lion_state_list)

    def test_init_good_obj(self):
            lion = LionStateFSM('сытый', lion_state_list)
            lion.fsm_realisation('антилопа')
            self.assertEqual(lion.state_list['сытый']['антилопа']['action'], lion.action,
                             "Ошибка! Должен быть " + lion.state_list['сытый']['антилопа']['action'])
            self.assertEqual(lion.state_list['сытый']['антилопа']['new_state'], lion.state,
                             "Ошибка! Должен быть " + lion.state_list['сытый']['антилопа']['new_state'])

    def test_init_bad_obj(self):
        lion = LionStateFSM('сытый', lion_state_list)
        self.assertRaises(ValueError, lion.fsm_realisation, "обезьяна")

if __name__ == '__main__':
    unittest.main()
