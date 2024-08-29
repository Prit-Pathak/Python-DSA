"""
start 5
end 26

1. start to end, total of all numbers (5+6+7+8...25+26)
2. start to end, total of all numbers divisible by 7
"""

# 1.
# start = int(input("enter start number: "))
# end = int(input("enter end number: "))
# sum = 0
# for i in range(start, end + 1):
#     sum += i
#     print(sum, end=" ")

# print()
# 2.Answer

start = int(input("enter start number: "))
end = int(input("enter end number: "))
sum = 0

for i in range(start, end):
    if i % 7 == 0:
        sum += i
        print(sum, end=" ")
