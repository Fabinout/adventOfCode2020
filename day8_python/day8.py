from dataclasses import dataclass
from typing import List

from day8_python.input_test import input_test


@dataclass
class Command(object):
    command: str
    argument: int
    has_run = False
    pass


def parse_line(line: str) -> Command:
    command = line.split()[0]
    arg = int(line.split()[1])
    return Command(command, arg)


def generate_commands() -> list:
    lines: list = []
    for string in input_test:
        lines.append(parse_line(string))
    return lines


def run_commands(commands: List[Command]) -> bool:
    running = True
    index = 0
    acc = 0
    while running:
        if index == len(commands):
            print(f'TROUVE!! {acc=}')
            return True
        current_command: Command = commands[index]
        if current_command.has_run:
            print(f'{index=} {acc=}')
            print(f'boucle infinie')
            return False
        else:
            current_command.has_run = True
        if current_command.command == "acc":
            acc += current_command.argument
            index += 1
        else:
            if current_command.command == 'jmp':
                index += current_command.argument
            else:
                if current_command.command == 'nop':
                    index += 1


def switch(c: Command) -> Command:
    if c.command == 'jmp':
        return Command("nop", c.argument)
    if c.command == 'nop':
        return Command('jmp', c.argument)
    return c


commands: list = generate_commands()
print(f'{commands=}')
print(f'{len(commands)=}')

i: int


def switch_one_and_reset(l: List[Command]) -> List[Command]:
    modified_list = l[0:i] + [switch(l[i])] + l[i + 1:len(l)]
    for item in modified_list:
        item.has_run = False
    return modified_list


for i in range(0, len(commands) - 1):
    # print(f'{commands[0:i]=}')
    # print(f'{i=}:{switch(commands[i])=}')
    # print(f'{commands[i+1:len(commands)]=}')

    new_list_of_commands = switch_one_and_reset(commands)

    # print(f'{modified_list=}')
    # print(f'{len(modified_list)=}')
    if run_commands(new_list_of_commands): break

