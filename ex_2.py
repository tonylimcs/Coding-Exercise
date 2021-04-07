"""
Given a set of single digits (up to 7),
find the number of prime numbers you can find from this input.
Assume positive values and greater than zero.

Example:
Input: {1, 7}
Expected: 3

Note: 7, 17, 71
"""

from itertools import combinations, permutations


def parse(in_):
    ls_ = []
    for ch in in_:
        if ch.isdigit():
            ls_.append(ch)
    return ls_


def check_prime(num):
    is_prime = True

    if num == 1:
        is_prime = False

    if num > 3 \
            and (num % 2 == 0
                 or num % 3 == 0):
        is_prime = False

    return is_prime


if __name__ == '__main__':
    input_ = input('Input: ')
    ls = parse(input_)

    count = 0
    for i in range(0, len(ls)):
        comb = list(combinations(ls, i+1))
        for j in comb:
            perm = list(permutations(j))
            for k in perm:
                int_ = int(''.join(k))
                if check_prime(int_):
                    print(int_)
                    count += 1

    print('Output:', count)
