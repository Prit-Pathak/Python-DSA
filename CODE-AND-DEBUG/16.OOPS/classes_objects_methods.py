class Student:
    # attributes / class variable
    # name = ""
    # age = 0
    # idd = 0
    # gender = ""
    """
    since all variables are getting overwritten whenever a object is created, we can set the class attributes
    insodes methods itself using self parameter as shown below.
    NOTE:- we can only use attributes after getting created, like in the below example, display methods will omly
    show the attributes value when we first call the set_attributes value.
    """

    # methods
    def set_details(self):
        self.idd = int(input("enter idd: "))
        self.age = int(input("enter age: "))
        self.name = input("enter name: ")
        self.gender = input("enter gender: ")

    def display(self):
        print(self)
        print(f"idd is {self.idd}")
        print(f"age is {self.age}")
        print(f"name is {self.name}")
        print(f"gender is {self.gender}")


s1 = Student()
s2 = Student()

print(s1)
s1.set_details()
s1.display()
s2.display()
