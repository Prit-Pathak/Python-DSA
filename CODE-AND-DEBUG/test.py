# def greet():
#     print("greeting")
#     greet()
#     print("done")


# greet()


# def func():
#     global count
#     print(count)
#     count += 1
#     func()


# def func(i, n):
#     if i > n:
#         return
#     print(i)
#     func(i + 1, n)


# def func(i):
#     if i < 1:
#         return
#     print(i)
#     func(i - 1)


# count = 1
# func(5)


# def nat_sum(i, sum):
#     if i < 1:
#         print(sum)
#         return
#     nat_sum(i - 1, sum + i)


# nat_sum(10, 0)


# def sum(num):
#     if num == 1:
#         return 1
#     return num + sum(num - 1)


# x = sum(5)
# print(x)


# lst = [5, 6, 1, 9, 10, 14, 7]
# n = len(lst)

# for i in range(1, n):
#     for j in range(n - 1, i - 1, -1):
#         if lst[j] > lst[j - 1]:
#             lst[j], lst[j - 1] = lst[j - 1], lst[j]

# print(lst)

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
n = len(nums)
for i in range(n - 1, k + 1, -1):
    nums[i], nums[(n - 1) % i] = nums[n % i], nums[i]

print(nums)
