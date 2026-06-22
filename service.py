from repository import StudentRepository
from models import Student

class StudentService:
    def __init__(self, repository):
        self.repository = repository
        self.students = self.repository.load_students()

    def add_student(self, student_id, name, age, grade):
        if any(s.student_id == student_id for s in self.students):
            print("A student with this id already exists")
            return False

        self.students.append(Student(name, age, student_id, grade))
        self.repository.save_students(self.students)
        print("Student added successfully")
        return True

    def get_all_students(self):
        return self.students

    def update_student(self, student_id):
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

                self.repository.save_students(self.students)
                print("Student updated successfully.")
                return True
        print("Error: Student ID not found.")
        return False

    def delete_student(self, student_id):
        initial_count = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]

        if len(self.students) < initial_count:
            self.repository.save_students(self.students)
            print("Student removed successfully.")
            return True
        else:
            print("Error: Student ID not found.")
            return False

    def get_top_students(self, threshold=85):
        return [s for s in self.students if s.grade >= threshold]

    def sort_students(self):
        if not self.students:
            print("No students to sort.")
            return
        self.students.sort(key=lambda s: s.grade, reverse=True)
        self.repository.save_students(self.students)
        print("Roster sorted by highest grade first.")