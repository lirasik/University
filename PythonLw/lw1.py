inputNumber = int(input("Enter input number: "))
borderNumber = int(input("Enter border number: "))
if (inputNumber < borderNumber):
    print(f"{inputNumber} is less than {borderNumber}")
elif (inputNumber < borderNumber * 3):
    print(f"{inputNumber} is more than {borderNumber}")
else:
    print(f"{inputNumber} is more than three times {borderNumber}")