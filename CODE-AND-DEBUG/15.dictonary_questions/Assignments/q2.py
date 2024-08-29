"""
Print the student name and their corresponding highest marks.
Anirudh: 78
Sanjay: 78
Muskan: 87
Nihar: 98
Akshay: 56
"""

# def max_score(dct: dict) -> None:
#     for key in dct:
#         max = 0
#         stu = ""
#         for item in dct[key]:
#             if item > max:
#                 max = item
#                 stu = key
#         print(f"{stu} : {max}")


def min_marks(dct: dict):
    student_name = ""
    min_marks = min(min(marks) for marks in dct.values())
    for stu, marks in details.items():
        if min_marks in marks:
            print(f"minimum marks: {stu} : {min_marks}")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

res = min_marks(details)
