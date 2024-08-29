"""
5674
10983


1. How many numbers are divisible by 7?             -> 759
2. How many numbers are divisible by both 2 and 7?  -> 379
"""

start = 5674
end = 10983

i = start
j = end
count = 0
count1 = 0
while i <= j:
    if i % 7 == 0:
        count += 1
    if i % 2 == 0 and i % 7 == 0:
        count1 += 1

    i += 1
print(count)
print(count1)
