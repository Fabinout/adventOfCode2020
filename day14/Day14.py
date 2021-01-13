import unittest
from typing import List

from day14.input_test import test_input


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


def seaport_computation_system(test_input: List[str])-> int:
    mask=Mask('')
    s: str
    mem={}
    for s in test_input:
        if s.startswith('mask'):
            mask = Mask(s.split()[2])
        else:
            index=int(s[4])
            value = int(s.split()[2])
            mem[index] = mask.apply(value)

    return sum(mem.values())



class MyTestCase(unittest.TestCase):

    def test_bitfield(self):
        self.assertEqual(bitfield(11), list('000000000000000000000000000000001011'))

    def test_to_int(self):
        self.assertEqual(11,to_int([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1]))

    def test_something(self):
        mask = Mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        self.assertEqual(mask.apply(11), 73)
        self.assertEqual(mask.apply(101), 101)
        self.assertEqual(mask.apply(0), 64)

    def test_seaport_computation_system(self):
        self.assertEqual(seaport_computation_system(test_input), 165)

if __name__ == '__main__':
    unittest.main()
