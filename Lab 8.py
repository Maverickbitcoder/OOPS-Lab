#To create a ComplexNumber class in Python
import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, c):
        return ComplexNumber(self.real + c.real, self.imaginary + c.imaginary)

    def magnitude(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


# Creating two complex numbers
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

# Adding the complex numbers
result = c1.add(c2)

# Displaying the results
print("First Complex Number:", c1)
print("Second Complex Number:", c2)
print("Sum:", result)
print("Magnitude of First Complex Number:", c1.magnitude())
print("Magnitude of Second Complex Number:", c2.magnitude())
print("Magnitude of Sum:", result.magnitude())

#to create a Person class and a Student subclass in Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_details(self):
        # Displaying all details including student_id
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")


# Example usage
p1 = Person("Alice", 30)
p1.display()

s1 = Student("Bob", 20, "S12345")
s1.show_details()

# To implement multilevel inheritance with the Vehicle, Car, and ElectricCar classes in Python.
class Vehicle:
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def car_info(self):
        print("This is a car")

class ElectricCar(Car):
    def battery_info(self):
        print("This car has a battery")


# Creating an ElectricCar object and calling all methods to demonstrate multilevel inheritance
electric_car = ElectricCar()
electric_car.info()          # From Vehicle class
electric_car.car_info()       # From Car class
electric_car.battery_info()   # From ElectricCar class

#To implement the Teacher and Author classes with their own description() methods and create a subclass TutorAuthor that inherits from both
class Teacher:
    def description(self):
        print("This is a Teacher, responsible for educating students.")

class Author:
    def description(self):
        print("This is an Author, responsible for writing books or articles.")

class TutorAuthor(Teacher, Author):
    def description(self):
        # Calling the description method from each parent class explicitly
        super(Teacher, self).description()  # Calls Author's description
        super(Author, self).description()   # Calls Teacher's description


# Creating a TutorAuthor object and calling description to demonstrate multiple inheritance
tutor_author = TutorAuthor()
tutor_author.description()

#to implement the Animal, Dog, and Cat classes in Python to demonstrate hierarchical inheritance, where both Dog and Cat inherit from Animal.
class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Creating objects of Dog and Cat and calling their sound methods
dog = Dog()
cat = Cat()

print("Dog Sound:")
dog.sound()  # Calls Dog's version of sound()

print("Cat Sound:")
cat.sound()  # Calls Cat's version of sound()