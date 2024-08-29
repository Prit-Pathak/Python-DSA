# Display details -> classs methods

from typing import List


class Student:
    # Magic/Dunder Methods
    def __init__(self, roll_no: int, name: str, age: int, gender: str, marks=[]):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = marks

    def updateName(self, new_name) -> None:
        self.name = new_name

    def total(self):
        t = 0
        for m in self.marks:
            t += m
        return t

    def display(self):
        print(f"roll_no = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")
        print(f"marks = {self.marks} \n\n")


Student_details: List[Student] = []

while True:
    print("1) Add a student")
    print("2) remove a student")
    print("3) display student details")
    print("4) update student details")
    print("5) Display a student details")
    print("6) exit")

    choice = int(input("enter your choice: "))

    if choice == 1:
        roll_no = int(input("enter roll no: "))
        name = input("enter name: ")
        age = int(input("enter age: "))
        gender = input("enter gender: ")
        no_of_sub = 4
        marks = []
        for _ in range(no_of_sub):
            m = int(input("enter marks: "))
            marks.append(m)
        x = Student(roll_no, name, age, gender, marks)
        Student_details.append(x)
    elif choice == 2:
        pass
    elif choice == 3:
        if len(Student_details) == 0:
            print("no students found")
        else:
            for stu in Student_details:
                stu.display()
    elif choice == 4:
        pass
    elif choice == 5:
        rno = int(input("Enter student roll number you want to search for = "))
        # Student_details[rol_no - 1].display() --> method 1 of accessing of obj
        for stu in Student_details:
            if stu.roll_no == rno:
                stu.display()
                break
            else:
                print("No student found with that roll number")
    elif choice == 6:
        break
    else:
        print("Invalid choice")
