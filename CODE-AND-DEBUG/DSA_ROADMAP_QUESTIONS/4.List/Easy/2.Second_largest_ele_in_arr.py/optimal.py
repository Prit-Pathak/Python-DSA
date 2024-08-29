"""
We are using 1 loop only, so TC will be O(N).

Time complexity = O(N) where N is the number of elements in list
Space complexity = O(1)
"""

# In previous solution we tried to do by 2 FOR loops.
# Can we solve this using single for loop? (Single pass solution?)

from typing import List


def getSecondOrderEle(n: int, arr: list) -> list:
    maxi = float("-inf")
    sec_maxi = float("-inf")
    mini = float("inf")
    sec_mini = float("inf")

    for i in range(0, n):
        if arr[i] > maxi:
            sec_maxi = maxi
            maxi = max(maxi, arr[i])
        elif arr[i] > sec_maxi and arr[i] != maxi:
            sec_maxi = arr[i]
        if arr[i] < mini:
            sec_mini = mini
            mini = min(mini, arr[i])
        elif arr[i] < sec_maxi and arr[i] != mini:
            sec_mini = arr[i]

    return [sec_mini, sec_maxi]


arr = [2, 3, 5, 9, 12, 4]
n = len(arr)
print(getSecondOrderEle(n, arr))
