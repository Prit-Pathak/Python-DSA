# print the Prime numbers in that list

lst = [11, 8, 6, 5, 3, 19, 1, 17]

for item in lst:
    factor = 0
    for i in range(1, item + 1):
        if item % i == 0:
            factor += 1
    if factor == 2:
        print(item, end=" ")
