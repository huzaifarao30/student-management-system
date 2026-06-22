from repository import StudentRepository
from service import StudentService

def main():
    repo = StudentRepository()
    service = StudentService(repo)

    while True:
        print("\n---------------- Student Management System ---------------------")
        print("1. Add Student")
        print("2. View Roster")
        print("3. Update Student")
        print("4. Remove Student")
        print("5. Sort Roster by Grade (Lambda)")
        print("6. Show Top Students (Comprehension)")
        print("7. Exit")

        choice = input("Select an option (1-7): ")

        if choice == "1":
            while True:
                try:
                    s_id = int(input("Enter Student ID (Numbers only): "))
                    break
                except ValueError:
                    print("Error: Student ID must be a whole number. Try again.")
            
            name = input("Enter Name: ")
            try:
                age = int(input("Enter Age: "))
                grade = float(input("Enter Grade: "))
                service.add_student(s_id, name, age, grade)
            except ValueError:
                print("Error: Age and Grade must be valid numbers.")

        elif choice == "2":
            students = service.get_all_students()
            if not students:
                print("No students in the system")
            else:
                print("\n-------------- Students Details -------------")
                for s in students:
                    print(f"ID: {s.student_id} | Name: {s.name} | Age: {s.age} | Grade: {s.grade}")

        elif choice == "3":
            while True:
                try:
                    s_id = int(input("Enter Student ID (Numbers only): "))
                    break
                except ValueError:
                    print("Error: Student ID must be a whole number. Try again.")
            service.update_student(s_id)

        elif choice == "4":
            while True:
                try:
                    s_id = int(input("Enter the ID of the student to remove: "))
                    break
                except ValueError:
                    print("Error: Student ID must be a whole number. Try again.")
            service.delete_student(s_id)

        elif choice == "5":
            service.sort_students()
            students = service.get_all_students()
            if students:
                print("\n-------------- Students Details -------------")
                for s in students:
                    print(f"ID: {s.student_id} | Name: {s.name} | Age: {s.age} | Grade: {s.grade}")

        elif choice == "6":
            top = service.get_top_students()
            if not top:
                print("No students have a grade of 85 or higher.")
            else:
                print("\n--- Top Students (Grade >= 85) ---")
                for s in top:
                    print(f"{s.name}: {s.grade}")

        elif choice == "7":
            print("Shutting down system...")
            break

        else:
            print("Invalid choice. Please select a valid number.")


if __name__ == "__main__":
    main()