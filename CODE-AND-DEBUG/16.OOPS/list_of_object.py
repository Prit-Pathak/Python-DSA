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


# s1 = Student(1, "Prit", 18, "male", [12, 15, 15, 23])
# s2 = Student(2, "Ram", 18, "male", [33, 45, 17, 25])

# methods 1 -> list of obejct
# student_data1 = [s1, s2]
# student_data1[0].display()
# print(student_data1[0].marks)
# print(student_data1[0].total())
# print(student_data1[1].total())
# student_data1[1].display()

# methods 2 ->list of object

student_data2 = [
    Student(1, "Prit", 18, "male", [12, 15, 15, 23]),
    Student(2, "Ram", 18, "male", [33, 45, 17, 25]),
]

student_data2[0].display()
print(student_data2[0].marks)
print(student_data2[0].total())
print(student_data2[1].total())

print(student_data2[1].age)
