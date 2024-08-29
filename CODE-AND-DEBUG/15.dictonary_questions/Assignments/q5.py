"""
Q5 -> Print the name of the student who has the highest average marks.
The highest average marks are 68.75, scored by Muskan.
"""


def max_avg_dict(dct: dict) -> None:
    max_avg = 0
    max_avg_name = ""
    for key in dct:
        total = 0
        for item in dct[key]:
            total += item
        avg = total / len(dct[key])
        if avg > max_avg:
            max_avg = avg
            max_avg_name = key
    print(f"The highest average marks are {max_avg}, scored by{max_avg_name} ")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

res = max_avg_dict(details)
