# Python Program to Convert Decimal to Binary Using Recursion
"""
Decimal number is converted into binary by dividing the number successively by 2
and printing the remainder in reverse order.
"""


def convertToBinary(n):
    if n > 1:
        convertToBinary(n // 2)
    print(n % 2, end='')


dec_num = 568
convertToBinary(dec_num)
print()
