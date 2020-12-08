from dataclasses import dataclass

from day8_python.input_prod_8 import input_prod
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


def generateCommands() -> list:
    lines: list = []
    for string in input_prod:
        lines.append(parse_line(string))
    return lines


commands: list = generateCommands()
running = True
index = 0
acc = 0

while running:
    currentCommand: Command = commands[index]
    print(f'{index=} {acc=} Has the command already run : {currentCommand.has_run}')
    if currentCommand.has_run:
        print(f'command has run')
        break
    else:
        currentCommand.has_run = True
    if currentCommand.command == "acc":
        acc += currentCommand.argument
        index += 1
    else:
        if currentCommand.command == 'jmp':
            index += currentCommand.argument
        else:
            if currentCommand.command == 'nop':
                index += 1
