def unregister_student(file_path, student_name, course_name):
    # Read contents
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find student & course
    student_index = None
    course_indices = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line == f'Student: {student_name}':
            student_index = i  # update student

        elif line == f'Course: {course_name}':
            course_indices.append(i)  # update course

        i += 1

    # Remove course
    if student_index is not None and course_indices:
        for index in course_indices:
            lines.pop(index)

        # Write modified data back to the text file
        with open(file_path, 'w') as file:
            file.writelines(lines)
    else:
        print(f"Student '{student_name}' or course '{course_name}' not found.")


def get_students_by_course(file_path, course_name):
    students = []
    current_student = None

    # Read contents
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Parse data
    for line in lines:
        line = line.strip()

        if line.startswith('Student:'):
            current_student = line.replace('Student: ', '')
        elif line.startswith('Course:') and line.replace('Course: ', '') == course_name:
            students.append(current_student)

    return students


# Test
file_path = 'Student Database\students.txt'
student_name = 'John Doe'
course_name = 'Mathematics'

# Unregister
unregister_student(file_path, student_name, course_name)

# Filter course
course_students = get_students_by_course(file_path, course_name)
print(f"Students registered for {course_name}: {course_students}")
