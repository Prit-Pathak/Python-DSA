# print min number present in the list , without using max function

lst = [5, -8, 10, -15, 2, -4, 95, -34, 25]
n = len(lst)
min = 0

for i in range(1, n - 1, 2):
    for j in range(i + 1, n, 2):
        if lst[i] < lst[j]:
            if lst[i] < min:
                min = lst[i]
            else:
                continue
        else:
            if lst[j] < min:
                min = lst[j]

print(min)
