"""
Print the name and highest mark of each student.
Anirudh: 455
Muskan: 99
Nihar: 100
"""


def high_score(dct: dict):
    for key, val in dct.items():
        max = 0
        for item in val["marks"]:
            if item > max:
                max = item
        print(f"{key} : {max}")


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

res = high_score(details)
