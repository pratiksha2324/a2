# Base class Person
class Person:
    def __init__(self, name, age, person_id):
        self.name = name
        self.age = age
        self.id = person_id

# Student class inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age, student_id)
        self.grade = grade
        self.enrolled_courses = []

    def enroll_course(self, course):
        self.enrolled_courses.append(course)
        course.add_student(self)

    def list_courses(self):
        return [course.course_name for course in self.enrolled_courses]

# Teacher class inherits from Person
class Teacher(Person):
    def __init__(self, name, age, teacher_id, subject):
        super().__init__(name, age, teacher_id)
        self.subject = subject
        self.assigned_courses = []

    def assign_course(self, course):
        self.assigned_courses.append(course)
        course.assign_teacher(self)

    def list_assigned_courses(self):
        return [course.course_name for course in self.assigned_courses]

# Course class
class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []
        self.teacher = None

    def add_student(self, student):
        self.enrolled_students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def list_students(self):
        return [student.name for student in self.enrolled_students]

    def calculate_average_grade(self):
        if not self.enrolled_students:
            return 0
        total_grades = sum(student.grade for student in self.enrolled_students)
        return total_grades / len(self.enrolled_students)

# School class to manage students, teachers, and courses
class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def view_students_in_course(self, course_id):
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course:
            return course.list_students()
        return None

    def view_courses_by_student(self, student_id):
        student = next((s for s in self.students if s.id == student_id), None)
        if student:
            return student.list_courses()
        return None

# Example usage
school = School("Springfield High")

# Creating students
student1 = Student("Alice", 15, "S001", 85)
student2 = Student("Bob", 16, "S002", 90)

# Creating teachers
teacher1 = Teacher("Mr. Smith", 40, "T001", "Mathematics")

# Creating courses
course1 = Course("Math 101", "C001")

# Adding students and teachers to the school
school.add_student(student1)
school.add_student(student2)
school.add_teacher(teacher1)

# Adding courses to the school
school.add_course(course1)

# Enrolling students in courses
student1.enroll_course(course1)
student2.enroll_course(course1)

# Assigning teacher to a course
teacher1.assign_course(course1)

# Viewing students in a course
print("Students in Math 101:", school.view_students_in_course("C001"))

# Viewing courses a student is enrolled in
print("Courses Alice is enrolled in:", school.view_courses_by_student("S001"))

# Calculating average grade in a course
print("Average grade in Math 101:", course1.calculate_average_grade())
