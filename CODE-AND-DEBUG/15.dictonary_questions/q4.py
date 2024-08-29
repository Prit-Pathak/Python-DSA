from typing import List, Dict

"""
print maximum marks and the person who has scored it.
Sanjay 371
..
..
"""


def max_marks(my_dict: Dict[str, List[int]]) -> None:
    name = None
    max_m = 0
    for key in my_dict:
        total = 0
        for i in range(0, len(my_dict[key])):
            total = total + my_dict[key][i]
            if total > max_m:
                max_m = total
                name = key

    print(f"maximum marks {max_m} is scored by {name}")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

res = max_marks(details)
