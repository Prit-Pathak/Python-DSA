my_list = [4, 5, 6, 7, 8, 9, 100]
n = len(my_list)

sum = 0
for i in range(0, n):
    if i % 2 != 0:
        sum += my_list[i]
print(sum)
