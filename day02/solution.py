#!/usr/bin/env python3

"""
Advent of Code
Day 2
Solution
"""

import operator
import os
from functools import reduce
from itertools import combinations

class Box:
    """Implementation of a perfect right rectangular prism."""
    def __init__(self, dimensions):
        self.dimensions = dimensions
    def faces_perimeters(self):
        """Return the perimeters of the faces."""
        return [2*sum(x) for x in combinations(self.dimensions, 2)]
    def faces_areas(self):
        """Return the areas of the faces."""
        return [reduce(operator.mul, x) for x in combinations(self.dimensions, 2)]
    def surface_area(self):
        """Return the total surface area."""
        return 2*sum([face for face in self.faces_areas()])
    def volume(self):
        """Return the volume."""
        return reduce(operator.mul, self.dimensions)
    def smallest_face_perimeter(self):
        """Return the shortest face perimeter."""
        return min(self.faces_perimeters())
    def smallest_face_area(self):
        """Return the smallest face area."""
        return min(self.faces_areas())

def solve():
    """Solve the puzzle."""
    filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    needed_paper = 0
    needed_ribbon = 0
    with open(filename) as file:
        for line in file:
            dimensions = [int(d) for d in line.rstrip().split("x")]
            box = Box(dimensions)
            needed_paper += box.surface_area() + box.smallest_face_area()
            needed_ribbon += box.smallest_face_perimeter() + box.volume()
    print("The elves should order {0} square feet of wrapping paper.".format(needed_paper))
    print("The elves should order {0} feet of ribbon.".format(needed_ribbon))

if __name__ == '__main__':
    solve()
