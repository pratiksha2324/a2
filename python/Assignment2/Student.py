def get_student_data():
    students_data = []
    print("Enter student data. Type 'done' when finished.")

    while True:
        student_name = input("Enter student name (or 'done' to finish): ")
        if student_name.lower() == 'done':
            break
        if not student_name.isalpha():
            print("Invalid name. Please enter a valid name consisting of only letters.")
            continue

        grades = {}
        while True:
            course_name = input("Enter course name (or 'done' to finish courses for this student): ")
            if course_name.lower() == 'done':
                break
            try:
                grade = float(input(f"Enter grade for {course_name}: "))
                if grade < 0 or grade > 100:
                    print("Invalid grade. Please enter a grade between 0 and 100.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a numeric value for the grade.")
                continue

            grades[course_name] = grade

        students_data.append({
            "student_name": student_name,
            "grades": grades
        })

    return students_data

def calculate_average_grade(grades):
    if len(grades) == 0:
        return 0
    return sum(grades.values()) / len(grades)

def find_top_performing_students(students_data):
    if not students_data:
        return []

    max_average = max(calculate_average_grade(student["grades"]) for student in students_data)
    top_students = [student for student in students_data if calculate_average_grade(student["grades"]) == max_average]
    return top_students

def calculate_grade_distribution(students_data):
    grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for student in students_data:
        for grade in student["grades"].values():
            if grade >= 90:
                grade_distribution["A"] += 1
            elif grade >= 80:
                grade_distribution["B"] += 1
            elif grade >= 70:
                grade_distribution["C"] += 1
            elif grade >= 60:
                grade_distribution["D"] += 1
            else:
                grade_distribution["F"] += 1
                
    return grade_distribution

def find_highest_lowest_scores(students_data):
    all_grades = [grade for student in students_data for grade in student["grades"].values()]
    highest_score = max(all_grades) if all_grades else None
    lowest_score = min(all_grades) if all_grades else None
    return highest_score, lowest_score

def main():
    # Get student data from the user
    students_data = get_student_data()
    #print student for student in students_data
    print(students_data)
    if not students_data:
        print("No student data provided.")
        return

    # Calculate average grade for each student
    for student in students_data:
        average_grade = calculate_average_grade(student["grades"])
        print(f"Average grade for {student['student_name']}: {average_grade:.2f}")

    # Find top-performing students
    top_students = find_top_performing_students(students_data)
    print("\nTop-Performing Students:")
    for student in top_students:
        print(f"  - {student['student_name']}")

    # Calculate grade distribution
    grade_distribution = calculate_grade_distribution(students_data)
    print("\nGrade Distribution:")
    for grade, count in grade_distribution.items():
        print(f"  - {grade}: {count} students")

    # Find highest and lowest scores
    highest_score, lowest_score = find_highest_lowest_scores(students_data)
    print(f"\nHighest Score: {highest_score:.2f}" if highest_score is not None else "\nNo grades available.")
    print(f"Lowest Score: {lowest_score:.2f}" if lowest_score is not None else "No grades available.")

if __name__ == "__main__":
    main()
