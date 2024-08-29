"""
5
45
345
2345
12345
2345
345
45
5
"""


def pattern(n: int):
    for i in range((n // 2) + 1, 0, -1):
        for j in range(i, (n // 2) + 2):
            print(j, end=" ")
        print()

    for i in range(2, (n // 2) + 2):
        for j in range(i, (n // 2) + 2):
            print(j, end=" ")
        print()


n = 9
pattern(n)
