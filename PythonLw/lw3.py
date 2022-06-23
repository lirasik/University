import random
import math
print("Possible operations: ")
print("\t+\t\tplus (for 2 numbers)")
print("\t-\t\tminus (for 2 numbers)")
print("\t/\t\tdivision (for 2 numbers)")
print("\t*\t\tmultiply (for 2 numbers)")
print("\t^\t\exponentiation (for 2 numbers)")
print("\tabs\t\tabsolute value (for 1 number)")
print("\trandom\t\trandom value from 0 to 1")
print("\tfactorial\tfactorial (for 1 number)")
print("\tacos\t\tarccosine (for 1 number)")
print("\texit\t\tclose program")
while (True):
    operation = str(input("Enter an operation: "))
    if (operation == '+'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("{} + {} = {}".format(num1, num2, num1 + num2))
    elif (operation == '-'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("{} - {} = {}".format(num1, num2, num1 - num2))
    elif (operation == '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("{} / {} = {}".format(num1, num2, num1 / num2))
    elif (operation == '*'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("{} * {} = {}".format(num1, num2, num1 * num2))
    elif (operation == '^'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("{} ^ {} = {}".format(num1, num2, num1 ** num2))
    elif (operation == 'abs'):
        num = float(input("Enter number: "))
        print("|{}| = {}".format(num, abs(num)))
    elif (operation == 'random'):
        print("Random number: {}".format(random.random()))
    elif (operation == 'factorial'):
        num = int(input("Enter number (only integers): "))
        print("{}! = {}".format(num, math.factorial(num)))
    elif (operation == 'acos'):
        num = float(input("Enter number (from -1 to 1): "))
        print("acos({}) = {}".format(num, math.acos(num)))
    elif (operation == 'exit'):
        break
    else:
        print("No such operator.")