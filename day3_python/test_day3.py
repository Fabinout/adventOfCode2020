from unittest import TestCase

from day3_python.day3 import getVal, get_positions, getval_tuple


class Test(TestCase):
    def test_get_val(self):
        self.assertFalse(getVal(0, 0))
        self.assertTrue(getVal(1, 0))
        self.assertTrue(getVal(12, 0))
        self.assertFalse(getVal(11, 0))

    def test_get_positions(self):
        self.assertEqual(get_positions(3, 1, 3), [(0, 0), (3, 1), (6, 2)])

    def test_count_number_of_trees(self):
        # print(f'{get_positions(3,1,326)=}')
        self.assertEqual(list(map(getval_tuple, get_positions(3, 1, 323))).count(True), 247)

    def test_count_number_of_trees_in_all_slopes(self):
        # print(f'{get_positions(3,1,326)=}')
        self.assertEqual(list(map(getval_tuple, get_positions(1, 1, 323))).count(True), 78)
        self.assertEqual(list(map(getval_tuple, get_positions(3, 1, 323))).count(True), 247)
        self.assertEqual(list(map(getval_tuple, get_positions(5, 1, 323))).count(True), 68)
        self.assertEqual(list(map(getval_tuple, get_positions(7, 1, 323))).count(True), 69)
        self.assertEqual(list(map(getval_tuple, get_positions(1, 2, 323))).count(True), 33)

        self.assertEqual(2983070376,
                         list(map(getval_tuple, get_positions(1, 1, 323))).count(True) *
                         list(map(getval_tuple, get_positions(3, 1, 323))).count(True) *
                         list(map(getval_tuple, get_positions(5, 1, 323))).count(True) *
                         list(map(getval_tuple, get_positions(7, 1, 323))).count(True) *
                         list(map(getval_tuple, get_positions(1, 2, 323))).count(True)
                         )
