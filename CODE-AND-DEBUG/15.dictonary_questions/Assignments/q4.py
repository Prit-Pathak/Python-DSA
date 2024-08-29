"""
Calculate and print the average marks of each student.
Anirudh: 66.33
Sanjay: 53.57
Muskan: 68.75
Nihar: 54.6
Akshay: 48.0

"""


def avg_dict(dct: dict) -> None:
    for key in dct:
        total = 0
        for item in dct[key]:
            total += item
        avg = total / len(dct[key])
        print(f"{key} : {avg}")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

res = avg_dict(details)
