# A1: Student class with attributes and a method

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def describe(self):
        print(f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}")


# --- Test ---
s1 = Student("Alice", 20, "A")
s1.describe()

