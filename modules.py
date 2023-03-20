# Write a Python program to print the numbers of a specified list
# after removing even numbers from it.

# Program to print the numbers of a specified list after removing even numbers from it

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Original list:")
print(my_list)

# Using list comprehension
new_list = [number for number in my_list if number % 2 != 0]

print("\nList after removing even numbers:")
print(new_list)


# Write a Python program to find the length of a tuple.

# Program to find the length of a tuple

my_tuple = (1, 2, 3, 4, 5)

print("Length of the Tuple is: ")
print(len(my_tuple))