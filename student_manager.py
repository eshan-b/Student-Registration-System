import pickle


class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course


def register_student(student_name, course_name, file_path):
    # Load existing student data from the pickle file
    try:
        with open(file_path, 'rb') as file:
            student_dict = pickle.load(file)
    except FileNotFoundError:
        student_dict = {}

    # Create new student object
    student = Student(student_name, course_name)

    # Add student to the dictionary
    student_dict[student_name] = student

    # Save updated student data to the pickle file
    with open(file_path, 'wb') as file:
        pickle.dump(student_dict, file)


def unregister_student(student_name, course_name, file_path):
    # Load existing student data from the pickle file
    try:
        with open(file_path, 'rb') as file:
            student_dict = pickle.load(file)
    except FileNotFoundError:
        student_dict = {}

    # Find and remove the student from the dictionary
    if student_name in student_dict:
        del student_dict[student_name]

    # Save updated student data to the pickle file
    with open(file_path, 'wb') as file:
        pickle.dump(student_dict, file)


def get_students_by_course(course_name, file_path):
    # Load existing student data from the pickle file
    try:
        with open(file_path, 'rb') as file:
            student_dict = pickle.load(file)
    except FileNotFoundError:
        return []

    # Retrieve students by course from the dictionary
    students = [student.name for student in student_dict.values()
                if student.course == course_name]
    return students


# Test
if __name__ == '__main__':
    file_path = 'Student Database\student_data.pkl'

    # Register a student
    register_student('John Doe', 'Math', file_path)

    # Unregister a student
    unregister_student('Jane Smith', 'English', file_path)

    # Get students by course
    math_students = get_students_by_course('Math', file_path)
    print('Math Students:', math_students)
