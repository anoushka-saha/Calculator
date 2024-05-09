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

#While loop so user can use again
while True: 

    #Ask user for the second number
    num2 = int(input("What is the second number?: "))

    #Ask user what operation they want
    for sym in operations:
        print(sym)
    opp = input("Choose an operation from the ones above: ")

    #Finding the answer of user's chosen operation
    calc = operations[opp]
    ans = calc(num1, num2)

    #Printing final answer
    print(str(num1) + " " + opp + " " + str(num2) + " = " + str(ans))

    #Asking user if they want to continue, and if they want to use the same number
    again = input("Do you want to go again? (y/n): ")

    if again != "y":
        break
    else:
        same_num = input("Type \"y\" if you want to continue with " + str(ans) + " or \"n\" if you want to use a new number: ")
        if same_num == "n":
            #Ask user for the first number
            num1 = int(input("What is the first number?: "))
        else:
            num1 = ans

