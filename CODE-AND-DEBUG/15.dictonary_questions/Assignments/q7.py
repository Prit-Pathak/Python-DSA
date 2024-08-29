"""
Q7 -> Identify and print the name(s) of the student(s) who have scored more
than a specified number of marks (e.g., more than 75) in any subject.
Students who scored more than 75:
Anirudh: [78]
Sanjay: [78]
Muskan: [87, 78]
Nihar: [78, 98]

"""

from typing import Dict, List


# Methid I
def sp_score(dct: dict, k: int) -> None:
    for key in dct:
        student = ""
        marks = []
        for item in dct[key]:
            if item > k:
                marks.append(item)
        student = key
        print(f"{student} : {marks}")


# Method II
def print_students_above_threshold(details: Dict[str, List[int]], threshold: int):
    for student, marks in details.items():
        above_threshold = [mark for mark in marks if mark > threshold]
        if above_threshold:
            print(f"{student}: {above_threshold}")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}
k = 75
res = sp_score(details, k)
