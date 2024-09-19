# Check if a Number is Prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
num = int(input("Enter a number to check if it is prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


#palindrome number
def is_palindrome(number):
    return str(number) == str(number)[::-1]
num = int(input("Enter a number to check if it is a palindrome: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


#Grade calculator
def find_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'
percentage = float(input("Enter the percentage: "))
grade = find_grade(percentage)
print(f"The grade for {percentage}% is: {grade}")