def InputStudent():
    student = []
    num_student = int(input("Enter number of student: "))
    for i in range(num_student):
        id = str(input("Enter id: "))
        student_name = str(input("Enter student name: "))
        DoB = str(input("Enter student DoB: "))
        student.append((id, student_name, DoB))
    return student   

def InputCourse():
    course = []
    num_course = int(input("Enter number of course"))
    for i in range(num_course):
        id_course = str(input("Enter course id: "))
        name_course = str(input("Enter course name: "))
        course.append((id_course,name_course))
    return course

def InputMark(student, course):
    marks = {}
    print("this is all the course: ")
    for (id_course, name_course) in course:
        print( {name_course},{id_course})
    choice = input("Enter course id: ")
    valid_course = False
    for id_course, name_course in course:
        if choice == id_course:
            valid_course = True
            marks[choice] = {}
            for id, student_name, _ in student:
                mark = float(input(f"Enter mark for {student_name} (ID: {id}): "))
                marks[choice][id] = mark
            break
    
    if not valid_course:
        print("Invalid course ID!")
    return marks
    
def showStudent(student):
    print("\nList of student: ")
    for (id, student_name, DoB) in student:
        print(f"ID: {id} Name: {student_name}  Date of Birth: {DoB}")

def showCourse(course):
    print("\n List of the course: ")
    for (id_course,name_course) in course:
        print(f"ID {id_course} Name: {name_course}")

def show_marks(student, course, marks):
    course_id = input("\nEnter course ID to show marks: ")
    if course_id in marks:
        print(f"\nMarks for Course ID {course_id}:")
        for id, student_name, _ in student:
            mark = marks[course_id].get(id, "N/A")
            print(f"{student_name} (ID: {id}): {mark}")
    else:
        print("Invalid course ID.")

def main():
    student = InputStudent()
    course = InputCourse()
    marks = InputMark(student, course)

    while (1):
        print("-----MENU-----")
        print("1. List course")
        print("2. List student")
        print("3. Show mark")
        print("0. Exit") 
        print("----------------")
        choice = int(input("Choose an option: "))   
        if choice == 1:
            showCourse(course)
        elif choice == 2:
            showStudent(student)
        elif choice == 3:
            show_marks(student, course, marks)
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()