class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def return_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_student):
        self.name = name
        self.max_student = max_student
        self.students = []

    def add_student(self, student):
        if len(self.students) <= self.max_student:
            self.students.append(student)

    def get_average(self):
        value = 0
        for s in self.students:
            value += s.return_grade()
        return value / len(self.students)

    def show_students(self):
        return self.students


eee = Course("EEE", 20)
s1 = Student("osamede", 22, 99)
s2 = Student("richmond", 24, 100)
eee.add_student(s1)
eee.add_student(s2)
# print(eee.show_students())
print(eee.get_average())
