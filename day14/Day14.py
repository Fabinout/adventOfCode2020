import unittest
from typing import List

from day14.input_test import test_input, test_input2, test_prod, test_input3


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

    def apply2(self, address: int) -> str:
        l = bitfield(address)
        n: List[str] = []
        for index, i in enumerate(list(self.arrays)):
            if i == "0":
                n.append(l[index])
            else:
                if i == "1":
                    n.append("1")
                else:
                    if i == "X":
                        n.append("X")
        return "".join(n)


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


def extract_index(s: str) -> int:
    return int(s.split("[")[1].split(']')[0])


def compute_floatings(m: Mask, address: int) -> List[int]:
    floating_string = m.apply2(address)
    possible_values: List[int] = []
    n = 0
    floating_bits = []
    # print(f'{floating_string}')
    for index, i in enumerate(list(floating_string[::-1])):
        # print(f'{index=};{i=}')
        if "X" == i:
            floating_bits.append(pow(2, index))
        else:
            if "1" == i:
                n += pow(2, index)
    print(f'{n=};{floating_bits=}')
    possible_values.append(n)
    for bit in floating_bits:
        new_possible_values = []
        for numbers in possible_values:
            new_possible_values.append(numbers + bit)
        possible_values = possible_values + new_possible_values

    return possible_values


def seaport_computation_system2(input: str):
    mask = Mask('')
    s: str
    mem = {}
    for s in test_input:
        if s.startswith('mask'):
            mask = Mask(s.split()[2])
        else:
            index = extract_index(s)
            value = int(s.split()[2])
            floatings_values = compute_floatings(mask, value)
            for memory_adress in floatings_values:
                mem[memory_adress] = value

    return sum(mem.values())


class MyTestCase(unittest.TestCase):

    def test_extract_index(self):
        self.assertEqual(80, extract_index("mem[80] = 11"))
        self.assertEqual(85, extract_index("mem[85] = 11"))
        self.assertEqual(8980, extract_index("mem[8980] = 11"))

    def test_compute_floatings(self):
        m = Mask("000000000000000000000000000000X1001X")
        self.assertEqual("000000000000000000000000000000X1101X", m.apply2(42))

        self.assertEqual([26, 27, 58, 59], compute_floatings(m, 42))

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

    def test_seaport_computation_system2(self):
        self.assertEqual(seaport_computation_system2(test_input3), 208)


if __name__ == '__main__':
    unittest.main()
