from unittest import TestCase

from day9_python.day9 import XMASData, get_preamble, get_all_combinations, find_first_anomaly, find_encryption_weakness, \
    get_subsequences_of_size
from day9_python.input_prod import input_prod
from day9_python.input_test import input_test


class Test(TestCase):
    def test_get_preamble(self):
        xmas_data = XMASData(input_test)
        self.assertEqual(get_preamble(xmas_data, 5, 5), [35,
                                                         20,
                                                         15,
                                                         25,
                                                         47])
        self.assertEqual(get_preamble(xmas_data, 6, 5), [20,
                                                         15,
                                                         25,
                                                         47, 40])
        self.assertEqual(get_preamble(xmas_data, 7, 5), [15,
                                                         25,
                                                         47, 40,
                                                         62])
        self.assertEqual(get_preamble(xmas_data, 8, 5), [25,
                                                         47, 40,
                                                         62,
                                                         55])

    def test_get_all_combinations(self):
        self.assertEqual(get_all_combinations([1, 2, 3]), {3, 4, 5})
        self.assertEqual(get_all_combinations([1, 2, 3, 4, 5]), {3, 4, 5, 6, 7, 8, 9})
        self.assertEqual(get_all_combinations(get_preamble(XMASData(input_test), 5, 5)),
                         {35, 67, 40, 72, 45, 50, 82, 55, 60, 62})

    def test_find_first_anomaly(self):
        self.assertEqual(find_first_anomaly(input_test, 5), 127)
        self.assertEqual(find_first_anomaly(input_prod, 25), 167829540)

    def test_find_encryption_weakness(self):
        self.assertEqual(find_encryption_weakness(input_test, 127), 62)
        self.assertEqual(find_encryption_weakness(input_prod, 167829540), 28045630)

    def test_get_subsequences_of_size(self):
        self.assertEqual(get_subsequences_of_size([1, 2, 3, 4], 2), [[1, 2], [2, 3], [3, 4]])
        self.assertEqual(get_subsequences_of_size([1, 2, 3, 4], 3), [[1, 2, 3], [2, 3, 4]])
