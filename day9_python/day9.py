from dataclasses import dataclass


@dataclass
class XMASData(object):
    data: list
    pass


def get_preamble(XMAS_data: XMASData, current: int) -> list:
    return XMAS_data.data[current - 5:current]


def get_all_combinations(data: list) -> set:
    combs = []
    for i in data:
        for j in data:
            if i != j:
                combs.append(i * j)
    return set(combs)