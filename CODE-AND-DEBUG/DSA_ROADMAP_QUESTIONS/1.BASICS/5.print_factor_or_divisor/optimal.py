"""
print factors
"""

from typing import List
import math


def count_factor(num: int) -> List:
    res = []
    for i in range(1, int(math.sqrt(num) + 1)):
        if num % i == 0:
            res.append(i)
            if num // i != i:
                res.append(num // i)
    res.sort()
    return res


a = count_factor(36)
print(a)
