"""
    5
   45
  345
 2345
12345
"""


def pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i):
            print(" ", end=" ")
        for k in range(i, n + 1):
            print(k, end=" ")
        print()


n = 5
pattern(n)
