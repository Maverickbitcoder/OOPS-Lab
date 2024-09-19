#Check if a Given Number is a Disarium Number
def is_disarium(number):
    num_str = str(number)
    return number == sum(int(digit) ** (i + 1) for i, digit in enumerate(num_str))
num = int(input("Enter a number to check if it is a Disarium number: "))
if is_disarium(num):
    print(f"{num} is a Disarium number.")
else:
    print(f"{num} is not a Disarium number.")


#Determine Whether the Given Number is a Harshad Number
def is_harshad(number):
    digit_sum = sum(int(digit) for digit in str(number))
    return number % digit_sum == 0
num = int(input("Enter a number to check if it is a Harshad number: "))
if is_harshad(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")


#Print Armstrong Numbers from 1 to 1000
def is_armstrong(number):
    num_str = str(number)
    power = len(num_str)
    return number == sum(int(digit) ** power for digit in num_str)
print("Armstrong numbers from 1 to 1000 are:")
for num in range(1, 1001):
    if is_armstrong(num):
        print(num)


#Compute the Value of X^n
def power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result
x = float(input("Enter the value of X: "))
n = int(input("Enter the value of n: "))
result = power(x, n)
print(f"The value of {x} raised to the power {n} is: {result}")


#Calculate the Value of nCr
import math
def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
result = nCr(n, r)
print(f"The value of {n}C{r} is: {result}")
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
num = int(input("Enter a number to count the sum of its digits: "))
result = sum_of_digits(num)
print(f"The sum of digits in the number {num} is: {result}")

