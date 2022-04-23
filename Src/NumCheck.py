# Python Program to Check if a Number is Positive, Negative or 0

num1 = float(input("Enter a number."))

if num1 > 0:
    print(f"{num1} is a positive number")
elif num1 == 0:
    print("Zero")
else:
    print(f"{num1} is negative number")