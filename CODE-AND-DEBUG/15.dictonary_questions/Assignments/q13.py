"""
Print the total marks scored by each student.
Anirudh: 555
Muskan: 335
Nihar: 199
"""


def total_mrks(dct: dict):
    for key, val in dct.items():
        total = sum(val["marks"])
        print(f"{key} : {total}")


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

res = total_mrks(details)
