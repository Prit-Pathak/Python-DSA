"""
    1
   21
  321
 4321
54321
"""


def pattern(n: int):
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", end=" ")
        for k in range(i, 0, -1):
            print(k, end=" ")
        print()


n = 5
pattern(n)
