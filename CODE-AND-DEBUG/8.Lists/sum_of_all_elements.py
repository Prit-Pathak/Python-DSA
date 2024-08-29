my_list = [4, 5, 6, 7, 8, 9, 100]

sum = 0

# Iterate by value
for i in my_list:
    sum += i
print("ietrate by Value, SUM: ", sum)


# Iterate by index
tota = 0
n = len(my_list)
for i in range(0, n):
    tota += my_list[i]
print("ietrate by index, SUM: ", tota)
