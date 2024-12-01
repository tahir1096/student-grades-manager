student_grades = { }

# add a student in dictionary
def add_student():
    try:
        name = input("Student Name: ")
        grade = float(input("Grade: "))
        student_grades[name] = grade
        print(f"Student Name: {name}, grade: {grade} is added successfully")
    except ValueError:
        print("Invalid input! Please enter a valid grade.")

# delete a student from dictionary
def delete_student():
    name = input("Student Name: ")
    if name in student_grades:
        del student_grades[name]
        print(f"Student Name: {name} is deleted successfully")
    else:
        print(f"Student {name} not found!")

# update a student's grade in dictionary
def update_student_grade():
    name = input("Student Name: ")
    if name in student_grades:
        try:
            new_grade = float(input("New Grade: "))
            student_grades[name] = new_grade
            print(f"Student Name: {name} grade is updated successfully to {new_grade}")
        except ValueError:
            print("Invalid input! Please enter a valid grade.")
    else:
        print(f"Student Name: {name} not found in the dictionary")

# display all students' grades
def display_students_grades():
    if student_grades:
        print("Student Grades List:")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found!")

# main menu
while True:
    print("\nWelcome to Student Grade Management System")
    print("Choose an option:")
    print("1. Add a student")
    print("2. Delete a student")
    print("3. Update a student's grade")
    print("4. Display all students' grades")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        add_student()
    elif choice == 2:
        delete_student()
    elif choice == 3:
        update_student_grade()
    elif choice == 4:
        display_students_grades()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
