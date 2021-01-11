import unittest
from enum import Enum, auto
from typing import Tuple

from day12.inputs import input_test, input_real_data


def extract_argument(param) -> int:
    return int(param[1:])


class C(Enum):
    FRONT = auto()
    LEFT = auto()
    RIGHT = auto()
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()
    pass


def extract_command(param) -> C:
    if param[0] == 'N': return C.NORTH
    if param[0] == 'S': return C.SOUTH
    if param[0] == 'E': return C.EAST
    if param[0] == 'W': return C.WEST
    if param[0] == 'F': return C.FRONT
    if param[0] == 'L': return C.LEFT
    if param[0] == 'R': return C.RIGHT
    return C.FRONT


def parse(param: str) -> Tuple:
    command = extract_command(param)
    argument = extract_argument(param)
    return command, argument


def avancer(position, arg) -> Tuple:
    x = position[1]
    y = position[2]
    waypoint_x = position[3]
    waypoint_y = position[4]
    vect_x = waypoint_x - x
    vect_y = waypoint_y - y
    x = x + vect_x * arg
    waypoint_x = waypoint_x + vect_x * arg
    y = y + vect_y * arg
    waypoint_y = waypoint_y + vect_y * arg

    return position[0], x, y, waypoint_x, waypoint_y


def rotate_left(position, arg) -> Tuple:
    direction = position[0]
    x = position[1]
    y = position[2]
    waypoint_x = position[3]
    waypoint_y = position[4]
    vect_x = waypoint_x - x
    vect_y = waypoint_y - y
    waypoint_x = x - vect_y
    waypoint_y = y + vect_x

    if arg == 90:
        return direction, position[1], position[2], waypoint_x, waypoint_y
    else:
        return rotate_left((direction, position[1], position[2], waypoint_x, waypoint_y), arg - 90)


def rotate_right(position, arg) -> Tuple:
    direction = position[0]
    x = position[1]
    y = position[2]
    waypoint_x = position[3]
    waypoint_y = position[4]
    vect_x = waypoint_x - x
    vect_y = waypoint_y - y
    waypoint_x = x + vect_y
    waypoint_y = y - vect_x

    if arg == 90:
        return direction, position[1], position[2], waypoint_x, waypoint_y
    else:
        return rotate_right((direction, position[1], position[2], waypoint_x, waypoint_y), arg - 90)


def final_destination(input_test):
    position = (C.EAST, 0, 0, 10, 1)
    for i in input_test:
        (co, arg) = parse(i)
        if co == C.FRONT:
            position = avancer(position, arg)
        if co == C.LEFT:
            position = rotate_left(position, arg)
        if co == C.RIGHT:
            position = rotate_right(position, arg)
        if co == C.NORTH:
            position = (position[0], position[1], position[2], position[3], position[4] + arg)
        if co == C.SOUTH:
            position = (position[0], position[1], position[2], position[3], position[4] - arg)
        if co == C.WEST:
            position = (position[0], position[1], position[2], position[3] - arg, position[4])
        if co == C.EAST:
            position = (position[0], position[1], position[2], position[3] + arg, position[4])

        print(f'{position=}')

    return position[1], position[2]


def manhatan_distance(input_test) -> int:
    dest = final_destination(input_test)

    return abs(dest[0]) + abs(dest[1])


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(parse(input_test[0]), (C.FRONT, 10))
        self.assertEqual(parse(input_test[1]), (C.NORTH, 3))
        self.assertEqual(parse(input_test[2]), (C.FRONT, 7))
        self.assertEqual(parse(input_test[3]), (C.RIGHT, 90))
        self.assertEqual(parse(input_test[4]), (C.FRONT, 11))

    def test_itinary_test(self):
        self.assertEqual(final_destination(input_test), (214, -72))

    def test_manhatan_distance(self):
        self.assertEqual(manhatan_distance(input_test), 286)

    def test_movement(self):
        self.assertEqual(final_destination(["F10"]), (100, 10))
        self.assertEqual(final_destination(["F10", "N3"]), (100, 10))
        self.assertEqual(final_destination(["F10", "N3", "F7"]), (170, 38))
        self.assertEqual(final_destination(["F10", "N3", "F7", "R90"]), (170, 38))
        self.assertEqual(final_destination(["F10", "N3", "F7", "R90", "F11"]), (214, -72))


    def test_manhatan_distance_with_real_input(self):
        self.assertEqual(manhatan_distance(input_real_data), 38693)


if __name__ == '__main__':
    unittest.main()
