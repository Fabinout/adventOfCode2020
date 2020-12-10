from unittest import TestCase

from day10.input_test import adapters_test
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
