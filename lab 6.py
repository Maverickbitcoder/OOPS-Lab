#code in python for the inbuilt function of list 6 fundction
# Define a sample list
my_list = [5, 3, 8, 1, 2]

# 1. append() - Adds an element to the end of the list
my_list.append(10)
print("After append(10):", my_list)

# 2. insert() - Inserts an element at a specific position
my_list.insert(2, 7)  # Insert 7 at index 2
print("After insert(2, 7):", my_list)

# 3. remove() - Removes the first occurrence of an element
my_list.remove(8)  # Remove the element 8
print("After remove(8):", my_list)

# 4. pop() - Removes and returns the last element (or an element at a specific index)
popped_element = my_list.pop()  # Removes the last element
print("After pop():", my_list, "- Popped element:", popped_element)

# 5. sort() - Sorts the list in ascending order
my_list.sort()
print("After sort():", my_list)

# 6. reverse() - Reverses the elements of the list
my_list.reverse()
print("After reverse():", my_list)

# Function to take a list as an argument and return the sum of its elements
def sum_of_list(numbers):
    total = sum(numbers)
    return total

# Define a list
my_list = [10, 20, 30, 40, 50]

# Call the function and pass the list as an argument
result = sum_of_list(my_list)

print("The sum of the list is:", result)

# Function to take variable-length arguments and return the cube of each
def cube_of_elements(*args):
    cubes = [x**3 for x in args]  # Compute cube for each argument
    return cubes

# Call the function with multiple arguments
result = cube_of_elements(1, 2, 3, 4, 5)

# Print the result
print("The cube of each element is:", result)


# Recursive function to solve Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary, using target as auxiliary
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    # Move n-1 disks from auxiliary to target, using source as auxiliary
    tower_of_hanoi(n-1, auxiliary, source, target)

# Number of disks
n = 3
# Names of the rods (source, auxiliary, target)
tower_of_hanoi(n, 'A', 'B', 'C')


# Function to calculate uppercase and lowercase letters
def count_upper_lower(s):
    upper_count = 0
    lower_count = 0

    # Loop through each character in the string
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    # Return the counts
    return upper_count, lower_count


# Example string
x = "Hello World"

# Call the function and pass the string
upper, lower = count_upper_lower(x)

# Print the results
print(f"String: {x}")
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")