# Python Program to Find Armstrong Number in an Interval

# num1 = int(input("Enter the starting of a interval"))
# num2 = int(input("Enter the end of the interval"))
num1 = 10
num2 = 1000

print(f"Armstrong Number from {num1} to {num2} are: ")
for i in range(num1, num2 + 1):
    order = len(str(i))
    sum_num = 0

    copy_num = i

    while copy_num > 0:
        digit = copy_num % 10
        sum_num += digit ** order
        copy_num //= 10

    if i == sum_num:
        print(i)