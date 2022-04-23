# Python Program to Find Factorial of Number Using Recursion
def factorial_recursion(n):
    if n <= 0:
        return n
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial = factorial*i
        return factorial

n = 0

if n < 0:
    print("Enter a positive number")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    print(f"Factorial of {n} is {factorial_recursion(n)}")