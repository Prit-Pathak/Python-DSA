"""
    1
   21
  321
 4321
54321
 4321
  321
   21
    1
"""


def pattern(n: int):
    for i in range(1, (n // 2) + 2):
        for j in range(1, ((n // 2) + 1) - i + 1):
            print(" ", end=" ")
        for k in range(i, 0, -1):
            print(k, end=" ")
        print()
    for i in range((n // 2), 0, -1):
        for j in range(1, ((n // 2) + 1) - i + 1):
            print(" ", end=" ")
        for k in range(i, 0, -1):
            print(k, end=" ")
        print()


n = 9
pattern(n)
