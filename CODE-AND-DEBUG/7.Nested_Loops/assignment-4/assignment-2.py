"""
1
12
123
1234
12345
1234
123
12
1
"""


def pattern(n: int):
    for i in range(1, (n // 2) + 2):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for i in range((n // 2), 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


n = 9
pattern(n)
