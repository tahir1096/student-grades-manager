
---

# Student Grade Management System

## Description

This is a simple Python-based command-line application that helps manage student grades. The program allows users to:

- Add a new student and their grade
- Delete a student from the gradebook
- Update an existing student's grade
- Display all students' names and their grades

The application uses a dictionary to store student names as keys and their grades as values. It operates in a loop, showing a menu with options, allowing users to perform operations on the gradebook until they choose to exit.

## Features

- **Add a Student**: Allows the user to input a student's name and grade and add it to the dictionary.
- **Delete a Student**: Enables the user to delete a student by name.
- **Update a Student's Grade**: Lets the user modify a student's existing grade.
- **Display All Students' Grades**: Displays a list of all students and their corresponding grades.
- **Exit the Program**: Gracefully exits the program with a prompt.

## Requirements

- Python 3.x or higher

## Installation

1. **Clone this repository** to your local machine:

   ```bash
   git clone https://github.com/your-username/student-grade-management.git
   ```

2. Navigate to the project directory:

   ```bash
   cd student-grade-management
   ```

3. **Run the program**:

   You can run the program directly using Python:

   ```bash
   python student_grade_management.py
   ```

   Make sure Python is installed on your system.

## Usage

Upon running the program, you will see a menu with the following options:

1. **Add a student**: Enter the student's name and grade to add them to the dictionary.
2. **Delete a student**: Enter the student's name to remove them from the dictionary.
3. **Update a student's grade**: Enter the student's name and new grade to update their record.
4. **Display all students' grades**: View a list of all students and their current grades.
5. **Exit**: Quit the program.

Example Menu:

```
Welcome to Student Grade Management System
Choose an option:
1. Add a student
2. Delete a student
3. Update a student's grade
4. Display all students' grades
5. Exit
```

### Example Usage:

```
Student Name: John Doe
Grade: 85.5
```

Output:

```
Student Name: John Doe grade: 85.5 is added successfully
```

## Error Handling

- The program will validate user inputs to ensure the grades are numeric.
- It will notify the user if an invalid menu choice is made or if the student cannot be found when trying to delete or update.
  
## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

