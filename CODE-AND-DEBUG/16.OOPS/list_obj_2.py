# update details -> classs methods

from typing import List


class Student:
    # Magic/Dunder Methods
    def __init__(self, roll_no: int, name: str, age: int, gender: str, marks=[]):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = marks

    def updateDetails(self, newName=None, age=None, gender=None) -> None:
        if newName:
            self.name = newName
        if age:
            self.age = age
        if gender:
            self.gender = gender

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
    print("3) display all student details")
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
        rno = int(input("Enter student roll number you want to remove = "))
        student_index = -1
        for i in range(len(Student_details)):
            if Student_details[i].roll_no == rno:
                student_index = i
                break
        if student_index == -1:
            print("student not found")
        else:
            Student_details.pop(student_index)
            print("student deleted \n\n")

    elif choice == 3:
        if len(Student_details) == 0:
            print("no students found")
        else:
            for stu in Student_details:
                stu.display()
    elif choice == 4:
        rno = int(input("Enter student roll number you want to update details = "))
        for stu in Student_details:
            if stu.roll_no == rno:
                n_name = input("enter new name: ")
                n_age = int(input("enter new age: "))
                n_gender = input("enter new gender: ")
                stu.updateDetails(n_name, n_age, n_gender)
                break
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
