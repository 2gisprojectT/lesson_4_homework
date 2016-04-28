from unittest import TestCase
import unittest
from main import FSM

lion = {"голодный": {"антилопа": {"action": "съесть", "state": "сытый"},
                     "охотник": {"action": "убежать", "state": "голодный"},
                     "дерево": {"action": "спать", "state": "голодный"}},
        "сытый": {"антилопа": {"action": "спать", "state": "голодный"},
                  "охотник": {"action": "убежать", "state": "голодный"},
                  "дерево": {"action": "смотреть", "state": "голодный"}}}


class LionTests(TestCase):
    def test_good_init(self):
        dictionary = lion
        state = list(dictionary.keys())[0]
        symbol = list(dictionary[state].keys())[0]
        lion_ = FSM(dictionary, state)
        self.assertEqual(lion_.action, None)
        self.assertEqual(lion_.state, state)

    def test_bad_init(self):
        self.assertRaises(ValueError, FSM, lion, "холодный")

    def test_bad_input(self):
        dictionary = lion
        state = list(dictionary.keys())[0]
        lion_ = FSM(dictionary, state)
        self.assertRaises(ValueError, lion_.input, "речка")

    def test_good_input(self):
        dictionary = lion
        state = list(dictionary.keys())[0]
        symbol = list(dictionary[state].keys())[0]
        lion_ = FSM(dictionary, state)
        lion_.input(symbol)
        self.assertEqual(lion_.action, lion[state][symbol]["action"])
        self.assertEqual(lion_.state, lion[state][symbol]["state"])


if __name__ == '__main__':
    unittest.main()
