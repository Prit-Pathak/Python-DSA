"""
Calculate and print the average marks for each student.
Anirudh: 138.75
Muskan: 67.0
Nihar: 99.5
"""


def avg_marks(dct: dict):
    for key, val in dct.items():
        total = 0
        for item in val["marks"]:
            total += item
        avg = total / len(val["marks"])

        print(f"{key} : {avg}")


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

res = avg_marks(details)
