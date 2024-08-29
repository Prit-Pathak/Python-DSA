# Brute force approach
class Solution:
    def count_digit(self, N):
        # code here
        n1 = N
        count = 0
        while N:
            count += 1
            N = N // 10

        return count


a = Solution()
print(a.count_digit(123))
