def factors_count(num):
    i = 1
    count = 0
    while i <= num // 2:
        if num % i == 0:
            count += 1
        i += 1
    count += 1
    return count


def check_prime(num: int) -> bool:
    fact = factors_count(num)
    if fact == 2:
        return True
    return False


n = int(input())
res = factors_count(n)
prime = check_prime(res)
print(prime)
