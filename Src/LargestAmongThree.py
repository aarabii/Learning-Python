# Python Program to Find the Largest Among Three Numbers

# a = int(input("Enter a number"))
# b = int(input("Enter a number"))
# c = int(input("Enter a number"))

a = 5
b = 3
c = 9

if a > b and a > c:
    print(f"{a} is the largest number among {a}, {b} and {c}")
elif b > a and b > c:
    print(f"{b} is the largest number among {a}, {b} and {c}")
else:
    print(f"{c} is the largest number among {a}, {b} and {c}")
