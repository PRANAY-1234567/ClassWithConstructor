📘 Python Program: Class with Constructor (Student Example)

📌 Overview

This Python program demonstrates Object-Oriented Programming (OOP) concepts using a class, constructor, and object.

The program creates a Student class that stores a student's name and displays it using a method.

⚙️ Source Code
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student name is", self.name)

s1 = Student("Rahul")
s1.show()
🧠 How the Program Works
1️⃣ Create a Class
class Student:

A class is a blueprint used to create objects.

Here, Student represents a student entity.

2️⃣ Constructor Method
def __init__(self, name):

__init__() is a constructor in Python.

It runs automatically when an object is created.

It initializes the object’s attributes.

3️⃣ Instance Variable
self.name = name

self.name stores the name of the student.

self refers to the current object.

4️⃣ Method to Display Data
def show(self):
    print("Student name is", self.name)

This method prints the student's name.

5️⃣ Create an Object
s1 = Student("Rahul")

s1 is an object (instance) of the Student class.

"Rahul" is passed to the constructor as the name.

6️⃣ Call the Method
s1.show()

The object calls the show() method to display the student's name.

▶️ Output
Student name is Rahul
🔑 Key Concepts Demonstrated

Classes

Objects (Instances)

Constructors (__init__)

Instance variables

Methods

self keyword

⏱️ Time Complexity

O(1) — The program executes a constant number of operations.

🚀 Possible Enhancements
Multiple Students Example
s1 = Student("Rahul")
s2 = Student("Priya")

s1.show()
s2.show()

Output:

Student name is Rahul
Student name is Priya

📚 Learning Outcome

After studying this program, you will understand:

How classes and objects work in Python

How to use a constructor to initialize data

How methods interact with object attributes
