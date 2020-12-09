from dataclasses import dataclass


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
