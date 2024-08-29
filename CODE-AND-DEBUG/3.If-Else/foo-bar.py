"""
Ask a number from user.

num is divisible by 3 -> FOO
num is divisible by 5 -> BAR

num is divisible by 3 and 5 -> FOOBAR

else
-> Invalid
"""

num = int(input("enter the number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FOOBAR")
elif num % 5 == 0:
    print("BAR")
elif num % 3 == 0:
    print("FOO")
else:
    print("Invalid")
