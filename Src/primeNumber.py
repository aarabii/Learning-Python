# Python Program to Check Prime Number

a = int(input("Enter a number"))

flag = False
"""

A flag is a variable used to have some value until some condition becomes true,
then we change it to false and print the output (Initially flag considered as true)

"""

if a > 1:
    for i in range(2, a):
        if 2 % i == 0:
            flag = True
            break

if flag:
    print(f"{a} is not a prime number")
else:
    print(f"{a} is a prime number")