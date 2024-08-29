"""
Find and print the names of all students who are adults.
"""

from typing import Dict, List


def adult(dct: Dict[str, Dict]):
    for key, val in dct.items():
        student = ""
        if val["age"] > 18:
            student = key
            print(student)


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

res = adult(details)
