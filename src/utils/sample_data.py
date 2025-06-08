def create_sample_problem() -> tuple[dict[int, set[int]], dict[int, set[int]]]:
    """
    Create a small sample exam timetabling problem.

    Returns:
        tuple: (exam_students, student_exams) dictionaries
    """
    # Dictionary mapping exams to the set of students taking them
    exam_students = {
        0: {101, 102, 103},  # Exam 0 taken by students 101, 102, 103
        1: {101, 103, 105},  # Exam 1 taken by students 101, 103, 105
        2: {102, 104, 106},  # Exam 2 taken by students 102, 104, 106
        3: {103, 105, 107},  # Exam 3 taken by students 103, 105, 107
        4: {104, 106, 108},  # Exam 4 taken by students 104, 106, 108
        5: {107, 108, 109},  # Exam 5 taken by students 107, 108, 109
    }

    # Build student_exams from exam_students
    student_exams: dict[int, set[int]] = {}
    for exam, students in exam_students.items():
        for student in students:
            if student not in student_exams:
                student_exams[student] = set()
            student_exams[student].add(exam)

    return exam_students, student_exams


if __name__ == "__main__":
    # Test the sample data
    exam_students, student_exams = create_sample_problem()

    print("Exams and their students:")
    for exam, students in exam_students.items():
        print(f"Exam {exam}: {students}")

    print("\nStudents and their exams:")
    for student, exams in student_exams.items():
        print(f"Student {student}: {exams}")

    # Identify conflicts (exams that share students)
    print("\nConflicting exams:")
    for exam1 in exam_students:
        for exam2 in exam_students:
            if exam1 < exam2:  # Check each pair only once
                common_students = exam_students[exam1].intersection(
                    exam_students[exam2]
                )
                if common_students:
                    print(
                        f"Exams {exam1} and {exam2} conflict: "
                        f"shared students {common_students}"
                    )
