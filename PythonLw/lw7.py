import random
import math

class Calculator:
    @staticmethod
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
    
    @staticmethod
    def handleInput():
        Calculator.printHelp()
        while (True):
            operation = str(input("Enter an operation: "))
            if (operation == '+'):
                Calculator.sumOperation()
            elif (operation == '-'):
                Calculator.minusOperation()
            elif (operation == '/'):
                Calculator.divisionOperation()
            elif (operation == '*'):
                Calculator.multiplyOperation()
            elif (operation == '^'):
                Calculator.powerOperation()
            elif (operation == 'abs'):
                Calculator.absoluteOperation()
            elif (operation == 'random'):
                Calculator.randomOperation()
            elif (operation == 'factorial'):
                Calculator.factorialOperation()
            elif (operation == 'acos'):
                Calculator.acosOperation()
            elif (operation == 'help'):
                Calculator.printHelp()
            elif (operation == 'exit'):
                break
            else:
                print("No such operator.")

    @staticmethod
    def getTwoFloatNumbers():
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return (num1, num2)

    @staticmethod
    def sumOperation():
        num1, num2 = Calculator.getTwoFloatNumbers()
        print("{} + {} = {}".format(num1, num2, num1 + num2))

    @staticmethod
    def minusOperation():
        num1, num2 = Calculator.getTwoFloatNumbers()
        print("{} - {} = {}".format(num1, num2, num1 - num2))

    @staticmethod
    def divisionOperation():
        num1, num2 = Calculator.getTwoFloatNumbers()
        try:
            print("{} / {} = {}".format(num1, num2, num1 / num2))
        except:
            print("Division by zero")

    @staticmethod
    def multiplyOperation():
        num1, num2 = Calculator.getTwoFloatNumbers()
        print("{} * {} = {}".format(num1, num2, num1 * num2))

    @staticmethod
    def powerOperation():
        num1, num2 = Calculator.getTwoFloatNumbers()
        print("{} ^ {} = {}".format(num1, num2, num1 ** num2))

    @staticmethod
    def absoluteOperation():
        num = float(input("Enter number: "))
        print("|{}| = {}".format(num, abs(num)))

    @staticmethod
    def randomOperation():
        print("Random number: {}".format(random.random()))

    @staticmethod
    def factorialOperation():
        num = int(input("Enter number (only integers): "))
        try:
            print("{}! = {}".format(num, math.factorial(num)))
        except:
            print("Float number")

    @staticmethod
    def acosOperation():
        num = float(input("Enter number (from -1 to 1): "))
        try:
            print("acos({}) = {}".format(num, math.acos(num)))
        except:
            print("Number's modulus is greater than 1")

def main():
    Calculator.handleInput()

main()