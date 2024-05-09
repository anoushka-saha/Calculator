#Anoushka Saha
#Calculator
#May 9th, 2024
#Day 10 Final Project

#Addition function
def add(int1, int2):
    return int1 + int2

#Subtraction function
def subtract(int1, int2):
    return int1 - int2

#Multiplication function
def multi(int1, int2):
    return int1 * int2

#Division function
def div(int1, int2):
    return int1 / int2

#Dictionary of operations
operations = {
    "+": add,
    "-": subtract,
    "*": multi,
    "/": div
}

#Ask user for the first number
num1 = int(input("What is the first number?: "))

#Ask user for the second number
num2 = int(input("What is the second number?: "))

#Ask user what operation they want
for sym in operations:
    print(sym)
opp = input("Choose an operation from the ones above: ")

