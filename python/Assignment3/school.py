class Person:
    def __init__(self, name, age, person_id):
        self.name = name
        self.age = age
        self.person_id = person_id


class Student(Person):
    def __init__(self, name, age, person_id):
        super().__init__(name, age, person_id)
        self.enrolled_courses = {}
    
    def enroll_course(self, course):
        if course.course_id not in self.enrolled_courses:
            self.enrolled_courses[course.course_id] = {"course": course, "grade": None}
    
    def set_grade(self, course_id, grade):
        if course_id in self.enrolled_courses:
            self.enrolled_courses[course_id]["grade"] = grade
        else:
            print(f"Student is not enrolled in course ID {course_id}.")
    
    def get_grades(self):
        return {course_info["course"].course_name: course_info["grade"] 
                for course_info in self.enrolled_courses.values()}
    
    def __repr__(self):
        return f"Student(Name: {self.name}, Age: {self.age}, ID: {self.person_id}, Grades: {self.get_grades()})"


class Teacher(Person):
    def __init__(self, name, age, person_id):
        super().__init__(name, age, person_id)
        self.assigned_courses = []
    
    def assign_course(self, course):
        if course not in self.assigned_courses:
            self.assigned_courses.append(course)
    
    def __repr__(self):
        courses = [course.course_name for course in self.assigned_courses]
        return f"Teacher(Name: {self.name}, Age: {self.age}, ID: {self.person_id}, Courses: {courses})"


class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []

    def add_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            student.enroll_course(self)
    
    def calculate_average_grade(self):
        grades = [s.enrolled_courses[self.course_id]["grade"] 
                  for s in self.enrolled_students if s.enrolled_courses.get(self.course_id)]
        if not grades:
            return 0
        total_grades = sum(g for g in grades if g is not None)
        return total_grades / len(grades)

    def __repr__(self):
        return f"Course(Name: {self.course_name}, ID: {self.course_id})"


