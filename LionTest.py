from unittest import TestCase
from Lion import Lion
import unittest

trans_table = {'сытый': {'антилопа': {'action': 'спать', 'state': 'голодный'}, }, }
key_state = list(trans_table.keys())[0]
key_symbol = list(trans_table[key_state].keys())[0]


class LionUnittest(TestCase):
    def test_init(self):
        lion = Lion(key_state, trans_table)
        self.assertEqual(key_state, lion.state)
        self.assertEqual(trans_table, lion.trans_table)

    def test_init_negative(self):
        self.assertRaises(ValueError, Lion, "уставший", trans_table)

    def test_transition(self):
        lion = Lion(key_state, trans_table)
        lion.transition(key_symbol)
        self.assertEqual(trans_table[key_state][key_symbol]['action'], lion.action)
        self.assertEqual(trans_table[key_state][key_symbol]['state'], lion.state)

    def test_transition_negative(self):
        lion = Lion(key_state, trans_table)
        self.assertRaises(ValueError, lion.transition, "НЛО")


if __name__ == '__main__':
    unittest.main()
