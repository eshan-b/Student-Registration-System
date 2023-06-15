# Student Registration System

This project implements a Student Registration System in Python. It provides functionality to register students for courses, retrieve students by course, and unregister students from courses. The project offers three different approaches to handle student data, each with its own advantages:

1. **Naive Solution**: The naive solution reads student information from a text file and performs linear searches for retrieval and updates. It is simple but not efficient for large data sets.

2. **Indexing Solution**: The indexing solution improves efficiency by building an index using a text file. It stores the index in a separate file and provides faster retrieval and update operations.

3. **Lookup Table (Pickle)**: The lookup table approach uses the pickle module to build an index for direct lookup of student data. It offers the fastest retrieval and update operations by storing the index as a serialized Python object.

4. **Student Manager**: The `student_manager.py` file introduces a `Student` class and provides functions to add, modify, and retrieve student data using a pickle file. The `Student` class represents a student object with instance variables for name and course. The system allows registering a student, unregistering a student, and retrieving students by course. The student data is stored in a binary file using the `pickle` module.

## File Structure

- `naive_solution.py`: Implements the student registration system using a linear search approach.
- `indexing_solution.py`: Implements the student registration system using an index for improved efficiency.
- `lookup_table_solution.py`: Implements the student registration system using a lookup table (pickle) for optimal performance.
- `student_manager.py`: Contains the implementation of the student registration system using a `Student` class and a pickle file.
- `students.txt`: Sample text file containing student registration information.

## Usage

1. Choose the desired solution based on your requirements: naive, indexing, or lookup table.
2. Run the selected Python script (`naive_solution.py`, `indexing_solution.py`, or `lookup_table_solution.py`).
3. Follow the prompts to register students, retrieve students by course, and unregister students from courses.

## Requirements

- Python 3.x
- pickle module (for indexing and lookup table solutions)
