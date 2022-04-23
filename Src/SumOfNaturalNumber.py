# Python Program to Find the Sum of Natural Numbers

# a = int(input("Enter a number"))
a = 100

if a < 0:
    print("Enter a positive number")
else:
    sum = 0
    while a > 0:
        sum += a
        a -= 1
    print(f"The sum of first n term is {sum}")
