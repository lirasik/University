fruitNames = []
fruitCounts = []

for i in range(3):
    word = str(input("Enter word: "))
    fruitNames.append(word)
print()

print("Fruit names with lower case:")
for fruit in fruitNames:
    print(fruit.lower())
print()

print("Fruit names with upper case:")
for fruit in fruitNames:
    print(fruit.upper())
print()

print("Fruit names with upper case:")
for fruit in fruitNames:
    print(fruit.capitalize())
print()

for fruit in fruitNames:
    number = int(input("Enter {} count: ".format(fruit)))
    fruitCounts.append(number)
print()

for i in range(3):
    fruitName = fruitNames[i]
    fruitCount = fruitCounts[i]
    print("{} count is {}".format(fruitName, fruitCount).capitalize())
print()