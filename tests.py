from unittest import TestCase
import unittest
from main import FSM
from main import lion


class LionTests(TestCase):
    def test_all_dictionary(self):
        dictionary = lion
        for state in dictionary.keys():
            for symbol in dictionary[state].keys():
                lion_ = FSM(dictionary, state)
                lion_.input(symbol)
                self.assertEqual(lion_.action, dictionary[state][symbol]['action'])
                self.assertEqual(lion_.state, dictionary[state][symbol]['state'])


if __name__ == '__main__':
    unittest.main()
