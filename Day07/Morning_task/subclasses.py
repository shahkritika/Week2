# A2: Teacher and Student subclasses overriding describe()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"Person: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def describe(self):
        print(f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def describe(self):
        print(f"Teacher: {self.name}, Age: {self.age}, Subject: {self.subject}")


# --- Test ---
s = Student("Bob", 19, "B+")
t = Teacher("Mr. Smith", 45, "Mathematics")
s.describe()
t.describe()

