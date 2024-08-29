"""
Find and print the names of students with more than 3 marks entries.
Students with more than 3 marks:
Anirudh
Muskan
"""


def marks_3_entry(dct: dict, k: int):
    for key, val in dct.items():
        if len(val["marks"]) > k:
            print(key)


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
k = 3

res = marks_3_entry(details, k)
