#Generate Fibonacci Series
def fibonacci(n):
    a, b = 0, 1
    series = []
    while a < n:
        series.append(a)
        a, b = b, a + b
    return series
limit = int(input("Enter the upper limit for Fibonacci series: "))
print("Fibonacci series up to", limit, "is:", fibonacci(limit))

#Calculate Factorial Using a Loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {num} is: {factorial(num)}")


#Check if a Given Number is an Armstrong Number
def is_armstrong(number):
    num_str = str(number)
    power = len(num_str)
    return number == sum(int(digit) ** power for digit in num_str)
num = int(input("Enter a number to check if it is an Armstrong number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


#Check if a Given Number is a Perfect Number
def is_perfect(number):
    sum_divisors = sum(i for i in range(1, number) if number % i == 0)
    return sum_divisors == number
num = int(input("Enter a number to check if it is a perfect number: "))
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")


#Check if a Given Number is a Strong Number
from math import factorial
def is_strong(number):
    return number == sum(factorial(int(digit)) for digit in str(number))
num = int(input("Enter a number to check if it is a strong number: "))
if is_strong(num):
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")


# Print Multiplication Tables
def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
num = int(input("Enter a number to print its multiplication table: "))
print_multiplication_table(num)


#Calculate the LCM and GCD of Two Numbers
import math
def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
gcd_value = math.gcd(num1, num2)
lcm_value = lcm(num1, num2)
print(f"GCD of {num1} and {num2} is: {gcd_value}")
print(f"LCM of {num1} and {num2} is: {lcm_value}")