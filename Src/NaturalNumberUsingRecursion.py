# Python Program to Find Sum of Natural Numbers Using Recursion
"""
A recursive function is a function in code that refers to itself for execution.
Recursive functions can be simple or elaborate.
They allow for more efficient code writing, for instance,
in the listing or compiling of sets of numbers, strings or other variables through a single reiterated process.
"""
def recursion_num(n):
    if n <= 1:
        return n
    else:
        return n + recursion_num(n-1)

num = 4

if num < 0:
    print("Please enter a positive number")
else:
    print(f"Sum is {recursion_num(num)}")