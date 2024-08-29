# print sum and product of all elements in the lists.

lst = [4, 8, 6, 5, 3, 12, 1, 3]

sum = 0
prod = 1

for item in lst:
    sum += item
    prod *= item

print("sum: ", sum)
print("product: ", prod)
