"""
ask a start num from user ->6
ask a end num from user ->15
print -> 6,7,8,.....,14,15

ask a start num from user ->15
ask a end num from user ->8
print -> 8,.....,14,15
"""

strt = int(input("enter start num: "))
end = int(input("enter end num: "))

# i = n1
# j = n2

# while j <= i:
#     print(j, end=" ")
#     j += 1

# while i <= j:
#     print(i, end=" ")
#     i += 1

# method 2

if strt < end:
    i = strt
    j = end
    while i < j:
        print(i, end=" ")
        i += 1
else:
    i = end
    j = strt
    while i < j:
        print(i, end=" ")
        i += 1
