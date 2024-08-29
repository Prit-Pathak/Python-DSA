"""
368 -> factors total
"""


def factors_count(num):
    i = 1
    sum = 0
    while i <= num // 2:
        if num % i == 0:
            sum += i
        i += 1
    sum += num
    return sum


n = int(input())
res = factors_count(n)
print(res)
