from unittest import TestCase

from day10.RealInput import input_prod
from day10.input_test import adapters_test, adapters_test_2
from day10.main import JoltageAdapters


class MyTestCase(TestCase):
    def test_something(self):
        device = JoltageAdapters(adapters_test)
        self.assertEqual(device.device_max_joltage, 22)

    def test_sorted(self):
        device = JoltageAdapters(adapters_test)
        self.assertEqual(device.values, [
        1,
        4,
        5,
        6,
        7,
        10,
        11,
        12,
        15,
        16,
        19
        ])

    def test_deltas(self):
        device = JoltageAdapters(adapters_test)
        self.assertEqual(device.difference_3, 5)
        self.assertEqual(device.difference_1, 7)

        self.assertEqual(device.result, 35)

    def test_deltas_2(self):
        device = JoltageAdapters(adapters_test_2)
        self.assertEqual(device.difference_3, 10)
        self.assertEqual(device.difference_1, 22)

        self.assertEqual(device.result, 220)

    def test_result_real_case(self):
        device = JoltageAdapters(input_prod)
        self.assertEqual(device.difference_3, 39)
        self.assertEqual(device.difference_1, 66)

        self.assertEqual(device.result, 2574)