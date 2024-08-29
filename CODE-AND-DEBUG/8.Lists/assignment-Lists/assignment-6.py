# print all numbers divisible by 5 but in reverse order
lst = [4, 10, 6, 5, 3, 15, 1, 25, 125]

res = []

for item in lst:
    if item % 5 == 0:
        res.append(item)

n = len(res)

for i in range(n - 1, -1, -1):
    print(res[i], end=" ")
