# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

from resources.day1.input import input_day1
from resources.day1.inputTests import day1_input_test

input = input_day1
input_test = day1_input_test


def sorted_input(testval: List) -> List:
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    return sorted(testval)


def day_1(input: List) -> int:
    sort_input = sorted_input(input)
    for i, val in enumerate(sort_input):
        for j, val2 in enumerate(sort_input[i + 1:]):
            if val + val2 == 2020:
                print(f'{val=}')
                print(f'{val2=}')
                print(f'résultat : {val2*val=}')
                return val2*val


def day_1_2(input: List) -> int:
    sort_input: List = sorted_input(input)
    for i, val in enumerate(sort_input):
        for j, val2 in enumerate(sort_input[i + 1:]):
            for k, val3 in enumerate(sort_input[i + j + 1:]):
                if val + val2 + val3 == 2020:
                    print(f'{val=}')
                    print(f'{val2=}')
                    print(f'{val3=}')
                    print(f'{val+val2+val3=}')
                    print(f'résultat : {val2*val*val3=}')
                    return val * val2 * val3


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    day_1(input)
    # day_1_2(input)
