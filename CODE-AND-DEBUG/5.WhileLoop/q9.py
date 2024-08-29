# 1 to 10, count how many even numbers

start = int(input("enter start num: "))
end = int(input("enter end num: "))

i = start
j = end
count = 0
while i <= j:
    if i % 2 == 0:
        count += 1
    i += 1

print(count)
