import task4
import unittest
from unittest import TestCase


class TestTask(TestCase):

    def test_N_is_int(self):
        self.assertTrue(type(task4.N) == int)
        self.assertFalse(type(task4.N) != int)

    def test_T_have_key(self):
        self.assertGreater(task4.T, 1)

    def test_dic_is_dict(self):
        self.assertTrue(type(task4.dic) == dict)
        self.assertFalse(type(task4.dic) != dict)


if __name__ == '__main__':
    unittest.main()
