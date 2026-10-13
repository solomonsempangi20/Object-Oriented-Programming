class Student:
    def __init__(self, name, grade, pin):
        self.name = name
        self._grade = grade
        self._pin = pin

    def get_pin(self):
        return self._pin

    def get_grade(self):
        return self._grade

s1 = Student("Sabrina", 4.7, 2580)

print(s1.name)
print(s1.get_grade())
print(s1.get_pin())