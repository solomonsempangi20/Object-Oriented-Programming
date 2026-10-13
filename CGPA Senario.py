class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa


student = Student("Amina", 4.2)
print(student.name, student.cgpa)