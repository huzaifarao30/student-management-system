from repository import StudentRepository
from models import Student
from constants import (
    MSG_ID_EXISTS, 
    MSG_STUDENT_ADDED, 
    MSG_STUDENT_NOT_FOUND,
    MSG_STUDENT_REMOVED, 
    MSG_STUDENT_UPDATED, 
    MSG_NO_STUDENTS_TO_SORT,
    MSG_SORTED,
    MSG_UPDATING,
    MSG_INVALID_FIELD_VALUE
)


class StudentService:
    def __init__(self, repository):
        self.repository = repository
        self.students = self.repository.load_students()

    def add_student(self, student_id, name, age, grade):
        if any(s.student_id == student_id for s in self.students):
            print(MSG_ID_EXISTS)
            return False

        self.students.append(Student(name, age, student_id, grade))
        self.repository.save_students(self.students)
        print(MSG_STUDENT_ADDED)
        return True

    def get_all_students(self):
        return self.students

    def update_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                print(MSG_UPDATING.format(s.name))

                updatable_fields = {
                    "name": str,
                    "age": int,
                    "grade": float
                }

                for field, data_type in updatable_fields.items():
                    current_value = getattr(s, field)
                    prompt = f"Enter new {field} [{current_value}]: "
                    
                    new_value = input(prompt).strip()
                    
                    if new_value:
                        try:
                            converted_value = data_type(new_value)
                            setattr(s, field, converted_value)
                        except ValueError:
                            print(MSG_INVALID_FIELD_VALUE.format(field))  # ← Now using constant

                self.repository.save_students(self.students)
                print(MSG_STUDENT_UPDATED)
                return True
        
        print(MSG_STUDENT_NOT_FOUND)
        return False

    def delete_student(self, student_id):
        initial_count = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]

        if len(self.students) < initial_count:
            self.repository.save_students(self.students)
            print(MSG_STUDENT_REMOVED)
            return True
        else:
            print(MSG_STUDENT_NOT_FOUND)
            return False

    def get_top_students(self, threshold=85):
        return [s for s in self.students if s.grade >= threshold]

    def sort_students(self):
        if not self.students:
            print(MSG_NO_STUDENTS_TO_SORT)
            return
        
        self.students.sort(key=lambda s: s.grade, reverse=True)
        self.repository.save_students(self.students)
        print(MSG_SORTED)