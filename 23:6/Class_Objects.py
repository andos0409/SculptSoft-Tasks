
class Student:

    num_students = 0

    def __init__(self, graduate_year, grade, age, enrolled, name):
        self.graduate_year = graduate_year
        self.grade = grade
        self.age = age
        self.enrolled = enrolled
        self.name = name

        Student.num_students += 1

    
    def give_grade(self, new_grade):
        self.grade = new_grade
    
    def unenrol(self):
        self.enrolled = False
    
    def change_name(self, new_name):
        self.name = new_name

student1 = Student(2026, 96, 18, True, 'John')
student2 = Student(2026, 79, 19, True, 'Jane')
student3 = Student(2026, 62, 19, True, 'James')

student1.change_name('Tim')
print('New student1 name is', student1.name)