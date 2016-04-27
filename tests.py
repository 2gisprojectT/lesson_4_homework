from unittest import TestCase
import unittest
from main import FSM
from main import lion


class LionTests(TestCase):
    def test_all_dictionary(self):
        dictionary = lion
        for state in dictionary["state"].keys():
            for symbol in dictionary["state"][state]["symbol"].keys():
                lion_ = FSM(dictionary, state)
                lion_.input(symbol)
                self.assertEqual(lion_.action, dictionary["state"][state]["symbol"][symbol]['action'])
                self.assertEqual(lion_.state, dictionary["state"][state]["symbol"][symbol]['state'])


if __name__ == '__main__':
    unittest.main()
