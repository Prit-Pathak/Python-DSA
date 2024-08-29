# num = 1


def pattern(n: int):
    for i in range(1, n + 1):
        num = 1
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
            if num > 2:
                num = 1
        print()


# method:-2
def pattern(n: int):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j % 2 == 0:
                print(2, end=" ")
            else:
                print(1, end=" ")
        print()


n = int(input())
pattern(n)
