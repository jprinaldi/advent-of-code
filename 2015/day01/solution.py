#!/usr/bin/env python3

"""
Advent of Code
Day 1
Solution
"""

import os

def get_displacement(instruction):
    """Return floor displacement given instruction."""
    if instruction == '(':
        return 1
    elif instruction == ')':
        return -1
    else:
        return 0

def solve():
    """Solve the puzzle."""
    filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    current_floor = 0
    basement = -1
    position = None
    with open(filename) as file:
        for index, char in enumerate(file.read()):
            current_floor += get_displacement(char)
            if not position and current_floor == basement:
                position = index + 1
    print("The instructions take Santa to the {0} floor.".format(current_floor))
    print("The position of the character that causes Santa to first enter the basement is {0}.".format(position))

if __name__ == '__main__':
    solve()
