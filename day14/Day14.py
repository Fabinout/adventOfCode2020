import unittest
from typing import List

from day14.input_test import test_input, test_input2, test_prod


def to_int(n: List[int]) -> int:
    out = 0
    for bit in n:
        out = (out << 1) | bit
    return out


class Mask(object):

    def __init__(self, value: str) -> None:
        self.arrays = list(value)
        super().__init__()

    def apply(self, param: int) -> int:
        l = bitfield(param)
        n = []
        for index, i in enumerate(self.arrays):
            mask_value = i
            if mask_value == 'X':
                n.append(int(l[index]))
            else:
                n.append(int(mask_value))
        out = to_int(n)
        return out


def bitfield(n) -> List:
    return list(format(n, '036b'))


def seaport_computation_system(test_input: List[str]) -> int:
    mask = Mask('')
    s: str
    mem = {}
    for s in test_input:
        if s.startswith('mask'):
            mask = Mask(s.split()[2])
        else:
            index = extract_index(s)
            value = int(s.split()[2])
            mem[index] = mask.apply(value)

    return sum(mem.values())


def extract_index(s: str)-> int:
    return int(s.split("[")[1].split(']')[0])


class MyTestCase(unittest.TestCase):

    def test_extract_index(self):
        self.assertEqual(80, extract_index("mem[80] = 11"))
        self.assertEqual(85, extract_index("mem[85] = 11"))
        self.assertEqual(8980, extract_index("mem[8980] = 11"))

    def test_bitfield(self):
        self.assertEqual(bitfield(11), list('000000000000000000000000000000001011'))

    def test_to_int(self):
        self.assertEqual(11, to_int(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1,
             1]))

    def test_something(self):
        mask = Mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        self.assertEqual(mask.apply(11), 73)
        self.assertEqual(mask.apply(101), 101)
        self.assertEqual(mask.apply(0), 64)

    def test_seaport_computation_system(self):
        self.assertEqual(seaport_computation_system(test_input), 165)
        self.assertEqual(seaport_computation_system(test_input2), 238)
        self.assertEqual(165, seaport_computation_system(test_prod))


if __name__ == '__main__':
    unittest.main()
