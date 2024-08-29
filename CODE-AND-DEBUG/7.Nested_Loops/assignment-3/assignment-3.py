"""
    5
   54
  543
 5432
54321
"""


def pattern(n: int):
    for i in range(n, 0, -1):
        for j in range(1, i):
            print(" ", end=" ")
        for k in range(n, i - 1, -1):
            print(k, end=" ")
        print()


n = 5
pattern(n)
