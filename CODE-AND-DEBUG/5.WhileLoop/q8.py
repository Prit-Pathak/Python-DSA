"""
start / end -> total of all even number

"""

start = int(input("enter start num: "))
end = int(input("enter end num: "))

i = start
j = end
sum = 0
while i <= j:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)
