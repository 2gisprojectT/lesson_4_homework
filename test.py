from mainLion import Lion
from unittest import TestCase
import unittest

class LionTest (TestCase) :
    def test_full_antelope (self) :
        fsm_lion = Lion("full")
        fsm_lion.implementation("antelope")
        self.assertEqual("hungry", fsm_lion.state, "wrong state")
        self.assertEqual("sleep", fsm_lion.action, "wrong action")

    def test_full_hunter (self) :
        fsm_lion = Lion("full")
        fsm_lion.implementation("hunter")
        self.assertEqual("hungry", fsm_lion.state, "wrong state")
        self.assertEqual("run", fsm_lion.action, "wrong action")

    def test_full_tree (self) :
        fsm_lion = Lion("full")
        fsm_lion.implementation("tree")
        self.assertEqual("hungry", fsm_lion.state, "wrong state")
        self.assertEqual("look", fsm_lion.action, "wrong action")

    def test_hungry_antelope (self) :
        fsm_lion = Lion("hungry")
        fsm_lion.implementation("antelope")
        self.assertEqual("full", fsm_lion.state, "wrong state")
        self.assertEqual("eat", fsm_lion.action, "wrong action")

    def test_hungry_hunter (self) :
        fsm_lion = Lion("hungry")
        fsm_lion.implementation("hunter")
        self.assertEqual("hungry", fsm_lion.state, "wrong state")
        self.assertEqual("run", fsm_lion.action, "wrong action")

    def test_hungry_tree (self) :
        fsm_lion = Lion("hungry")
        fsm_lion.implementation("tree")
        self.assertEqual("hungry", fsm_lion.state, "wrong state")
        self.assertEqual("sleep", fsm_lion.action, "wrong action")

    def test_create_state_full (self) :
        fsm_lion = Lion("full")
        self.assertEqual("full", fsm_lion.state, "wrong state")

    def test_create_state_hungry (self) :
        fsm_lion = Lion("hungry")
        self.assertEqual("hungry", fsm_lion.state, "wrong state")

    def test_incorrect_state_full (self) :
        fsm_lion = Lion("full")
        self.assertRaises(ValueError, fsm_lion.implementation, "rabbit")

    def test_incorrect_state_hungry (self) :
        fsm_lion = Lion("hungry")
        self.assertRaises(ValueError, fsm_lion.implementation, "cow")

    def test_incorrect_arguments (self) :
        self.assertRaises(ValueError, Lion, "happy")

    if __name__ == '__main__' :
        unittest.main()
