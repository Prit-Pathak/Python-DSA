def factors(num):
    i = 1
    fact = []
    while i <= num:
        if num % i == 0:
            fact.append(i)
        i += 1
    return fact


def factors_method_2(num):
    i = 1
    fact = []
    while i <= num // 2:
        if num % i == 0:
            fact.append(i)
        i += 1
    fact.append(num)
    return fact


n = int(input())
m = int(input())
res = factors(n)
print(res)
res1 = factors_method_2(m)
print(res1)
