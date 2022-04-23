# Python Program to Check Leap Year

a = int(input("Enter a year."))

if a % 4 == 0:
    print(f"{a} is a leap year")
else:
    print(f"{a} is not a leap year")