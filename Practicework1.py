import math
import numpy as np

class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits


class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  

    def add_mark(self, course_id, raw_mark):
        floored_mark = math.floor(raw_mark * 10) / 10.0
        self.marks[course_id] = floored_mark

        marks_list = []
        weights_list = []
        
        for course_id, mark in self.marks.items():
            if course_id in courses_dict:
                marks_list.append(mark)
                weights_list.append(courses_dict[course_id].credits)
                
        if not weights_list:
            return 0.0
            
        return np.average(marks_list, weights=weights_list)


students = []
courses_dict = {}

num_s = int(input("Number of students: "))
for _ in range(num_s):
    s_id = input("Student ID: ")
    s_name = input("Student name: ")
    s_dob = input("Date of birth: ")
    students.append(Student(s_id, s_name, s_dob))

num_c = int(input("Number of courses: "))
for _ in range(num_c):
    c_id = input("Course ID: ")
    c_name = input("Course name: ")
    c_credits = int(input("Course credits: "))
    courses_dict[c_id] = Course(c_id, c_name, c_credits)

for c_id, course in courses_dict.items():
    print(f"\n--- Entering marks for course: {course.name} ({c_id}) ---")
    for student in students:
        mark = float(input(f"Enter mark for {student.name}: "))
        student.add_mark(c_id, mark)
