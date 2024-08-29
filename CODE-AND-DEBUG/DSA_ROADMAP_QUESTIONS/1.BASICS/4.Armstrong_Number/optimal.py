import math


class Solution:
    def armstrongNumber(self, n):

        # code here
        res = 0
        N = n
        nod = int(math.log10(N)) + 1
        while N:
            lst_digit = N % 10
            res = res + lst_digit**nod  # nod-> number of digits
            N = N // 10
        if n < 100 or n > 1000:
            return 0
        return res == n
