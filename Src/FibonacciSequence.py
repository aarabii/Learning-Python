# Python Program to Print the Fibonacci sequence
"""
A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....

The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.
This means to say the nth term is the sum of (n-1)th and (n-2)th term.
"""
num = int(input("Enter the number of terms. "))

# First two term
a, b = 0, 1
c = 0

if num <= 0:
    print("Fibonacci sequence doesn't exist for negative term or zero")
else:
    print(f"Fibonacci sequence upto {num} term are: ")
    while c < num:
        print(a)
        nTerm = a + b
        a, b = b, nTerm  # updating values
        c += 1
