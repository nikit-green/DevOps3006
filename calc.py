import re

print("Calculator")
print("Type 'quit' to exit\n")
previous = 0
run = True


def perform_math():
    global run
    global previous
    eq = input("Enter equation: ")
    if eq == "quit":
        run = False
    else:
        eq = re.sub('[a-zA-Z.,()" "]', '', eq)
        previous = eval(eq)

        print(eq)


while run:
    perform_math()
