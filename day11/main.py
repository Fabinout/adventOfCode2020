from enum import Enum
from typing import List
from unittest import TestCase

from day11.input_test import seat_layout_test


class S(Enum):
    EMPTY_SEAT = 1
    FLOOR = 2
    OCCUPIED_SEAT = 3


class Seats(object):

    def __init__(self, seatings) -> None:
        self.seat_values: List[List[int]] = seatings
        self.wide: int = len(seatings[0])
        self.height: int = len(seatings)
        super().__init__()

    def count_occupied_seats(self) -> int:
        total = 0
        for strings in self.seat_values:
            total += strings.count('#')
        return total

    def get_seat(self, x: int, y: int) -> S:
        if x >= self.wide or x < 0 or y >= self.height or y < 0:
            return S.FLOOR
        val = self.seat_values[x][y]
        if val == 'L': return S.EMPTY_SEAT
        if val == '.': return S.FLOOR
        if val == '#': return S.OCCUPIED_SEAT

    def seats_as_string(self) -> str:
        string = ''
        for i in self.seat_values:
            for j in i:
                string += j
            string += "\n"
        return string


def final_count(s: Seats) -> int:
    seats_count = s.count_occupied_seats()
    print(s.seats_as_string())
    print(f'{s.count_occupied_seats()=}')
    next_step = next_seatings(s)
    new_seat_count = next_step.count_occupied_seats()
    if new_seat_count == seats_count and next_step.seats_as_string() == s.seats_as_string():
        print('final_state')
        print(next_step.seats_as_string())
        print(f'{next_step.count_occupied_seats()=}')
        return seats_count
    else:
        return final_count(next_step)


def next_seatings(test_seating: Seats) -> Seats:
    new_seatings = []
    for x in range(0, test_seating.height):
        row = []
        for y in range(0, test_seating.wide):
            if test_seating.get_seat(x, y) == S.FLOOR:
                row.append('.')
            if test_seating.get_seat(x, y) == S.EMPTY_SEAT:
                row.append(case_EMPTY_SEAT(test_seating, x, y))
            if test_seating.get_seat(x, y) == S.OCCUPIED_SEAT:
                row.append(case_OCCUPIED_SEAT(test_seating, x, y))
        new_seatings.append(row)
    new_seating = Seats(new_seatings)

    return new_seating


def case_OCCUPIED_SEAT(test_seating, x, y) -> str:
    occupied_count = 0
    if test_seating.get_seat(x + 1, y - 1) == S.OCCUPIED_SEAT: occupied_count += 1
    if test_seating.get_seat(x + 1, y) == S.OCCUPIED_SEAT: occupied_count += 1
    if test_seating.get_seat(x + 1, y + 1) == S.OCCUPIED_SEAT: occupied_count += 1
    if test_seating.get_seat(x, y - 1) == S.OCCUPIED_SEAT: occupied_count += 1
    if test_seating.get_seat(x, y + 1) == S.OCCUPIED_SEAT: occupied_count += 1
    if test_seating.get_seat(x - 1, y + 1) == S.OCCUPIED_SEAT:  occupied_count += 1
    if test_seating.get_seat(x - 1, y) == S.OCCUPIED_SEAT:  occupied_count += 1
    if test_seating.get_seat(x - 1, y - 1) == S.OCCUPIED_SEAT:  occupied_count += 1
    if occupied_count >= 4:
        return 'L'
    else:
        return '#'


def case_EMPTY_SEAT(test_seating, x, y) -> str:
    occupied_count = 0
    if test_seating.get_seat(x + 1, y - 1) == S.OCCUPIED_SEAT: occupied_count += 1
    if test_seating.get_seat(x + 1, y) == S.OCCUPIED_SEAT: occupied_count += 1
    if test_seating.get_seat(x + 1, y + 1) == S.OCCUPIED_SEAT: occupied_count += 1
    if test_seating.get_seat(x, y - 1) == S.OCCUPIED_SEAT: occupied_count += 1
    if test_seating.get_seat(x, y + 1) == S.OCCUPIED_SEAT: occupied_count += 1
    if test_seating.get_seat(x - 1, y + 1) == S.OCCUPIED_SEAT:  occupied_count += 1
    if test_seating.get_seat(x - 1, y) == S.OCCUPIED_SEAT:  occupied_count += 1
    if test_seating.get_seat(x - 1, y - 1) == S.OCCUPIED_SEAT:  occupied_count += 1
    if test_seating.get_seat(x + 1, y - 1) == S.OCCUPIED_SEAT:  occupied_count += 1
    if occupied_count == 0:
        return '#'
    else:
        return 'L'


class MyTestCase(TestCase):
    def test_something(self):
        test_seating = Seats(seat_layout_test)
        self.assertEqual(test_seating.get_seat(0, 0), S.EMPTY_SEAT)
        self.assertEqual(test_seating.get_seat(1, 1), S.EMPTY_SEAT)
        self.assertEqual(test_seating.get_seat(1, 0), S.EMPTY_SEAT)
        self.assertEqual(test_seating.get_seat(0, 1), S.FLOOR)
        self.assertEqual(test_seating.get_seat(10, 0), S.FLOOR)

    def test_count(self):
        test_seating = Seats(seat_layout_test)
        expected_seating = Seats([
            "#.##.##.##",
            "#######.##",
            "#.#.#..#..",
            "####.##.##",
            "#.##.##.##",
            "#.#####.##",
            "..#.#.....",
            "##########",
            "#.######.#",
            "#.#####.##"
        ])
        self.assertEqual(expected_seating.count_occupied_seats(), 71)

    def test_nextstep(self):
        test_seating = Seats(seat_layout_test)
        expected_seating = Seats([
            "#.##.##.##",
            "#######.##",
            "#.#.#..#..",
            "####.##.##",
            "#.##.##.##",
            "#.#####.##",
            "..#.#.....",
            "##########",
            "#.######.#",
            "#.#####.##"
        ])
        seating_2 = next_seatings(test_seating)
        self.assertEqual(seating_2.seats_as_string(), expected_seating.seats_as_string())

    def test_step2(self):
        test_seating = Seats([
            "#.##.##.##",
            "#######.##",
            "#.#.#..#..",
            "####.##.##",
            "#.##.##.##",
            "#.#####.##",
            "..#.#.....",
            "##########",
            "#.######.#",
            "#.#####.##"
        ])
        expected_seatings = Seats([
            "#.LL.L#.##",
            "#LLLLLL.L#",
            "L.L.L..L..",
            "#LLL.LL.L#",
            "#.LL.LL.LL",
            "#.LLLL#.##",
            "..L.L.....",
            "#LLLLLLLL#",
            "#.LLLLLL.L",
            "#.#LLLL.##"
        ])
        seating_2 = next_seatings(test_seating)
        self.assertEqual(expected_seatings.seats_as_string(), seating_2.seats_as_string())

    def test_step3(self):
        test_seating = Seats(seat_layout_test)
        self.assertEqual(final_count(test_seating), 37)
