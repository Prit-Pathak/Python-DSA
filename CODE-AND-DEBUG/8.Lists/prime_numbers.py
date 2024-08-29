# print all the prime numbers
my_lists = [45, 31, 7, 5, 3, 100, 17, 19, 15, 65, 92]


def is_prime(num: int) -> bool:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


# Iterate by value
for item in my_lists:
    if is_prime(item):
        print(item, end=" ")
print()

# iterate by index
n = len(my_lists)
for index in range(0, n):
    if is_prime(my_lists[index]):
        print(my_lists[index], end=" ")

# METHOD 2
# ==================================================================================

print()

for item in my_lists:
    factors = 0
    for i in range(1, item + 1):
        if item % i == 0:
            factors += 1

    if factors == 2:
        print(item, end=" ")
