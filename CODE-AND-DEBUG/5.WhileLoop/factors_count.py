def factors_count(num):
    i = 1
    count = 0
    while i <= num // 2:
        if num % i == 0:
            count += 1
        i += 1
    count += 1
    return count


n = int(input())
res = factors_count(n)
print(res)
