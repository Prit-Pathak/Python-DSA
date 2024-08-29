# Q1. There are two variables.
# a=5
# b=10
# What will be the output of following:
# a >= 5 or not b > 10
# not ( a > 5 and b > 5)
# not ( a < 10 or not b < 10)
# not ( not a <= 5 or not b >= 10
# a = 5
# b = 10

# print("1 :", a >= 5 or not b > 10)
# print("2 :", not (a > 5 and b > 5))
# print("3 :", not (a < 10 or not b < 10))
# print("4 :", not (a < 10 or not b < 10))


# Q2. Python program to convert kilometers to miles. Ask kilometer from User.

# km = int(input("enter the kms : "))

# miles = km * 0.621

# print(f"required miles is : {miles}")

# Q3. Ask 3 numbers from User and Calculate the Average.
# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))
# num3 = int(input("enter num3: "))
# print("average is :", (num1 + num2 + num3) / 3)

# Q4. Ask value in Rupees and Convert into Paise.
# rup = int(input("enter the required rupee: "))
# paisa = rup * 100
# print(f"enter the paisa {paisa}")


# Q5. Calculate Area of Square by taking side from User.
# side = int(input("enter the side of square :"))
# area_of_square = side**2

# print(f"area of square {area_of_square}")


# Q6. Ask number of games played in a tournament. Ask the user number of
# games won and number of games loss. Calculate number of tie and total
# Points. (1 win= 4 points, 1 tie =2 points)

total_games = int(input("enter the number of tournamen : "))
won = int(input("enter the number of tournamen won: "))
loss = int(input("enter the number of tournamen loss: "))

games_tied = total_games - (won + loss)

total_points = (won * 4) + (games_tied * 2)

print(f"total points : {total_points}")
print(f"games tied {games_tied}")

# 7. Check if the number entered by User is divisible by 3 or not.
# num = int(input("enter the number: "))
# if num % 3 == 0:
#     print("divisible by 3")
# else:
#     print("not divisible by 3")

# Q8. Ask a number from user. Print if the number is ODD or EVEN.
# num = int(input("enter the number: "))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")
# Q9. Take values of length and breadth of a rectangle from user and check if
# it is square or not.

l = int(input("enter the number: "))
b = int(input("enter the number: "))

if l == b:
    print("it is a square")
else:
    print("it is rectangle")
