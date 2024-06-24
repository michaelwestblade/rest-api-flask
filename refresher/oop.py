student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))

class Student(object):
    def __init__(self, name, age, grades):
        self.name = name
        self.grades = grades
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old."

    def __repr__(self):
        return f"<Person({self.name, self.age, self.grades})>"

    def average(self):
        return average(self.grades)


rolf = Student("Rolf", 35,  (89, 90, 93, 78, 90))
print(rolf.average())
print(rolf)
print(rolf.__repr__())