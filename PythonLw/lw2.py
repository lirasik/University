string = str(input("Enter string: "))

print("String without 3rd symbol: ", end = '')
for it, char in enumerate(string):
    if (it == 2):
        continue
    print(char, end = '')
print()

if (string.find('c') != -1):
    print("This string owns symbol \"c\".")
else:
    print("This string doesn't own symbol \"c\".")

print("String length: {}".format(len(string)))
print("String without last symbol: {}".format(string[:-1:]))