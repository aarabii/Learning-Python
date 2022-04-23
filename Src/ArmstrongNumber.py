# Python Program to Check Armstrong Number
"""

A positive integer is called an Armstrong number of order n if
# abcd... = an + bn + cn + dn + ...
In case of an Armstrong number of 3 digits,
the sum of cubes of each digit is equal to the number itself.
For example: 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

"""
num = int(input("Enter a number. "))
num_copy = num

sum_num = 0
order = len(str(num))

while num_copy > 0:
    digit = num_copy % 10
    sum_num += digit ** order
    num_copy = num_copy // 10

if sum_num == num:
    print(f"{num} is a Armstrong number")
else:
    print(f"{num} is not a Armstrong number")
