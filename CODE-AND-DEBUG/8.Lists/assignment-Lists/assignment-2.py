# total count of all even and odd numbers

lst = [4, 8, 6, 5, 3, 12, 1, 3]
even = 0
odd = 0

for item in lst:
    if item % 2 == 0:
        even += 1
    else:
        odd += 1

print("total even num: ", even)
print("total odd num: ", odd)
