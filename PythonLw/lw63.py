import random
import math

def printHelp():
    print("Possible operations: ")
    print("\thelp\t\tshow this message")
    print("\t+\t\tplus (for 2 numbers)")
    print("\t-\t\tminus (for 2 numbers)")
    print("\t/\t\tdivision (for 2 numbers)")
    print("\t*\t\tmultiply (for 2 numbers)")
    print("\t^\t\texponentiation (for 2 numbers)")
    print("\tabs\t\tabsolute value (for 1 number)")
    print("\trandom\t\trandom value from 0 to 1")
    print("\tfactorial\tfactorial (for 1 number)")
    print("\tacos\t\tarccosine (for 1 number)")
    print("\texit\t\tclose program")

def getTwoFloatNumbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return (num1, num2)

def sumOperation():
    num1, num2 = getTwoFloatNumbers()
    print("{} + {} = {}".format(num1, num2, num1 + num2))

def minusOperation():
    num1, num2 = getTwoFloatNumbers()
    print("{} - {} = {}".format(num1, num2, num1 - num2))

def divisionOperation():
    num1, num2 = getTwoFloatNumbers()
    print("{} / {} = {}".format(num1, num2, num1 / num2))

def multiplyOperation():
    num1, num2 = getTwoFloatNumbers()
    print("{} * {} = {}".format(num1, num2, num1 * num2))

def powerOperation():
    num1, num2 = getTwoFloatNumbers()
    print("{} ^ {} = {}".format(num1, num2, num1 ** num2))

def absoluteOperation():
    num = float(input("Enter number: "))
    print("|{}| = {}".format(num, abs(num)))

def randomOperation():
    print("Random number: {}".format(random.random()))

def factorialOperation():
    num = int(input("Enter number (only integers): "))
    print("{}! = {}".format(num, math.factorial(num)))

def acosOperation():
    num = float(input("Enter number (from -1 to 1): "))
    print("acos({}) = {}".format(num, math.acos(num)))

def main():
    printHelp()
    while (True):
        operation = str(input("Enter an operation: "))
        if (operation == '+'):
            sumOperation()
        elif (operation == '-'):
            minusOperation()
        elif (operation == '/'):
            divisionOperation()
        elif (operation == '*'):
            multiplyOperation()
        elif (operation == '^'):
            powerOperation()
        elif (operation == 'abs'):
            absoluteOperation()
        elif (operation == 'random'):
            randomOperation()
        elif (operation == 'factorial'):
            factorialOperation()
        elif (operation == 'acos'):
            acosOperation()
        elif (operation == 'help'):
            printHelp()
        elif (operation == 'exit'):
            break
        else:
            print("No such operator.")

main()