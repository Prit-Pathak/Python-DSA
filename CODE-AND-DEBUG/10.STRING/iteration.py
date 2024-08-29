a = "Prit"
n = len(a)

# by index
for i in range(n):
    print(a[i], end=" ")

print()
for i in range(n - 1, -1, -1):
    print(a[i], end=" ")

print()

# by value
for char in a:
    print(char, end=" ")

print("llllllllll")

for char in a[::-1]:
    print(char, end=" ")
