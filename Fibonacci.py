# Write a Python program to get the Fibonacci series between 0 to 50.
# Go to the editor Note : The Fibonacci Sequence is the series of
# numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it

# Fibonacci series
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

    # Driver program


print("Fibonacci series:")
for i in range(51):
    print(fibonacci(i))