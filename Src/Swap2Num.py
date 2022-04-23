# Python Program to Swap Two Variables

num1 = int(input("Enter an number. \n"))
num2 = int(input("Enter a number. \n"))

print(f"Number 1 = {num1} \n Number 2 = {num2}")

swapNum = num1
num1 = num2
num2 = swapNum
"""
Or we can use
# num1 , num2 = num2, num1
"""

print(f"After swaping \n Number 1 = {num1} \n Number 2 = {num2}")