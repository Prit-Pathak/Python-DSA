# print total count of all odd numbers

lst = [4, 8, 6, 5, 3, 12, 1, 3]
count = 0

for item in lst:
    if item % 2 != 0:
        count += 1

print(count)
