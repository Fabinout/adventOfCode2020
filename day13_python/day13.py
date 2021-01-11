import unittest

from day13_python.inputs import test_inputs


def filter_list(my_input):
    return list(filter(lambda bus_id: bus_id != "x", my_input[1]))


def is_a_multiple_(param: int, param1: int) -> bool:
    return param % param1 == 0


class MyTestCase(unittest.TestCase):

    def test_filter_lambda(self):
        my_input = test_inputs
        newlist = filter_list(my_input)
        self.assertEqual(newlist, ["7", "13", "59", "31", "19"])

    def test_is_a_multiple(self):
        self.assertEqual(is_a_multiple_(944, 59), True)
        self.assertEqual(is_a_multiple_(944, 7), False)
        self.assertEqual(is_a_multiple_(945, 7), True)
        self.assertEqual(is_a_multiple_(945, 59), False)

