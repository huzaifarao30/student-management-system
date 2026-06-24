import os
import json
from .models import Student

class StudentRepository:
    def __init__(self, filename="Studentlist.json"):
        self.filename = filename

    def load_students(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Student.from_dict(s) for s in data]
        except Exception as e:
            print(f"Loading error: {e}")
            return []

    def save_students(self, students):
        try:
            data = [student.to_dict() for student in students]
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False