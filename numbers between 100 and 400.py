#  Write a Python program to find numbers between 100 and 400
#  (both included) where each digit of a number is an
#  even number. The numbers obtained should be printed in a
#  comma-separated sequence.
numbers = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        numbers.append(s)
print( ",".join(numbers))