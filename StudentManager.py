import os
import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def toDict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
        }


class StudentManagementSystem:
    def __init__(self, filename="Studentlist.json"):
        self.filename = filename
        self.students = []
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.students = [
                    Student(s["name"], s["age"], s["id"], s["grade"]) for s in data
                ]
        except Exception as e:
            print(f"Loading error: {e}")

    def save_data(self):
        try:
            with open(self.filename, "w") as file:
                data = [student.toDict() for student in self.students]
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def addStudent(self, student_id, name, age, grade):
        if any(s.student_id == student_id for s in self.students):
            print("A student with this id already exists")
            return

        self.students.append(Student(name, age, student_id, grade))
        self.save_data()
        print("Student added successfully")

    def viewStudents(self):
        if not self.students:
            print("No students in the system")
            return
        print("\n-------------- Students Details -------------")
        for s in self.students:
            print(f"ID: {s.student_id} | Name: {s.name} | Age: {s.age} | Grade: {s.grade}")

    def updateStudent(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                print(f"Updating data for {s.name} (Leave blank if you don't want to change)")

                new_name = input(f"Enter new name [{s.name}]: ")
                if new_name:
                    s.name = new_name

                new_age = input(f"New Age [{s.age}]: ")
                if new_age:
                    s.age = int(new_age)

                new_grade = input(f"New Grade [{s.grade}]: ")
                if new_grade:
                    s.grade = float(new_grade)

                self.save_data()
                print("Student updated successfully.")
                return
        print("Error: Student ID not found.")

    def deleteStudent(self, student_id):
        initial_count = len(self.students)

        self.students = [s for s in self.students if s.student_id != student_id]

        if len(self.students) < initial_count:
            self.save_data()
            print("Student removed successfully.")
        else:
            print("Error: Student ID not found.")

    def showTopStudents(self, threshold=85):
        top = [s for s in self.students if s.grade >= threshold]

        if not top:
            print(f"No students have a grade of {threshold} or higher.")
            return

        print(f"\n--- Top Students (Grade >= {threshold}) ---")
        for s in top:
            print(f"{s.name}: {s.grade}")

    def sortStudents(self):
        if not self.students:
            print("No students to sort.")
            return

        self.students.sort(key=lambda s: s.grade, reverse=True)
        self.save_data()
        print("Roster sorted by highest grade first.")
        self.viewStudents()


def main():
    system = StudentManagementSystem()

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

        match choice:
            case "1":
                while True:
                    s_id_input = input("Enter Student ID (Numbers only): ")
                    try:
                        s_id = int(s_id_input)
                        break  
                    except ValueError:
                        print("Error: Student ID must be a whole number. Try again.")
                name = input("Enter Name: ")
                try:
                    age = int(input("Enter Age: "))
                    grade = float(input("Enter Grade: "))
                    system.addStudent(s_id, name, age, grade)
                except ValueError:
                    print("Error: Age and Grade must be valid numbers.")

            case "2":
                system.viewStudents()

            case "3":
                while True:
                    s_id_input = input("Enter Student ID (Numbers only): ")
                    try:
                        s_id = int(s_id_input)
                        break
                    except ValueError:
                        print("Error: Student ID must be a whole number. Try again.")
                system.updateStudent(s_id)

            case "4":
                while True:
                    s_id_input = input("Enter the ID of the student to remove: ")
                    try:
                        s_id = int(s_id_input)
                        break
                    except ValueError:
                        print("Error: Student ID must be a whole number. Try again.")
                        
                system.deleteStudent(s_id)

            case "5":
                system.sortStudents()

            case "6":
                system.showTopStudents()

            case "7":
                print("Shutting down system...")
                break

            case _:
                print("Invalid choice. Please select a valid number.")


if __name__ == "__main__":
    main()