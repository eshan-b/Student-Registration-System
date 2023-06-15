import pickle


class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course


def register_student(student_name, course_name, file_path):
    # Load existing student data from lookup table
    try:
        with open(file_path, 'rb') as file:
            students = pickle.load(file)
    except FileNotFoundError:
        students = []

    # Create new student object
    student = Student(student_name, course_name)

    # Add student to the list
    students.append(student)

    # Save updated student data to the lookup table
    with open(file_path, 'wb') as file:
        pickle.dump(students, file)


def unregister_student(student_name, course_name, file_path):
    # Load existing student data from the lookup table
    try:
        with open(file_path, 'rb') as file:
            students = pickle.load(file)
    except FileNotFoundError:
        students = []

    # Find student to unregister
    for student in students:
        if student.name == student_name and student.course == course_name:
            # Remove student from the list
            students.remove(student)
            break

    # Save updated student data to the lookup table
    with open(file_path, 'wb') as file:
        pickle.dump(students, file)


def get_students_by_course(course_name, file_path):
    # Load existing student data from the lookup table
    try:
        with open(file_path, 'rb') as file:
            students = pickle.load(file)
    except FileNotFoundError:
        return []

    # Retrieve students by course
    course_students = []
    for student in students:
        if student.course == course_name:
            course_students.append(student.name)

    return course_students


# Test
if __name__ == '__main__':
    file_path = 'Student Database\student_data.pkl'

    # Register student
    register_student('John Doe', 'Math', file_path)

    # Unregister student
    unregister_student('Jane Smith', 'English', file_path)

    # Get students by course
    math_students = get_students_by_course('Math', file_path)
    print('Math Students:', math_students)
