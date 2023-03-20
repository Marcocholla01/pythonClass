# Write a Python function to calculate the factorial of a number
# (a non-negative integer). The function accepts the number as an argument.

# function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Write a Python function to multiply all the numbers in a list
# function to multiply all the numbers in a list
def multiply_list(my_list):
    result = 1
    for x in my_list:
        result = result * x
    return result

# testing the functions
num = 5
print("Factorial of", num, "is", factorial(num))

nums = [1, 2, 3, 4]
print("Product of all the numbers in the list is:", multiply_list(nums))

