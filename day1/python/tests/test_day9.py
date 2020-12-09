from unittest import TestCase

from day9_python.day9 import XMASData, get_preamble, get_all_combinations
from day9_python.input_test import input_test


class Test(TestCase):
    def test_get_preamble(self):
        xmas_data = XMASData(input_test)
        self.assertEqual(get_preamble(xmas_data, 5), [35,
                                                      20,
                                                      15,
                                                      25,
                                                      47])
        self.assertEqual(get_preamble(xmas_data, 6), [20,
                                                      15,
                                                      25,
                                                      47, 40])
        self.assertEqual(get_preamble(xmas_data, 7), [15,
                                                      25,
                                                      47, 40,
                                                      62])
        self.assertEqual(get_preamble(xmas_data, 8), [25,
                                                      47, 40,
                                                      62,
                                                      55])

    def test_get_all_combinations(self):
        self.assertEqual(get_all_combinations([1, 2, 3]), {2, 3, 6})
        self.assertEqual(get_all_combinations([1, 2, 3, 4, 5]), {2, 3, 4, 5, 6, 8, 10, 12, 15, 20})
