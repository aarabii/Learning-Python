# Python Program to Solve Quadratic Equation

import cmath

num1 = float(input("Enter the value of a"))
num2 = float(input("Enter the value of b"))
num3 = float(input("Enter the value of c"))

# c = 1
# b = 3
# a = 6

determinant = (b**2) - (4*a*c) #b^2-4ac

if determinant > 0:
    print("Roots are real and different")
elif determinant == 0:
    print("Roots are real and equal")
else:
    print("Roots are imaginary and different")

root1 = (-b-cmath.sqrt(determinant))/(2*a)
root2 = (-b+cmath.sqrt(determinant))/(2*a)

print(f"Roo1 = {root1} \nRoot2 = {root2}")