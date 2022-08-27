# A - Check if < / > / =
x = int(input("Enter First Number:"))
y = int(input("Enter Second Number:"))
if x > y:
    print("BIG")
elif x < y:
    print("small")
else:
    print("Equal")

# B - for loop
for i in range(5):
    print("Iteration number:", (i + 1))

# C - if-elif conditions
k = int(input("Enter a number between 1 to 4:"))
while 1 <= k <= 4:
    if k == 1:
        print("Summer")
        break
    elif k == 2:
        print("Winter")
        break
    elif k == 3:
        print("Fall")
        break
    else:
        print("Spring")
        break
else:
    print("Numer out of range")

# D
# 1 - Loop will run 10 times
# 2 - 10
count = 1
while count < 11:
    print(count)
    count = count + 1

# E - Personal info
m = {"Age": "30", "fLatter": "G", "Currency": "Shekel", "fAbroad": True, "AptNum": "7"}
print(m)
print(m["Age"] + m["Currency"])

# F - input phone number
n = input("Enter phone number:")
print("phone number:", n)


# G - Functions
# 1
def print_hello(str1):
    print(str1)


print_hello("Hello")


# 2
def calc():
    print(5 + 3.2)


calc()


# H - Functions
# 1
def my_name(name="Unknown"):
    print(name)


my_name("Nikita")


# 2
def divide(num):
    print(num / 2)


g = int(input("Enter a number you would like to divide: "))
divide(g)


# I - Functions
# 1
def return_sum(int1, int2):
    return int1 + int2


num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))
res = return_sum(num1, num2)
print("result is :", res)


# 2
def two_str(str1, str2):
    return str1 + " " + str2


newStr = two_str("cat", "dog")
print(newStr)
