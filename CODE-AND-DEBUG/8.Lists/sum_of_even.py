# print the sum of all even numbers
my_list = [4, 5, 6, 7, 8, 9, 100]

# Iterate by value
sum = 0
for i in my_list:
    if i % 2 == 0:
        sum += i
print("sum of even num: ", sum)

# Iterate by index
total = 0
n = len(my_list)
for i in range(0, n):
    if my_list[i] % 2 == 0:
        total += my_list[i]
print("sum of even num: ", total)
