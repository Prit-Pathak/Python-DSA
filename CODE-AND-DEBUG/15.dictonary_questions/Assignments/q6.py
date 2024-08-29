"""
Q6 -> Print the total number of marks entries (i.e., the total number of marks
given) for each student.
Anirudh: 3
Sanjay: 7
Muskan: 4
Nihar: 5
Akshay: 2
"""


def marks_entries(dct: dict) -> None:
    for key in dct:
        print(f"{key} : {len(dct[key])}")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

res = marks_entries(details)
