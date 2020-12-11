import unittest
from enum import Enum, auto


class S(Enum):
    EMPTY_SEAT = 1
    FLOOR = 2
    OCCUPIED_SEAT = 3


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertNotEqual(S.EMPTY_SEAT, S.OCCUPIED_SEAT)
        self.assertFalse(S.EMPTY_SEAT == S.OCCUPIED_SEAT)

if __name__ == '__main__':
    unittest.main()
