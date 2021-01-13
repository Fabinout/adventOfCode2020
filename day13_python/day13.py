import unittest

from day13_python.inputs import test_inputs, real_inputs


def is_a_multiple_(param: int, param1: int) -> bool:
    return param % param1 == 0


def find_first_minute(test_inputs):
    minute = 0
    step = 1
    while True:
        subsequent_departure = True
        for (index, i) in enumerate(test_inputs[1]):
            if i != "x":
                i_int = int(i)
                if not (is_a_multiple_(minute + index, i_int)):
                    subsequent_departure = False
                    break
                else:
                    if not is_a_multiple_(step, i_int):
                        step *= i_int
        if subsequent_departure:
            return minute
        else:
            minute = minute + step
    pass


class MyTestCase(unittest.TestCase):

    def test_is_a_multiple(self):
        self.assertEqual(is_a_multiple_(944, 59), True)
        self.assertEqual(is_a_multiple_(944, 7), False)
        self.assertEqual(is_a_multiple_(945, 7), True)
        self.assertEqual(is_a_multiple_(945, 59), False)

    def test_find_first_bus(self):
        self.assertEqual(find_first_minute(test_inputs), 1068781)
        self.assertEqual(find_first_minute(real_inputs), 725169163285238)
