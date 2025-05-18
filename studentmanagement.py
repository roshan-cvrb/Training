import json, os

class Student:
    def __init__(self, s_id, s_name, s_course, s_score):
        self.id = s_id
        self.name = s_name
        self.course = s_course
        self.score = s_score

    def to_dict(self):
        return {"id": self.id, "name": self.name, "course": self.course, "score": self.score}

    def __str__(self):
        return f"{self.id}: {self.name}, {self.course}, {self.score}"

class StudentManagement(Student):
    students = {}

    @classmethod
    def load(cls, file="students.json"):
        if os.path.exists(file):
            with open(file) as f:
                for s_id, s in json.load(f).items():
                    cls.students[s_id] = Student(**s)

    @classmethod
    def save(cls, file="students.json"):
        with open(file, "w") as f:
            json.dump({i: s.to_dict() for i, s in cls.students.items()}, f)

    @classmethod
    def add(cls, s_id, s_name, s_course, s_score):
        cls.students[s_id] = Student(s_id, s_name, s_course, s_score)
        cls.save()
        print("Added.")

    @classmethod
    def view(cls, s_id=None):
        if not s_id:
            if cls.students:
                for s in cls.students.values():
                    print(s)
            else:
                print("No students found.")
        else:
            print(cls.students.get(s_id, "Not found."))

    @classmethod
    def update(cls, s_id, s_name=None, s_course=None, s_score=None):
        s = cls.students.get(s_id)
        if s:
            if s_name: s.name = s_name
            if s_course: s.course = s_course
            if s_score: s.score = s_score
            cls.save()
            print("Updated.")
        else:
            print("Not found.")

    @classmethod
    def delete(cls, s_id):
        if cls.students.pop(s_id, None):
            cls.save()
            print("Deleted.")
        else:
            print("Not found.")

if __name__ == "__main__":
    StudentManagement.load()
    while True:
        c = input("add/view/update/delete/exit: ")
        if c == "add":
            StudentManagement.add(input("id: "), input("name: "), input("course: "), input("score: "))
        elif c == "view":
            s_id = input("id (leave blank for all): ")
            StudentManagement.view(s_id if s_id else None)
        elif c == "update":
            s_id = input("id: ")
            StudentManagement.update(
                s_id,
                input("new name (blank=skip): ") or None,
                input("new course (blank=skip): ") or None,
                input("new score (blank=skip): ") or None
            )
        elif c == "delete":
            StudentManagement.delete(input("id: "))
        elif c == "exit":
            break
        else:
            print("Invalid choice")