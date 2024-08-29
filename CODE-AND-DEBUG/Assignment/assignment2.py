# 1. Write a program that takes two numbers as input and checks if the first
# number is divisible by the second
# num1 = int(input("enetr first num:"))
# num2 = int(input("enetr second num:"))

# if num1 != 0 and num1 % num2 == 0:
#     print(f"{num1} divisible by {num2}")
# else:
#     print(f"{num1} not divisible {num2}")


# 2. A student will not be allowed to sit in exam if his/her attendance is less
# than 75%.
# Take following input from user
#  Number of classes held
#  Number of classes attended.
#   1. Print percentage of class attended
#   2. Print Is student is allowed to sit in exam or not.
# total_classes = int(input("enter total number of classes: "))
# classes_attend = int(input("enter number of classes attended: "))

# req_att = total_classes * 0.75

# att_per = (classes_attend * 100) / total_classes

# print(f"percentage of class attended is {att_per}")

# if att_per >= req_att:
#     print("student is allowed to sit in exam")
# else:
#     print("not allowed")

# Q3. Write a program to check if number is divisible by 2 and 3 but not 8.
# num = int(input("enter the number: "))
# if num % 2 == 0 and num % 3 == 0 and num % 8 != 0:
#     print(f"{num} is divisible by 2 and 3 but not 8")
# else:
#     print("invalid")

# 4. Write a Python program that takes a student's score as input and
# prints the corresponding grade. Use the following grading scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
# complted in class (if else .py)

# 5. Write a program to calculate bill. Ask the final amount from the user.
# You have to give discount and print the final bill after discount.
# 50000 above - 30% discount
# 40000 - 49999 - 25% discount
# 30000 - 39999 - 20% discount
# 10000 - 29999 - 10% discount
# 1 - 9999 - No discount
# Print the discount and the final amount to be paid.
# Example 1
# Enter bill amount = 80000
# You got 30% discount
# Your final bill is Rs. 56000

# bill = int(input("enter the bill: "))

# if bill >= 50000:
#     print("You got 30% discount")
#     fin_bill = bill - bill * 0.3
#     print(f"our final bill is Rs. {fin_bill}")

# if bill >= 40000 and bill < 50000:
#     print("You got 25% discount")
#     fin_bill = bill - bill * 0.25
#     print(f"our final bill is Rs. {fin_bill}")

# if bill >= 30000 and bill < 40000:
#     print("You got 20% discount")
#     fin_bill = bill - bill * 0.2
#     print(f"our final bill is Rs. {fin_bill}")

# if bill >= 10000 and bill < 30000:
#     print("You got 10% discount")
#     fin_bill = bill - bill * 0.1
#     print(f"our final bill is Rs. {fin_bill}")

# if bill > 0 and bill < 10000:
#     print("No discount")
#     fin_bill = bill
#     print(f"our final bill is Rs. {fin_bill}")

# Q6. Ask 4 numbers from user. Make sure all the numbers entered by user
# are different. Print which number is the smallest.
# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))
# num3 = int(input("enter num3: "))
# num4 = int(input("enter num4: "))

# if num1 < num2 and num1 < num3 and num1 < num4:
#     smallest = num1
# elif num2 < num1 and num2 < num3 and num2 < num4:
#     smallest = num2
# elif num3 < num2 and num3 < num1 and num3 < num4:
#     smallest = num3
# else:
#     smallest = num4

# print(f"smallest number is {smallest}")

# 7. Take Salary as input from User and Update the salary of an employee.
# salary less than 10,000, 5 % increment
# salary between 10,000 and 20, 000, 10 % increment
# salary between 20,000 and 50,000, 15 % increment
# salary more than 50,000, 20 % increment

# salary = int(input("enter the salary"))

# if salary < 10000:
#     print("you got 5 % increment")
# if salary >= 10000 and salary < 20000:
#     print("you got 10 % increment")
# if salary >= 20000 and salary < 50000:
#     print("you got 15 % increment")
# if salary >= 50000:
#     print("you got 20 % increment")

# Q8. An extra day is added to the calendar almost every four years as
# February 29, and the day is called a leap day. A leap year contains a leap
# day.
# These are the conditions used to identify leap years:
# if the year can be evenly divided by 4, it is then a leap year
# but if the year is evenly divided by 4 and also by 100, then it is NOT a
# leap year
# but if the year is evenly divided by 4 and also by 400, then it is a leap
# year
# This means the years 2000 and 2400 are leap years, while 1800, 1900,
# 2100, 2200, 2300 and 2500 are NOT leap years.
# Ask a year input from user. And tell if the year entered by user is leap or
# not.

# year = int(input("enter the year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("leap year")
# else:
#     print("not a leap year")


# num = int(input())

# if num < 0:
#     num = -num
#     print(num)
# else:
#     print(num)


n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 < n2 and n1 < n3:
    smallest = n1
if n2 < n1 and n2 < n3:
    smallest = n2
else:
    smallest = n3


if n1 > n2 and n1 > n3:
    great = n1
if n2 > 1 and n2 > n3:
    great = n2
else:
    great = n3

print(smallest, great)
