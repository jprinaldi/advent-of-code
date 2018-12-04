#!/usr/bin/env python3

"""
Advent of Code
Day 4
Solution
"""

from hashlib import md5

def has_n_leading_zeroes(num_zeroes, digest):
    """Check if the given digest has the required number of leading zeroes."""
    return digest[:num_zeroes] == '0'*num_zeroes

def find_mystery_number(secret_key, num_zeroes, initial_candidate):
    """
    Return the smallest positive number >= initial_candidate for which,
    when preceded by the given secret_key,
    produces an MD5 hash with num_zeroes leading zeroes.
    """
    mystery_number = None
    candidate = initial_candidate
    while not mystery_number:
        hash_input = (secret_key + str(candidate)).encode('utf-8')
        digest = md5(hash_input).hexdigest()
        if has_n_leading_zeroes(num_zeroes, digest):
            mystery_number = candidate
        else:
            candidate += 1
    return int(mystery_number)

def solve():
    """Solve the puzzle."""
    secret_key = 'bgvyzdsv'
    first_mystery_number = find_mystery_number(secret_key, 5, 1)
    print("The first mystery number is {0}.".format(first_mystery_number))
    second_mystery_number = find_mystery_number(secret_key, 6, first_mystery_number)
    print("The second mystery number is {0}.".format(second_mystery_number))

if __name__ == '__main__':
    solve()
