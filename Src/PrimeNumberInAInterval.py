# Python Program to Print all Prime Numbers in an Interval

# a = int(input("Enter initial number"))
# b = int(input("Enter final number"))
a = 2
b = 9568

print(f"Prime number between {a} and {b} are: ")

for i in range(a, b+1):
    if i > 1:
        for num in range(2, i):
            if i % num == 0:
                break
        else:
            print(i)