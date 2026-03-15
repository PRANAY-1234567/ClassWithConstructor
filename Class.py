class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student name is", self.name)

s1 = Student("Rahul")
s2 = Student("Pranay")
s2.show()