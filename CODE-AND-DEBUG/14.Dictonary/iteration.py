marks = {
    "history": 78,
    "science": 16,
    "computer": 99,
    "chemistry": 65,
    "sst": 25,
}

# for k in marks:
#     print(k)
#     print(marks[k])
#     print(f"Key = {k}, Value = {marks[k]}")

# total = 0
# for k in marks:
#     total = total + marks[k]

# print(total)

# Print the maximum marks with the subject

max = 0
sub = ""
for k in marks:
    if marks[k] > max:
        max = marks[k]
        sub = k
print(sub, max)
