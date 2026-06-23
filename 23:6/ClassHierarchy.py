class School:
    num_students = 0

    def __init__(self):
        School.num_students += 1

class Classroom:
    def __init__(self, classname, teacher):
        self.classname = classname
        self.teacher = teacher
        super().__init__()


class Student(Classroom, School):
    def __init__(self, classname, sname, sgrade, teacher):
        self.sname = sname
        self.sgrade = sgrade
        super().__init__(classname, teacher)

student1 = Student('8A', 'John', 83, 'Ms. Blue')
student2 = Student('8B', 'Jane', 91, 'Ms. Green')

print(f'{student1.sname}\'s teacher is {student1.teacher}, and his school has {School.num_students} students')