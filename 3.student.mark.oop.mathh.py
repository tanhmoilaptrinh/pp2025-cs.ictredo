import math
import numpy as np

class Input:
    def __init__(self, num, id, name, mark=None):
        self.num = num
        self.id = id
        self.name = name
        self.__mark = mark

    def getmark(self):
        return self.__mark

    def setmark(self, mark):
        if 0 <= mark <= 10:
            self.__mark = mark
        else:
            print("Invalid mark!! Mark must be between 0 and 10.")
            self.__mark = None

class Student(Input):
    def __init__(self, num, id, name, DoB, mark=None):
        super().__init__(num, id, name, mark)
        self.DoB = DoB
        self.courses = {}  # Store course ids as keys and marks as values
        self.credits = {}  # Store course ids as keys and credits as values

    @staticmethod
    def InputStudent():
        student_list = []
        num = int(input("Enter number of students: "))
        for _ in range(num):
            id = str(input("Enter student's id: "))
            name = str(input("Enter student's name: "))
            DoB = str(input("Enter student's date of birth: "))
            student_list.append(Student(num, id, name, DoB))
        return student_list

    @staticmethod
    def showStudent(student_list):
        print("\nList of students: ")
        for student in student_list:
            print(f"ID: {student.id} Name: {student.name} Date of Birth: {student.DoB}")

class Course(Input):
    def __init__(self, num, id, name, mark=None):
        super().__init__(num, id, name, mark)

    @staticmethod
    def InputCourse():
        course_list = []
        num = int(input("Enter number of courses: "))
        for _ in range(num):
            id = str(input("Enter course id: "))
            name = str(input("Enter course name: "))
            course_list.append(Course(num, id, name))
        return course_list

    @staticmethod
    def showCourse(course_list):
        print("\nList of courses: ")
        for course in course_list:
            print(f"ID: {course.id} Name: {course.name}")

class Mark:
    def __init__(self, student, course, mark, credit):
        self.student = student
        self.course = course
        self.__mark = None
        self.setmark(mark)
        self.credit = credit

    def getmark(self):
        return self.__mark

    def setmark(self, mark):
        if 0 <= mark <= 10:
            self.__mark = mark
        else:
            print("Invalid mark!! Mark must be between 0 and 10.")
            self.__mark = None

    @staticmethod
    def InputMark(student_list, course_list):
        marks = {}
        print("This is all the courses: ")
        for course in course_list:
            print(f"Course: {course.name}, ID: {course.id}")
        choice = input("Enter course id: ")
        valid_course = None
        for course in course_list:
            if choice == course.id:
                valid_course = course
                marks[choice] = {}
                for student in student_list:
                    mark = float(input(f"Enter mark for {student.name} (ID: {student.id}): "))
                    credit = int(input(f"Enter credit for {course.name}: "))
                    # Directly store mark and credit for each student
                    student.courses[course.id] = mark
                    student.credits[course.id] = credit
                break

        if not valid_course:
            print("Invalid course ID!")
        return marks

    @staticmethod
    def show_marks(student_list, course_list, marks):
        course_id = input("\nEnter course ID to show marks: ")
        if course_id in marks:
            print(f"\nMarks for Course ID {course_id}:")
            for student in student_list:
                mark = marks[course_id].get(student.id, "N/A")
                print(f"{student.name} (ID: {student.id}) Mark: {math.floor(mark)}")
        else:
            print("Invalid course ID.")

    @staticmethod
    def calculate_gpa(student):
        marks = np.array(list(student.courses.values()))
        credits = np.array(list(student.credits.values()))
        weighted_sum = np.sum(marks * credits)
        total_credits = np.sum(credits)
        if total_credits > 0:
            return weighted_sum / total_credits
        else:
            return 0.0

    @staticmethod
    def sort_students_by_gpa(student_list):
        student_gpas = [(student, Mark.calculate_gpa(student)) for student in student_list]
        student_gpas.sort(key=lambda x: x[1], reverse=True)

        print("Sorted Students by GPA (Descending):")
        for student, gpa in student_gpas:
            print(f"ID: {student.id}, Name: {student.name}, GPA: {gpa:.2f}")

def main():
    student_list = []
    course_list = []
    marks = {}

    while True:
        print("\n----- MENU -----")
        print("1. Enter Students")
        print("2. Enter Courses")
        print("3. Enter Marks")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Marks")
        print("7. Sort Students by GPA")
        print("8. Exit")
        print("-----------------")
        choice = int(input("Please select an option: "))
        if choice == 1:
            student_list = Student.InputStudent()
        elif choice == 2:
            course_list = Course.InputCourse()
        elif choice == 3:
            marks = Mark.InputMark(student_list, course_list)
        elif choice == 4:
            Student.showStudent(student_list)
        elif choice == 5:
            Course.showCourse(course_list)
        elif choice == 6:
            Mark.show_marks(student_list, course_list, marks)
        elif choice == 7:
            Mark.sort_students_by_gpa(student_list)
        elif choice == 8:
            print("BYE BYE!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
