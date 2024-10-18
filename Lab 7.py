# Define the Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create two instances of Person
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Print their name and age
print(f"Person 1: Name = {person1.name}, Age = {person1.age}")
print(f"Person 2: Name = {person2.name}, Age = {person2.age}")

## Define the Student class
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# Create an object of Student class and assign values
student = Student("John", 2)

# Print the details of the student
print(f"Student Name: {student.name}, Roll No: {student.roll_no}")

# Define the BankAccount class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance is {self.balance}.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"The current balance is {self.balance}.")

# Create a bank account object
account = BankAccount("Alice", 100)

# Perform operations
account.check_balance()
account.deposit(50)
account.withdraw(30)
account.check_balance()

# Define the Student class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create objects for different students
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Print details of the students
print(f"Student 1: Name = {student1.name}, Age = {student1.age}")
print(f"Student 2: Name = {student2.name}, Age = {student2.age}")