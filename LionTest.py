from unittest import TestCase
from Lion import Lion
import unittest

trans_table = {'сытый': {'антилопа': {'action': 'спать', 'state': 'голодный'}, }, }


class LionUnittest(TestCase):
    def test_init(self):
        lion = Lion(list(trans_table.keys())[0], trans_table)
        self.assertEqual(list(lion.trans_table.keys())[0], lion.state)
        self.assertEqual(trans_table, lion.trans_table)

    def test_init_negative(self):
        self.assertRaises(ValueError, Lion, "уставший", trans_table)

    def test_transition(self):
        lion = Lion(list(trans_table.keys())[0], trans_table)
        lion.transition(list(lion.trans_table[list(lion.trans_table.keys())[0]].keys())[0])
        self.assertEqual(lion.trans_table[list(lion.trans_table.keys())[0]]
                         [list(lion.trans_table[list(lion.trans_table.keys())[0]].keys())[0]]['action'], lion.action)
        self.assertEqual(lion.trans_table[list(lion.trans_table.keys())[0]]
                         [list(lion.trans_table[list(lion.trans_table.keys())[0]].keys())[0]]['state'], lion.state)

    def test_transition_negative(self):
        lion = Lion(list(trans_table.keys())[0], trans_table)
        self.assertRaises(ValueError, lion.transition, "НЛО")


if __name__ == '__main__':
    unittest.main()
