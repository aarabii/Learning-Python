# Python Program to Find the Factorial of a Number

a = 6

factorial = 1

if a < 0:
    print(f"Factorial doest exist for negative numbers.")
elif a == 0:
    print(f"Factorial of 0 is 1")
else:
    for i in range(1, a + 1):
        factorial = factorial*i
    print(f"Factorial of {a} is {factorial}")
