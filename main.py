class Student:
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def set_grade(self, grade):
        self.grade = grade

    def set_name(self, name):
        self.name = name

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}")

    def student_display(self):
        self.display_info()


class UndergraduateStudent(Student):
    def __init__(self, name, id, grade, major):
        super().__init__(name, id, grade)
        self.major = major

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}, Major: {self.major}")


class GraduateStudent(Student):
    def __init__(self, name, id, grade, program_title):
        super().__init__(name, id, grade)
        self.program_title = program_title

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}, Program Title: {self.program_title}")


if __name__ == "__main__":
    student1 = Student("Youssef", 202501148, "A")
    student2 = Student("Seif", 202501143, "A+")

    student1.student_display()
    student2.student_display()

    student1.set_grade("A+")
    student1.student_display()

    ug_student = UndergraduateStudent("Ali", 202501150, "B+", "Computer Science")
    grad_student = GraduateStudent("Fatma", 202501160, "A", "Master of Data Science")

    ug_student.display_info()
    grad_student.display_info()