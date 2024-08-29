num_subject = int(input("enter number of subject: "))
my_dict = {}
for i in range(num_subject):
    sub_name = input("enter subject name: ")
    sub_marks = int(input("enter marks: "))
    my_dict[sub_name] = sub_marks

print(my_dict)
