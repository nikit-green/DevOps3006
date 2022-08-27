from decimal import Decimal

# K - Triangle
n = 5
for i in range(n):
    for j in range(i + 1):
        print('#', end=" ")
    print()

# L - X shape
n = 7
for i in range(n):
    for j in range(n):
        if (i == j) or (i + j == n - 1):
            print('#', end=" ")
        else:
            print(" ", end=' ')
    print()


# M - Function to Function
def rec_num():
    num = input("Enter your number: ")
    sum_num(num)


def sum_num(x):
    print(sum(Decimal(a) for a in x))


rec_num()
