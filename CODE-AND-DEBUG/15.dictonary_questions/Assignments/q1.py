"""
Use this dict in all the questions.
details = {
 "Anirudh": [56, 78, 65],
 "Sanjay": [58, 78, 56, 12, 33, 56, 78],
 "Muskan": [87, 78, 65, 45],
 "Nihar": [32, 78, 32, 98, 33],
 "Akshay": [56, 40],
}

Q1->  Print all the marks of each student in a readable format.
Anirudh: 56, 78, 65
Sanjay: 58, 78, 56, 12, 33, 56, 78
Muskan: 87, 78, 65, 45
Nihar: 32, 78, 32, 98, 33
Akshay: 56, 40
"""


def re_form(details: dict):
    for key, value in details.items():
        print(f"{key} : {', '.join(str(m) for m in value)}")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

z = re_form(details)
print(z)
