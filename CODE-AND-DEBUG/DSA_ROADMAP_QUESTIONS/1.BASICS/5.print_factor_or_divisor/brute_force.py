"""
print factors
"""

from typing import List


def count_factor(num: int) -> List:
    res = []
    for i in range(1, num + 1):
        if num % i == 0:
            res.append(i)
    return res


a = count_factor(36)
print(a)
