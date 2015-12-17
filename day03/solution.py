#!/usr/bin/env python3

"""
Advent of Code
Day 3
Solution
"""

import os

class Grid:
    """Representation of a two-dimensional grid."""
    def __init__(self):
        self._current_position = (0, 0)
        self._visited_locations = {self._current_position}
    def move(self, direction):
        """Set new current location after moving in the given direction."""
        row, col = self._current_position
        self._current_position = {
            '^': (row, col + 1),
            'v': (row, col - 1),
            '<': (row - 1, col),
            '>': (row + 1, col)
        }.get(direction)
        self._visited_locations.add(self._current_position)
    def visited_locations(self):
        """Return number of visited locations."""
        return self._visited_locations

def is_santas_turn(turn):
    """Check if the given turn corresponds to Santa."""
    return turn % 2 == 0

def solve():
    """Solve the puzzle."""
    filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    santa_alone_grid = Grid()
    santa_grid = Grid()
    robo_santa_grid = Grid()

    with open(filename) as file:
        for turn, direction in enumerate(file.read()):
            santa_alone_grid.move(direction)
            if is_santas_turn(turn):
                santa_grid.move(direction)
            else:
                robo_santa_grid.move(direction)

    santa_alone_visited_locations = santa_alone_grid.visited_locations()
    print("The first year, {0} houses receive at least one present.".\
    format(len(santa_alone_visited_locations)))

    santa_visited_locations = santa_grid.visited_locations()
    robo_santa_visited_locations = robo_santa_grid.visited_locations()
    all_visited_locations = santa_visited_locations.union(robo_santa_visited_locations)
    print("The second year, {0} houses receive at least one present.".\
    format(len(all_visited_locations)))

if __name__ == '__main__':
    solve()
