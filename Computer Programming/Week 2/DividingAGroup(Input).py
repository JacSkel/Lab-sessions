#!/usr/bin/env python3

student = int(input("Enter how many students? "))
group_size = int(input("Enter the size of how many students there are in a group? "))
number_groups = int(student / group_size)
number_student_left = student % group_size
if number_student_left > 1:
    print(number_groups, "number of groups with" , number_student_left, "number of students left over")
else:
    print(number_groups, "number of groups with", number_student_left, "number of student left over")