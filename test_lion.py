from unittest import TestCase
from lion import Lion
import unittest

class TestLion(TestCase):
    correctResults = [('голодный', 'спать'), ('сытый', 'съесть'),
                      ('голодный', 'убежать'), ('голодный', 'убежать'),
                      ('голодный', 'смотреть'), ('голодный', 'спать')]

    def test_init(self):
        self.assertEqual('сытый', Lion('сытый').get_state(), 'State have wrong value')
        self.assertEqual('голодный', Lion('голодный').get_state(), 'State have wrong value')
        self.assertRaises(ValueError, Lion, 'фывфаы')

    def test_action(self):
        i = 0
        for factor in Lion.factors:
            for state in Lion.states:
                lion = Lion(state)
                action = lion.action(factor)
                self.assertEqual(lion.get_state(), self.correctResults[i][0],
                                 'New state is wrong by factor = %s, old state = %s'
                                 %(factor, state))
                self.assertEqual(action, self.correctResults[i][1],
                                 'Action is wrong by factor = %s, state = %s'
                                 %(factor, state))
                i += 1
        self.assertRaises(ValueError, lion.action, 'фыв')
if __name__ == '__main__':
    unittest.main()