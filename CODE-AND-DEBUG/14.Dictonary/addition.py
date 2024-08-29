from typing import Dict

marks: Dict[str, int] = {
    "history": 78,
    "science": 16,
    "computer": 99,
    "chemistry": 65,
    "sst": 25,
}

marks["sst"] = 66
print(marks)

marks["English"] = 84
print(marks)

# marks.update({"Physics": 90})
# print(marks)

# marks.update({"sst": 55})
# print(marks)
