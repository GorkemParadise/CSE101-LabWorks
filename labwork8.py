# 1. Basic Class & String Parsing

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

p1 = Student("Alice", 21)
print(p1)


# 2. Class vs. Instance State

class Course():
    total_courses = 0 
    def __init__(self, title,):
        self.title = title
        self.students = []
        Course.total_courses += 1
    def enroll(self, student):
        self.students.append(student)
    @classmethod
    def get_total_courses(cls):
        return cls.total_courses
course1 = Course("Math")
course2 = Course("Science")
print(f"Total Courses: {Course.get_total_courses()}")


# 3. Typed Collections & Properties

class Gradebook():
    def __init__(self):
        self._grades = {}
        self._students = []
    def add_grade(self, student_name: str, grade: float):
        if 0 <= grade <= 100:
            self._grades[student_name] = grade
            self._students.append(student_name)
    def average_grade(self) -> float:
        total = sum(self._grades.values())
        count = len(self._grades)
        return total / count if count > 0 else 0
    
gradebook = Gradebook()
gradebook.add_grade("Mehmet", 90.5)
gradebook.add_grade("Ali", 85.0)
print(f"Students: {gradebook._students}")
print(f"Average Grade: {gradebook.average_grade()}")


# 4. Composition with Data Normalization

class Roster():
    def __init__(self, student_tuples):
        self.students = {}
        self.gradebooks = {}
        for name, age in student_tuples:
            student = Student(name.title(), age)
            self.students[name.lower()] = student
            self.gradebooks[name.lower()] = Gradebook()
    def record(self, name, score):
        key = name.lower()
        if key not in self.gradebooks:
            raise KeyError(f"Student '{name}' not found.")
        self.gradebooks[key].add_grade(name.title(), score)
    def top_student(self):  
        top_student = None
        highest_avg = -1
        for key, gradebook in self.gradebooks.items():
            avg = gradebook.average_grade()
            if avg > highest_avg:
                highest_avg = avg
                top_student = self.students[key]
        return top_student
    
roster = Roster([("atıl", 20), ("babum", 22), ("paradise", 23)])
roster.record("Atıl", 95)
roster.record("Babum", 85)
roster.record("Paradise", 90)
top_student = roster.top_student()
print(f"Top Student: {top_student}")