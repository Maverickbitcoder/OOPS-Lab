# Number Triangle Pattern
n = 5
for i in range(1, n + 1):
    print((str(i) + ' ') * i)


# Inverted Pyramid of Numbers
n = 5
for i in range(1, n + 1):
    print(' ' * (i - 1) + (str(i) + ' ') * (n - i + 1))


# Inverted Pyramid of the Same Digit
n = 5
for i in range(n):
    print(' ' * (2 * i) + (str(n) + ' ') * (n - i))


# Reverse Pyramid of Numbers
n = 5
for i in range(1, n + 1):
    print(' ' * (2 * (n - i)) + ' '.join(str(j) for j in range(i, 0, -1)))


# Connected Inverted Pyramid Pattern of Numbers
n = 5
for i in range(n):
    left_part = ' '.join(str(n - j) for j in range(i + 1))  # Left part of the pattern
    right_part = ' '.join(str(j + 1) for j in range(i, n))  # Right part of the pattern
    print(left_part + ' ' + right_part)


# Pyramid of Horizontal Tables
n = 7
for i in range(n):
    print(' '.join(str(i * j) for j in range(i + 1)))


# Downward Triangle Pattern of Stars
n = 6
for i in range(n):
    print(' ' * i + '* ' * (n - i))


#Write a program to do the following
#A. To separate the following string into comma (,) separated values. X= “ India.is.my.country”
#B. To remove a given character from a string. Y=”M.A.N.I.P.A.L”
#C. To remove the (.) dots from the above string.
#X = "India.is.my.country"
separated_X = ','.join(X.split('.'))
print("A. Comma separated values:", separated_X)
Y = "M.A.N.I.P.A.L"
char_to_remove = '.'
removed_char_Y = Y.replace(char_to_remove, '')
print("B. String after removing '.':", removed_char_Y)
removed_dots_Y = Y.replace('.', '')
print("C. String after removing dots:", removed_dots_Y)


# Program to sort strings alphabetically
strings = ["banana", "apple", "cherry", "date", "grape", "fig"]
sorted_strings = sorted(strings)
print("Sorted strings alphabetically:", sorted_strings)



# Program to reverse a user input string
user_input = input("Enter a string: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)


# Program to check if a string contains only digits
user_input = input("Enter a string: ")
if user_input.isdigit():
    print("The string contains only digits.")
else:
    print("The string contains characters other than digits.")


# Program to find the number of vowels in a string
user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in user_input:
    if char in vowels:
        vowel_count += 1
print("Number of vowels in the string:", vowel_count)