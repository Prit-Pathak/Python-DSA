from typing import List

"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(n)
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        freq = {i: 0 for i in range(0, len(nums) + 1)}
        for i in nums:
            freq[i] += 1
        for k, v in freq.items():
            if v == 0:
                return k


# method II -> self tried and tested -> successfull
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        has_lst = [0] * (n + 1)
        for ele in nums:
            has_lst[ele] += 1

        for i in range(len(has_lst)):
            if has_lst[i] == 0:
                return i
        return -1
