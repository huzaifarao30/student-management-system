class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"], 
            data["age"], 
            data["id"], 
            data["grade"]
        )