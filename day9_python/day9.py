from dataclasses import dataclass

from typing import List


@dataclass
class XMASData(object):
    data: list
    pass


def get_preamble(XMAS_data: XMASData, current: int, preamble_size: int) -> list:
    return XMAS_data.data[current - preamble_size:current]


def get_all_combinations(data: list) -> set:
    combs = []
    for i in data:
        for j in data:
            if i != j:
                combs.append(i + j)
    return set(combs)


def find_first_anomaly(input_test, preamble_size: int):
    running = True
    i = preamble_size
    xmas_data = XMASData(input_test)
    while running:
        preamble = get_preamble(xmas_data, i, preamble_size)
        possible_values = get_all_combinations(preamble)
        if xmas_data.data[i] in possible_values:
            i += 1
        else:
            running = False
            print(xmas_data.data[i])
            return xmas_data.data[i]
    pass


def get_subsequences_of_size(input_test, size: int) -> list:
    subs = []
    for index in range(0, len(input_test) - size + 1):
        subs.append(input_test[index:index + size])
    return subs


def find_encryption_weakness(input_test: list, invalid_number: int) -> int:
    for i in range(2, len(input_test) - 5):
        sequences: list = get_subsequences_of_size(input_test, i)
        subs: List[int]
        for subs in sequences:
            if sum(subs) == invalid_number:
                return max(subs) + min(subs)