class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student_in_course(self, student_id, course_id):
        student = next((s for s in self.students if s.person_id == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)

        if student and course:
            course.add_student(student)
            print(f"{student.name} enrolled in {course.course_name}")
        else:
            print("Invalid student or course ID")

    def assign_teacher_to_course(self, teacher_id, course_id):
        teacher = next((t for t in self.teachers if t.person_id == teacher_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)

        if teacher and course:
            teacher.assign_course(course)
            print(f"{teacher.name} assigned to {course.course_name}")
        else:
            print("Invalid teacher or course ID")

    def view_students_in_course(self, course_id):
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course:
            if course.enrolled_students:
                print(f"Students in {course.course_name}:")
                for student in course.enrolled_students:
                    print(f"{student.name} (ID: {student.person_id})")
            else:
                print(f"No students enrolled in {course.course_name}")
        else:
            print("Course not found")

    def view_courses_of_student(self, student_id):
        student = next((s for s in self.students if s.person_id == student_id), None)
        if student:
            if student.enrolled_courses:
                print(f"{student.name} is enrolled in the following courses:")
                for course_id, info in student.enrolled_courses.items():
                    print(f"{info['course'].course_name} (ID: {course_id}), Grade: {info['grade']}")
            else:
                print(f"{student.name} is not enrolled in any courses")
        else:
            print("Student not found")

    def calculate_course_average_grade(self, course_id):
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course:
            avg_grade = course.calculate_average_grade()
            print(f"Average grade for {course.course_name}: {avg_grade:.2f}")
        else:
            print("Course not found")

    def view_all_students(self):
        if self.students:
            print("List of Students:")
            for student in self.students:
                print(f"Name: {student.name}, Age: {student.age}, ID: {student.person_id}, Grades: {student.get_grades()}")
        else:
            print("No students enrolled.")

    def view_all_teachers(self):
        if self.teachers:
            print("List of Teachers:")
            for teacher in self.teachers:
                print(f"Name: {teacher.name}, Age: {teacher.age}, ID: {teacher.person_id}, Courses: {[course.course_name for course in teacher.assigned_courses]}")
        else:
            print("No teachers available.")

    def view_all_courses(self):
        if self.courses:
            print("List of Courses:")
            for course in self.courses:
                print(f"Course Name: {course.course_name}, ID: {course.course_id}")
        else:
            print("No courses available.")


def validate_positive_integer(input_value):
    try:
        value = int(input_value)
        if value <= 0:
            raise ValueError
        return value
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return None


def main():
    school = School()

    while True:
        print("\nSchool Management System Menu:")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Course")
        print("4. Enroll Student in a Course")
        print("5. Assign Teacher to a Course")
        print("6. View Students in a Course")
        print("7. View Courses of a Student")
        print("8. Calculate Average Grade of a Course")
        print("9. View All Students")
        print("10. View All Teachers")
        print("11. View All Courses")
        print("12. Set Grade for a Course")
        print("13. Exit")

        choice = input("Enter your choice (1-13): ")

        if choice == "1":
            name = input("Enter student's name: ")
            age = validate_positive_integer(input("Enter student's age: "))
            if age is None:
                continue
            student_id = validate_positive_integer(input("Enter student's ID: "))
            if student_id is None:
                continue
            student = Student(name, age, student_id)
            school.add_student(student)
            print(f"Student {name} added successfully.")

        elif choice == "2":
            name = input("Enter teacher's name: ")
            age = validate_positive_integer(input("Enter teacher's age: "))
            if age is None:
                continue
            teacher_id = validate_positive_integer(input("Enter teacher's ID: "))
            if teacher_id is None:
                continue
            teacher = Teacher(name, age, teacher_id)
            school.add_teacher(teacher)
            print(f"Teacher {name} added successfully.")

        elif choice == "3":
            course_name = input("Enter course name: ")
            course_id = validate_positive_integer(input("Enter course ID: "))
            if course_id is None:
                continue
            course = Course(course_name, course_id)
            school.add_course(course)
            print(f"Course {course_name} added successfully.")

        elif choice == "4":
            student_id = validate_positive_integer(input("Enter student's ID to enroll: "))
            if student_id is None:
                continue
            course_id = validate_positive_integer(input("Enter course ID: "))
            if course_id is None:
                continue
            school.enroll_student_in_course(student_id, course_id)

        elif choice == "5":
            teacher_id = validate_positive_integer(input("Enter teacher's ID to assign: "))
            if teacher_id is None:
                continue
            course_id = validate_positive_integer(input("Enter course ID: "))
            if course_id is None:
                continue
            school.assign_teacher_to_course(teacher_id, course_id)

        elif choice == "6":
            course_id = validate_positive_integer(input("Enter course ID to view students: "))
            if course_id is None:
                continue
            school.view_students_in_course(course_id)

        elif choice == "7":
            student_id = validate_positive_integer(input("Enter student's ID to view courses: "))
            if student_id is None:
                continue
            school.view_courses_of_student(student_id)

        elif choice == "8":
            course_id = validate_positive_integer(input("Enter course ID to calculate average grade: "))
            if course_id is None:
                continue
            school.calculate_course_average_grade(course_id)

        elif choice == "9":
            school.view_all_students()

        elif choice == "10":
            school.view_all_teachers()

        elif choice == "11":
            school.view_all_courses()

        elif choice == "12":
            student_id = validate_positive_integer(input("Enter student's ID to set grade: "))
            if student_id is None:
                continue
            course_id = validate_positive_integer(input("Enter course ID: "))
            if course_id is None:
                continue
            grade = validate_positive_integer(input("Enter grade: "))
            if grade is None:
                continue
            student = next((s for s in school.students if s.person_id == student_id), None)
            if student:
                student.set_grade(course_id, grade)
                print(f"Grade {grade} set for course ID {course_id} for student ID {student_id}.")
            else:
                print("Student not found.")

        elif choice == "13":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
