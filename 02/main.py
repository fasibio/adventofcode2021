from enum import Enum
from typing import List


class Direction(Enum):
    forward = "forward"
    down = "down"
    up = "up"


class Command:
    direction: Direction
    steps: str

    def __init__(self, line: str):
        data = line.split(" ")
        self.direction = Direction(data[0])
        self.steps = data[1]


def loadFile(fileName):
    return open(fileName, "r").read()


def getDestinationPosition(way: list[Command]):
    x = 0
    y = 0
    for command in way:
        if command.direction == Direction.forward:
            x += int(command.steps)
        elif command.direction == Direction.down:
            y += int(command.steps)
        elif command.direction == Direction.up:
            y -= int(command.steps)
    return (x, y)


def getDestinationPositionStep2(way: list[Command]):
    x = 0
    y = 0
    aim = 0
    for command in way:
        if command.direction == Direction.forward:
            x += int(command.steps)
            y += aim * int(command.steps)
        elif command.direction == Direction.down:
            aim += int(command.steps)
        elif command.direction == Direction.up:
            aim -= int(command.steps)
    return (x, y)


filelines = loadFile("input.txt").split("\n")

commands: List[Command] = []

for line in filelines:
    if line != "":
        commands.append(Command(line))


x, y = getDestinationPosition(commands)
print("step1:", x, y, x*y)

x, y = getDestinationPositionStep2(commands)
print("step2:", x, y, x*y)
