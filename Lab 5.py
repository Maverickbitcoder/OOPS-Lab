#1. Write a Python program to triple all numbers in a given list of integers. Use Python map.
def triple_numbers(lst):
    return list(map(lambda x: x * 3, lst))

numbers = [1, 2, 3, 4, 5]
print(triple_numbers(numbers))

#2. Write a Python program to add three given lists using Python map and lambda.
def add_three_lists(lst1, lst2, lst3):
    return list(map(lambda x, y, z: x + y + z, lst1, lst2, lst3))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
print(add_three_lists(list1, list2, list3))
#3. Write a Python program to listify the list of given strings individually using Python map.
def listify_strings(lst):
    return list(map(list, lst))

strings = ['apple', 'banana', 'cherry']
print(listify_strings(strings))
#4. Write a Python program to create a list containing the power of said number in bases raised
def power_by_index(lst):
    return list(map(lambda x, idx: x ** idx, lst, range(len(lst))))

numbers = [2, 3, 4, 5]
print(power_by_index(numbers))
#5. Write a Python program to square the elements of a list using the map() function.
def square_elements(lst):
    return list(map(lambda x: x ** 2, lst))

numbers = [1, 2, 3, 4, 5]
print(square_elements(numbers))
#6. Write a Python program to convert all the characters into uppercase and lowercase
#eliminate duplicate letters from a given sequence. Use the map() function.
def convert_case_and_remove_duplicates(sequence):
    unique_chars = set(sequence)
    return list(map(lambda x: (x.upper(), x.lower()), unique_chars))

sequence = "HelloWorld"
print(convert_case_and_remove_duplicates(sequence))
#7. Write a Python program to add two given lists and find the dimap() function.
def add_and_difference(lst1, lst2):
    added = list(map(lambda x, y: x + y, lst1, lst2))
    diff = list(map(lambda x, y: x - y, lst1, lst2))
    return added, diff

list1 = [10, 20, 30]
list2 = [1, 2, 3]
added, diff = add_and_difference(list1, list2)
print("Added:", added)
print("Difference:", diff)
#8. Write a Python program to convert a given list of integers and a tuple of integers in a list of
def convert_to_strings(lst, tpl):
    return list(map(str, lst)) + list(map(str, tpl))

numbers_list = [10, 20, 30]
numbers_tuple = (40, 50, 60)
print(convert_to_strings(numbers_list, numbers_tuple))
#9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to an integer.
def specific_elements_and_convert(tpl, indices):
    return list(map(int, [tpl[i] for i in indices]))

tuple_of_numbers = ('1', '2', '3', '4', '5')
indices = [1, 3]
print(specific_elements_and_convert(tuple_of_numbers, indices))
#10. Write a Python program to compute the square of the first N Fibonacci numbers, using themap function and generate a list of the numbers.def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def square_fibonacci(n):
    fib_numbers = fibonacci(n)
    return list(map(lambda x: x ** 2, fib_numbers))

print(square_fibonacci(10))

#11. Write a Python program to compute the sum of elements of an array of integers. Use the map() function.
from functools import reduce

def sum_of_elements(lst):
    return reduce(lambda x, y: x + y, lst)

numbers = [1, 2, 3, 4, 5]
print(sum_of_elements(numbers))