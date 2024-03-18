# Day 10 Project👌
from art import calc_logo
from replit import clear


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def power(n1, n2):
    return n1 ** n2


operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '**': power
}
process = 'n'
# instead of while for no condition we can define it as def - function.
while process == 'n':
    clear()
    print(calc_logo)
    result = 0.0
    process = 'y'
    num1 = float(input("What's the first number?: "))
    for keys in operators:
        print(keys)
    while process == 'y':
        operator = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calc_function = operators[operator]
        result = calc_function(num1, num2)

        print(f"{num1} {operator} {num2} = {result}")

        process = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
        )
        num1 = result
