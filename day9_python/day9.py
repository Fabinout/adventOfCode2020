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
                combs.append(i + j)
    return set(combs)


def find_first_anomaly(input_test):
    running = True
    i = 5
    xmas_data = XMASData(input_test)
    while running:
        preamble = get_preamble(xmas_data, i)
        possible_values = get_all_combinations(preamble)
        if xmas_data.data[i] in possible_values:
            i += 1
        else:
            running = False
            print(xmas_data.data[i])
            return xmas_data.data[i]
    pass
