"""
Q3-> Find and print the student(s) with the highest individual score. If
multiple students have the same highest score, print all their names.
The highest mark is 98, scored by Nihar
"""


def highest_score(dct: dict) -> None:
    topper_marks = 0
    topper_name = ""
    for key in dct:
        max = 0
        for item in dct[key]:
            if item > max:
                max = item
        if max > topper_marks:
            topper_marks = max
            topper_name = key
    print(f"The highest mark is {topper_marks}, scored by {topper_name}")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

res = highest_score(details)
