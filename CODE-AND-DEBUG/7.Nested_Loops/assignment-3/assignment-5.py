"""
    5
   44
  333
 2222
11111
"""


def pattern(n: int):
    for i in range(n, 0, -1):
        for j in range(1, i):
            print(" ", end=" ")
        for k in range(1, n - i + 2):
            print(i, end=" ")
        print()


n = 5
pattern(n)
