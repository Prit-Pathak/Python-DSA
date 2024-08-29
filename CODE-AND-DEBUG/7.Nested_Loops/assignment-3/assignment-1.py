"""
    1
   12
  123
 1234
12345
"""


def pattern(n: int):
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", end=" ")
        for k in range(1, i + 1):
            print(k, end=" ")
        print()


n = 5
pattern(5)
