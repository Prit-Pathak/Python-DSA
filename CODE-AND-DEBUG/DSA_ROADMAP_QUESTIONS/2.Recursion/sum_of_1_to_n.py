# Parameterized Way
def natsum(i, sum):
    if i < 1:
        print(sum)
        return
    return natsum(i - 1, sum + i)


# Functional way


def natsum1(num):
    if num == 1:
        return 1
    return num + natsum1(num - 1)


if __name__ == "__main__":
    natsum(5, 0)
    print(natsum1(4))
