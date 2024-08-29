"""
Find and print the name of the student with the highest average
marks.
The student with the highest average marks is Nihar with an average of 99.5
"""


def print_highest_average(details: Dict[str, Dict]):
    highest_average = 0
    top_student = ""
    for student, info in details.items():
        marks = info["marks"]
        total = 0
        count = 0
        for mark in marks:
            total += mark
            count += 1
        average = total / count
        if average > highest_average:
            highest_average = average
            top_student = student
    print(
        f"The student with the highest average marks is {top_student} with an average of {highest_average:.2f}."
    )


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
