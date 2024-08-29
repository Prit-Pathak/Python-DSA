"""
prime number
"""

from typing import List
import math


def is_prime(num: int) -> bool:
    res = []
    for i in range(1, int(math.sqrt(num) + 1)):
        if num % i == 0:
            res.append(i)
            if num // i != i:
                res.append(num // i)
    if len(res) == 2:
        return True
    return False


a = is_prime(17)
print(a)
