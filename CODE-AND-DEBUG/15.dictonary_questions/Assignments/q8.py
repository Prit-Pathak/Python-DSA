"""
Print the name and age of each student.
Anirudh: 56
Muskan: 16
Nihar: 24

"""

from typing import Dict, List


def info(dct: Dict[str, Dict]):
    for key, value in dct.items():
        print(f"{key} : {value['age']}")


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

res = info(details)
