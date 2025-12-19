
def add_student(students):
    name = input("Enter student name: ")
    score = float(input("Enter student score (0-100): "))
    students[name] = score
    print(f"Student {name} added successfully!\n")

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def display_students(students):
    print("\n--- Student Details ---")
    for name, score in students.items():
        grade = calculate_grade(score)
        print(f"Name: {name}, Score: {score}, Grade: {grade}")
    print("------------------------\n")

def average_score(students):
    if students:
        avg = sum(students.values()) / len(students)
        print(f"Average Score: {avg:.2f}\n")
    else:
        print("No students to calculate average.\n")

def main():
    students = {}
    while True:
        print("1. Add Student")
        print("2. Display Students and Grades")
        print("3. Show Average Score")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            average_score(students)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

main()
