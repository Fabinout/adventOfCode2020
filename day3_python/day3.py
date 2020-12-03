from day3_python.input import input_real_case

input_prod = input_real_case


def getVal(x: int, y: int) -> bool:
    # print(f'{x=};{y=}')
    return input_prod[y][x] == "#"


def getval_tuple(t: tuple) -> bool:
    return getVal(t[0], t[1])


def get_positions(dx: int, dy: int, lines: int) -> list:
    list = [(0, 0)]
    while list[-1][1] < lines - 1:
        x = list[-1][0]
        y = list[-1][1]
        list.append((x + dx, y + dy))
    return list
