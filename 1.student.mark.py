students = {}

def add_student(student_id, name, dob):
    students[student_id] = {'name': name, 'dob': dob, 'marks': {}}

def add_mark(student_id, subject, mark):
    if student_id in students:
        students[student_id]['marks'][subject] = mark
    else:
        print("Student ID not found.")

def list_students():
    print("\nStudents:")
    for student_id, info in students.items():
        print(f"ID: {student_id}, Name: {info['name']}, DOB: {info['dob']}")

def list_marks(student_id):
    if student_id in students:
        marks = students[student_id]['marks']
        print(f"\nMarks for {students[student_id]['name']}:")
        if marks:
            for subject, mark in marks.items():
                print(f"Subject: {subject}, Mark: {mark}")
        else:
            print("No marks available for this student.")
    else:
        print("Student ID not found.")

if __name__ == "_main_":
    while True:
        print("\n1. Add Student")
        print("2. Add Mark")
        print("3. List Students")
        print("4. List Marks")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            add_student(student_id, name, dob)
            print("Student added successfully.")

        elif choice == '2':
            student_id = input("Enter student ID: ")
            subject = input("Enter subject: ")
            mark = float(input("Enter mark: "))
            add_mark(student_id, subject, mark)
            print("Mark added successfully.")

        elif choice == '3':
            list_students()

        elif choice == '4':
            student_id = input("Enter student ID: ")
            list_marks(student_id)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")