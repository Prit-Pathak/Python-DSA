"""
Ask a mark from a user.

91 - 100 -> A
81 - 90 -> B
71 - 80 -> C
61 - 70 -> D
1 - 60 -> Fail
"""

marks = int(input("enter the marks: "))

if marks > 90 and marks <= 100:
    print("A")
elif marks > 80 and marks <= 90:
    print("B")
elif marks > 70 and marks <= 80:
    print("C")
elif marks > 60 and marks <= 70:
    print("D")
elif marks > 0 and marks <= 60:
    print("Fail")
else:
    print("Invalid")
