import pickle


def build_index(file_path):
    # Read contents
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Build index map
    index = {}
    current_student = None

    for line in lines:
        line = line.strip()

        if line.startswith('Student:'):
            current_student = line.replace('Student: ', '')  # update student

        elif line.startswith('Course:'):
            course_name = line.replace('Course: ', '')  # update course

            if course_name not in index:
                index[course_name] = []

            index[course_name].append(current_student)

    # Save index map to pkl file
    index_file = 'index.pkl'
    with open(index_file, 'wb') as file:
        pickle.dump(index, file)


def get_students_by_course(course_name):
    # Load index map
    index_file = 'index.pkl'
    with open(index_file, 'rb') as file:
        index = pickle.load(file)

    # Get students by course
    if course_name in index:
        return index[course_name]
    else:
        return []


def unregister_student(student_name, course_name):
    # Load index map
    index_file = 'index.pkl'
    with open(index_file, 'rb') as file:
        index = pickle.load(file)

    # Remove course
    if course_name in index and student_name in index[course_name]:
        index[course_name].remove(student_name)

    # Update index map
    with open(index_file, 'wb') as file:
        pickle.dump(index, file)


# Test
file_path = 'Student Database\students.txt'
student_name = 'John Doe'
course_name = 'Mathematics'

build_index(file_path)  # build index map

# Unregister
unregister_student(file_path, student_name, course_name)

# Filter course
course_students = get_students_by_course(file_path, course_name)
print(f"Students registered for {course_name}: {course_students}")
