"""
Print the name of the youngest student.
The youngest student is Muskan, age 16.

"""

from typing import Dict


def print_youngest_student(details: Dict[str, Dict]):
    youngest_age = None
    youngest_student = ""
    for student, info in details.items():
        age = info["age"]
        if youngest_age is None or age < youngest_age:
            youngest_age = age
            youngest_student = student
    print(f"The youngest student is {youngest_student}, age {youngest_age}.")


details = {
    "Anirudh": {
        "age": 56,
        "gender": "Male",
        "marks": [3, 455, 64, 33],
        "adult": True,
    },
    "Muskan": {
        "age": 16,
        "gender": "Female",
        "marks": [34, 89, 70, 99, 43],
        "adult": False,
    },
    "Nihar": {
        "age": 24,
        "gender": "Male",
        "marks": [99, 100],
        "adult": True,
    },
}

res = print_youngest_student(details)
