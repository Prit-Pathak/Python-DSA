class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        reversed_number = 0
        while n > 0:
            last_digit = n % 10
            reversed_number = (reversed_number * 10) + last_digit
            n = n // 10
        return reversed_number == x


a = Solution()
print(a.isPalindrome(121))
